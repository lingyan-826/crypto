from string import ascii_lowercase

#加密代码
def cip(plainstr,key,sLen,kLen):
    cip = ""
    for i in range(0,sLen):
        j = i%kLen
        if plainstr[i] not in ascii_lowercase:
            cip += plainstr[i]
            continue
        a = (ord(plainstr[i])-ord('a')+ord(key[j])-ord('a'))%26+ord('a')
        cip += chr(a)
    return cip

#解密代码
def plai(cipher,key,kLen,sLen):
    plai = ""
    for i in range(0,sLen):
        j = i%kLen
        if cipher[i] not in ascii_lowercase:
            plai += cipher[i]
            continue
        a = (ord(cipher[i])-ord(key[j]))%26+ord('a')
        plai += chr(a)
    return plai


plainstr = input("输入明文:")
key = input("输入密钥:")
sLen = len(plainstr)
kLen = len(key)
cipher = ""
plain = ""
cipher = cip(plainstr,key,sLen,kLen)
print("加密后：",end=" ")
print(cipher)
print("解密后：",end=" ")
plain = plai(cipher,key,kLen,sLen)
print(plain)