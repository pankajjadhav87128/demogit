f = open("img.png", "rb")
f1 = open("mypic.JPG","wb")
for i in f:
    f1.write(i)