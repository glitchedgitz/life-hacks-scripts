import sys
import os
import argparse
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
# import keyboard as k
# k.add_hotkey("ctrl+c", lambda: quit())

def help():
    print('''

   |\      _,,,---,,_
   /,`.-'`'    -.  ;-;;,_    RUN CAT RUN!!
  |,4-  ) )-,_..;\ (  `'-'   
 '---''(_/--'  `-'\_)        

OPTIONS:
    -h      Kill your system
    -t      Threads
    -m      Work with threads, either 0/1 (default 0)
                0 - ThreadPool/Lightweight
                1 - ProcessPool/Heavyweight
                    eg. - screenshotting tools
                        - tool using huge files 
    -seq    Print output sequence-wise
                Command 1   >   Output 1
                Command 2   >   Output 2
                ..              ..
                ..              ..
                Command n   >   Output n
    -skip   Skip commands to print with output
    
ASCII ART:
    https://user.xmission.com/~emailbox/ascii_cats.htm''')
    sys.exit(0)

def parser_error(errmsg):
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():
    parser = argparse.ArgumentParser(add_help=False)
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-t', type=int, default=1)
    parser.add_argument('-m', type=int, default=0)
    parser.add_argument('-seq', default=False, action='store_true')
    parser.add_argument('-h', default=False, action='store_true')
    return parser.parse_args()

def do(cmd):
    try:
        print("Running... ",cmd)
        data = os.popen(cmd).read()
        return data
    except (KeyboardInterrupt, SystemExit):
        print('Closing Thread')
        return

def run(executor ,seq):
    if seq:
        results = executor.map(do, sys.stdin)
        for r in results:
            print(r)
    else:
        results = [executor.submit(do, cmd) for cmd in sys.stdin]
        for f in as_completed(results):
            print(f.result())

def main():
    args = parse_args()
    if args.h:
        help()

    if args.t == 1:
        for cmd in sys.stdin:
            print(do(cmd))
    else:
        if args.m == 0:
            with ThreadPoolExecutor(args.t) as executor:
                run(executor, args.seq)
        elif args.m == 1:
            with ProcessPoolExecutor(args.t) as executor:
                run(executor, args.seq)
        else:
            print("m can be 0 or 1, check usage")

if __name__ == '__main__':
    main()
