#Programmet skriver ut en tilfeldig måned og månedens tilhørende tall

import random

random_number_representing_month = random.randint(1, 12)

if random_number_representing_month == 1:
    print("January")
elif random_number_representing_month==2:
    print("February")
elif random_number_representing_month==3:
    print("March")
elif random_number_representing_month==4:
    print("April")
elif random_number_representing_month==5:
    print("May")
elif random_number_representing_month==6:
    print("June")
elif random_number_representing_month==7:
    print("July")
elif random_number_representing_month==8:
    print("August")
elif random_number_representing_month==9:
    print("September")
elif random_number_representing_month==10:
    print("October")
elif random_number_representing_month==11:
    print("November")
else:
    print("December")

print(random_number_representing_month)