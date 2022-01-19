#Programmet beregner det initielle innskuddet på en sparekonto dersom
#en kjenner hva sluttsummen har blitt etter at innskuddet har stått der
#et bestemt antall år med en bestemt årlig rentesats

final_account_value           = float( input("Final account value: ") )
yearly_interest_rate_percent  = float( input("Yearly interest rate(%): ") )
number_of_years               = float( input("Number of years: ") )

#Gjør om til prosentfaktor og deler på 12 måneder
monthly_interest_rate = yearly_interest_rate_percent/1200  
number_of_months = number_of_years * 12

initial_deposit_amount = ( final_account_value / 
                           (1 + monthly_interest_rate)**number_of_months )

print(initial_deposit_amount)

