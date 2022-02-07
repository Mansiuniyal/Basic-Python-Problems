food_calories=list(map(int,input("Enter The Calories:").split()))
print(food_calories)
#Built in function
l2=list(reversed(food_calories))
#slice method
l3=food_calories[::-1]

#Swap method
length=len(food_calories)
for i in range(length//2):
    temp=food_calories[i]
    food_calories[i]=food_calories[-1+-i]
    food_calories[-i+-1]=temp
print(l2)
print(l3)
print(food_calories)
