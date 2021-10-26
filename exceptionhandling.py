a=8
b=0

try:
    print("hey hi you open  connection")
    print(a/b)
    k = int (input("enter nummber"))
    print(k)

except ZeroDivisionError as e:
    print("hey you add zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("some thing went wrong",e)
finally:
    print("hey you got disconnected")
print("bye")

