from pwn import *
import random
import time

conn = remote('number.wanictf.org', 60000)

randnum = random.randint(0, 500000)
tries = 0

while tries != 20:
    res = conn.recvuntil("input:")
    #print(res)

    print("What?"+str(res.splitlines()[0]))
    
    print(conn.recvuntil("times").splitlines())

        #conn.sendline(str(randnum))
    if res.splitlines()[0] == b"too small":
        random.seed(time.time())
        randnum = random.randint(randnum, 500000)
        
        #randnum += 500
        print(randnum)
        #conn.sendline(str(randnum))
    elif res.splitlines()[0] == b"too big":
        random.seed(time.time())
        randnum = random.randint(0, randnum)
        #randnum -= 500
        print(randnum)
        #conn.sendline(str(randnum))
    #else:
    #    print(conn.recvline())

    print("sending + ", randnum)
    conn.sendline(str(randnum))
  
    #res = conn.recvuntil("input:")

    #if res.splitlines()[3] == "too small":
    #    print("too small broski")


    tries += 1
conn.close()
