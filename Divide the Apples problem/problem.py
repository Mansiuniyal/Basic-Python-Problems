print("Divide the apples problem")
print("Input the No. of apples harry has got")
n=int(input())
print("Input the minimum range")
min=int(input())
print("Input the maximum range")
max=int(input())
if(min==max):
    print("This is not a range")
else:
    for i in range(min,max+1):
        if n%i==0:
            print(f"{i} is divisor of {n}")

