a = 'anhuiuniversityofscienceandtechnology'
print(len(a)*8)
d = ''
for i in a:
    b = ord(i)
    c = bin(b).replace('0b','')
    if(len(c)<8):
        d+='0'*(8-len(c))
        d+=c
e=len(d)
e = bin(e).replace('0b','')
d+='1'
for i in range(len(d),512-len(e)):
    d+='0'
d = d+e
print(d)