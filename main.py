#Write a program that calculates the time it takes for a car to reach its destination.

print (""" 
---------------------------------------------------------
-----------------Exercise 16 ----------------------------
---------------------------------------------------------""")

def travel_time():
    distance = float(input("Please enter the distance to travel: "))
    speed = float(input("Please enter the average speed: "))

    time_hours = distance/speed

    hours = int(time_hours)
    minutes = (time_hours - hours)*60

    print (f"El tiempo estimado de viaje es: {hours} hours and {minutes:.0f} minutes")

    if speed > 120:
        print ("Warning! You are exceeding the speed limit")

travel_time()