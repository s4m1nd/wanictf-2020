from pwn import *
import random
import time

conn = remote('number.wanictf.org', 60000)
#conn = process(["./number.py"])
tries = 0
while tries != 20:
    res = conn.recvuntil("input:")
    #print(res)

    print("What?"+str(res.splitlines()[0]))
    
    low = 0
    high = 500000
    randnum = 50

    conn.sendline(str(high//2))
    
    res = conn.recvuntil("input:")

    if res.splitlines()[0] == b"too small":
        #random.seed(time.time())
        #randnum = random.randint(randnum, 500000)
        low = randnum + 1

        #randnum += high - mid / 2
        print(randnum)
        #conn.sendline(str(randnum))
    elif res.splitlines()[0] == b"too big":
        #randnum = random.randint(0, randnum)
        high = randnum

        #randnum = randnum / 2
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
