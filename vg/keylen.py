def getKeyLen(cipherText): # 获取密钥长度
    keylength = 1
    maxCount = 0
    for step in range(3,10): # 循环密钥长度
        count = 0
        for i in range(len(cipherText)-step): #range(step,len(cipherText)-step):
            if cipherText[i] == cipherText[i+step]:
                 count += 1
        if count>maxCount:
            maxCount = count
            keylength = step
    return keylength

f = open("./cipher.txt","r")
text = f.read()
f.close()
print(getKeyLen(text))