import datetime
# usertime = float(input("What hour is it? (0-23)"));

usertime = datetime.datetime.now()
print(usertime.hour)

if usertime.hour <=5:
    print("It's early, You should be sleeping")
elif usertime.hour <=7:
    print("Wake up, brew that coffee, get that mile run in, and get that breakfast...")
elif usertime.hour <=9:
    print("Time to go to work.")
elif usertime.hour <=12:
    print("You should be working")
elif usertime.hour <=13:
    print("Take your lunch break")
elif usertime.hour <=17:
    print("Do you feel that afternoon lull?")
elif usertime.hour <=19:
    print("Time to hit the gym")
elif usertime.hour <=21:
    print("Gotta eat that dinner")
elif usertime.hour <=23:
    print("Get that SLEEP. And rePEAT!")
else:
    print("You didn't type an acceptable value")