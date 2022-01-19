#Programmet finner stigningstallet til den rette
#linjen mellom to brukervalgte punkter


x_1 = float(input("Skriv inn x-verdi for punkt 1"))
y_1 = float(input("Skrv inn y-verdi for punkt 1"))
x_2 = float(input("Skriv inn x-verdi for punkt 2"))
y_2 = float(input("Skriv inn y-verdi for punkt 2"))

stigningstall = (y_1 - y_2) / (x_1 - x_2)

print(f"Stigningstallet til linjen mellom ({x_1}, {y_1})"
+ f"({x_2}, {y_2}) er {stigningstall}") 
