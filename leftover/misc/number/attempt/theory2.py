import random
from pwn import *

p = remote('number.wanictf.org', 60000)

def computer_guess():
    low = 1
    high = 500000
    guess = 1
    tries = 1
    while tries != 20:
        res = p.recvuntil("input:")

        guess = (low+high)//2
        
        print("Guess: ", guess)
        p.sendline(str(guess))
        
        res = p.recvuntil("input:")
        if res.splitlines()[0] == b"too big":
            high = guess
            print("big, ", high)
        elif res.splitlines()[0] == b"too small":
            low = guess + 1
            print("low, ", low)

        p.sendline(str(guess))

        tries += 1
    p.interactive()

def main():
    computer_guess()

if __name__ == '__main__':
    main()
