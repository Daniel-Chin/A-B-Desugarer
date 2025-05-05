import re

WILDCARD = 'a totally reserved string'

def multilineInput():
    while True:
        try:
            yield input()
        except EOFError:
            break

def main():
    print(transform('\n'.join(multilineInput())))

def transform(x: str, /):
    buf = []
    for line in x.splitlines():
        line = re.sub(r'(?<!\\)\?', WILDCARD, line)
        line = line.replace('\\\\', '\\').replace('\\?', '?')
        if WILDCARD in line:
            for c in 'abc':
                buf.append(line.replace(WILDCARD, c))
        else:
            buf.append(line)
    return '\n'.join(buf)

def test():
    src = r'''
    ?|=|?
    # \? \\ \\\?
'''
    print('in:')
    print(src)
    print('out:')
    print(transform(src))
    input('Enter...')

if __name__ == "__main__":
    # test()
    main()
