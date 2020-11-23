import random
from pwn import *

p = remote('number.wanictf.org', 60000)

def computer_guess():
    low = 1
    high = 500000
    guess = 1
    p.recvuntil(":")
    p.sendline(str(first_guess))
    while i != 20:
        res = p.recvuntil("input:")
        #print("Guess: ", guess)
        #p.sendline(str(guess))
        v[i].append(first_guess) 
        #res = p.recvuntil("input:")
        if res.splitlines()[0] == b"too big":
            #high = guess
            v[i+1].append(v[i]//2)
            print("big, ", v[i+1])
        elif res.splitlines()[0] == b"too small":
            #low = guess + 1
            v[i+1].append((high + (v[i-2] + v[i-1])//2)//2)
            print("low, ", v[i+1])

        p.sendline(str(v[i]))

        i+=1
    p.interactive()

def main():
    computer_guess()

if __name__ == '__main__':
    main()
