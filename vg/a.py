from string import ascii_uppercase
v=""
f = open("./plain.txt","r")
a = f.read()
f.close()
a = a.lower()
f = open("./plain.txt","w")
f.write(a)
f.close()
