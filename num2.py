from string import ascii_lowercase

keyMar = []

plain = input("输入明文：")
key = input("输入密钥：")
pLen = len(plain)
kLen = len(key)
k = 0
a = ''
for i in range(0,24):
    if(k<kLen):
        if key[k] not in keyMar:
            keyMar.insert(i,key[k])
            if(key[k] == 'i'):
                keyMar.insert(25,'j')
            if(key[k] == 'j'):
                keyMar.insert(25,'i')
            k += 1
    else:
        for a in ascii_lowercase:
            if a not in keyMar:
                keyMar.append(a)
for j in range(0,25):
    print(keyMar[j],end=' ')