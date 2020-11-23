from pwn import *

"""
seth@pyramid:~/Desktop/ctf/wanictf-2020/crypto/basic-rsa$ python ./solve.py 
[+] Opening connection to rsa.wanictf.org on port 50000: Done
[+] Correct! Here's your reward: FLAG{y0uv3_und3rst00d_t3xtb00k_RSA}
[*] Closed connection to rsa.wanictf.org port 50000
seth@pyramid:~/Desktop/ctf/wanictf-2020/crypto/basic-rsa$ 
"""

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m


conn = remote('rsa.wanictf.org',50000)
#conn.recvline()
res = conn.recvuntil(" > ").decode('utf-8').splitlines()
p = int(res[-3].split(" ")[2])
q = int(res[-2].split(" ")[2])
n = p*q
conn.sendline(str(n))

#chall2
res = conn.recvuntil(" > ").decode('utf-8').splitlines()
n = int(res[-2].split(" ")[2])
e = int(res[-3].split(" ")[2])
m = int(res[-4].split(" ")[2])
c = m ** e % n
conn.sendline(str(c))

#chall 3
res = conn.recvuntil(" > ").decode('utf-8').splitlines()
#print(res)
c = int(res[-2].split(" ")[2])
e = int(res[-3].split(" ")[2])
q = int(res[-4].split(" ")[2])
p = int(res[-5].split(" ")[2])
n = p*q
phi = ( q - 1 ) * ( p - 1 )
d = modinv( e, phi )
m = pow( c, d, n )

conn.sendline(str(m))

#getflag
res = conn.recvuntil("}")
print(res)

conn.close()
