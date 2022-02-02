print("Age Detector")
print("Enter either the birth year or the age of a person")
isAge=False
isYear=False
y=int(input())
if len(str(y))==4:
    isYear=True
else:
    isAge=True
if y<1900 and isYear:
    print("You seem to be the oldest person alive!")
if y>2022:
    print("You are not yet born")
if isAge:
    y=2022-y

print(f"You will be 100 years old in {y+100}")

interestedYear=int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - y} years old in {interestedYear}")
