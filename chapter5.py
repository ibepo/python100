cars = ["audi", "bwm", "toyota"]
for car in cars:
    if car == "bwm":
        print(car.upper())
    else:
        print(car.title())

if "audi" in cars:
    print("yes,i am in it")

if "hoda" not in cars:
    print("yes,i am not in it")


age_0 = 10
age_1 = 20
age_2 = 30

if age_2 > age_0 and age_2 > age_1:
    print(f"yes,i am {age_2}")

age = 12
if age < 4:
    print("kid")
elif age < 18:
    print("young")
else:
    print("old")

requested_top = []

if not requested_top:
    print("your requested_top is empty")
