temperature_user = float(input("Temperature: "))

if temperature_user < 30:
    print("Too cold")
elif temperature_user > 100:
    print("Too hot")
else: 
    print("Just right")