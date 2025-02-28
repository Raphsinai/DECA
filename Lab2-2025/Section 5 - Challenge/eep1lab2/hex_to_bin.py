def convert(content):
    from builtins import bin
    print("got\n", content)
    result = []
    l = True
    if content is not list:
        print('it is not a list')
        l = False
        content = content.strip().split('\n')
    print(type(content))
    print(content)
    for line in content:
        if len(line) == 1:
            print('only instruction in lines')
            print("instruction:", line[2:])
            result.append(bin(int(line[2:], 16)))
        else:
            line = line.split(' ')
            print('address and instruction in line')
            newline = ""
            print("address:", line[0][2:])
            adbin = bin(int(line[0][2:], 16))
            while len(adbin) < 5:
                adbin = '0b0' + adbin[2:]
            newline += adbin
            newline += " "
            print("instruction:", line[1][2:])
            insbin = bin(int(line[1][2:], 16))
            while len(insbin) < 18:
                insbin = '0b0' + insbin[2:]
            insbin = f"{insbin[:6]} {insbin[6:10]} {insbin[10:14]} {insbin[14:18]}"
            newline += insbin
            result.append(newline)
    if l:
        return result
    return '\n'.join(result)
            


if __name__ == "__main__":
    import os, sys
    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    for file in os.listdir():
        print(file)
        if os.path.isfile(file):
            print("checking if ram...")
            if file.endswith('.ram'):
                print("it is ram!")
                with open(file, 'r') as ram:
                    hexcont = ram.read()
                    print('read hex content')
                    ram.close()
                with open(file[:-3] + 'bin', 'w') as bin:
                    bincont = convert(hexcont)
                    print('converted to bin')
                    bin.write(bincont)
                    bin.close()
                print(f"done with {file}")