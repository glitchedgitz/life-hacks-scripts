package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/giteshnxtlvl/cook/pkg/cook"
	"github.com/giteshnxtlvl/cook/pkg/parse"
)

var (
	help          = parse.B("-h", "-help")
	showColor     = parse.B("-c", "-color")
	reverseSearch = parse.B("-r", "-reverse")
)

var banner = `
    GREP FOR COOK
    Usage         : cat urls.txt | ck [flags] [set] [set] [set] ... [set]

    Normal Grep   : cat urls.txt | ck admin_set api conf
    Reverse Grep  : cat urls.txt | ck -r raft_ext 
    Show Color    : cat urls.txt | ck -c admin_set api conf
    Mutiple Cases : cat urls.txt | ck -c -r admin_set api conf
`

func main() {
	parse.Help = banner

	parse.Parse()

	cook.CookConfig()

	parse.Parse()

	if help {
		fmt.Print(banner)
		os.Exit(0)
	}

	if !showColor {
		cook.Blue = ""
		cook.Reset = ""
	}

	parse.Help = banner

	pattern := parse.Args

	columnValues := []string{}

	for _, p := range pattern {
		if cook.RawInput(p, &columnValues) || cook.ParseRanges(p, &columnValues) || cook.CheckYaml(p, &columnValues) {
			continue
		}

		columnValues = append(columnValues, p)
	}

	sc := bufio.NewScanner(os.Stdin)

	for sc.Scan() {
		line := sc.Text()
		if line == "" {
			continue
		}
		tmpline := strings.ToLower(line)
		for _, val := range columnValues {
			val := strings.ToLower(val)
			valLen := len(val)
			index := strings.Index(tmpline, val)
			if index > -1 && !reverseSearch {
				found := line[index : index+valLen]
				line = strings.ReplaceAll(line, found, cook.Blue+found+cook.Reset)
				fmt.Println(line)
			} else if index == -1 && reverseSearch {
				fmt.Println(line)
			}
		}
	}
}
