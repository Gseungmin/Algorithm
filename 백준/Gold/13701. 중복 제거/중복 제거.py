import sys
import os
#import tracemalloc

def read_word():

    unstdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=1000000)
    ch = unstdin.read(1)
    while True:
        num = 0
        while not (ch == b'\n' or ch == b'' or (ch >= b'0' and ch <= b'9')):
            ch = unstdin.read(1)
        if ch == b'\n' or ch == b'':
            break
        while ch >= b'0' and ch <= b'9':
            num = num * 10 + int(ch)
            ch = unstdin.read(1)
        yield num

def set_bit(n):
    nn = n // 8
    nr = n % 8

    ret = (bits[nn] & (1 << nr)) == 0

    bits[nn] |= (1 << nr)

    return ret

if __name__ == '__main__':
    bits = bytearray(4194304)

    try:
        sys.stdin = open("13701_input.txt")
    except FileNotFoundError:
        pass

    for num in read_word():
        if set_bit(num) == True:
            print(num, end=" ")
    print()