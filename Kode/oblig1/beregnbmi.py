weight_in_kilo   = float( input("Enter weight in kilo: ") )
height_in_meters = float( input("Enter height in meters: ") )

bmi = weight_in_kilo / (height_in_meters**2)

print(f"Your BMI is {bmi:.1f}")   #En desimal er nok