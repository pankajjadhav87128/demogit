list = [21,1,2,9,5,1,]
n = 9
pos = -1

def search(list,n):
    global pos
    i =0
    print("her")
    while i < (len(list)):
        print("her2")
        if list[i] == n:
            pos= i
            return True
        i +=1

    return False




if search(list,n):
    print("founf at",pos+1)
else:
    print("not found")