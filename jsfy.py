import jsbeautifier,sys,os

folder = sys.argv[1]

os.chdir(os.path.join(os.getcwd(),folder))

files=[]
for file in os.listdir('./'):
    files.append(file)

for file in files:
    if file.endswith('.js'):
        print('Done > ',file)
        try:
            opts = jsbeautifier.default_options()
            # opts.indent_size = 2
            # opts.space_in_empty_paren = True
            opts.eol = r'\r\n'
            opts.preserve_newlines = False
            # res = jsbeautifier.beautify('some javascript', opts)
            res = jsbeautifier.beautify_file(file, opts)
            with open(file,"w+",encoding='utf-8',errors='ignore') as f:
                f.write(res)
        except Exception:
            print(Exception)
        
