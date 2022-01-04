
def Age_detail(Age):
    if Age> 0 and Age<= 110:
        return True
    return False 
while True:
    try:
        County_detail =str(input("Enter the Name of YOur Country ")).upper()
        Age = int(input("Enter Your Age "))
        
    except ValueError:
        print('Sorry, your Age response must not be String or real')
        continue

    if Age_detail(Age):  
        break
    print('Do not do Price Calculation')

# def Country_detail():
           #Country_detail.var =str(input("Enter the Name of YOur Country ")).upper()
        #    Name_casefold = Name.upper()
        #    return Name_casefold
def fare_calcul():
           Age #, Country_detail.var
           Ticketfare = 40
           Federick_fare = 35
           if Age >= 65:
                   Age_Cal = Ticketfare*0.50
                   Age_Discount_above65 = Ticketfare - Age_Cal
                   print("The Tickect Fare :" + "$" +" "+str(Age_Discount_above65))
           elif Age <= 6:
                   print('Ticket Free For Below 6 years')
                   
            # elif Country_detail.var == "FREDERICK":
           elif County_detail == "FREDERICK":
                    Federick_fare = 35
                    if Age >=  65 and County_detail == "FREDERICK":
                        Federick_Cal = Federick_fare*0.5  
                        Federick_offer = Federick_fare - Federick_Cal
                        print("The Tickect Fare :" + "$" +" "+ str(Federick_offer))  
                    else:
                        print('The Ticket Fare : $35')          
           else:
                print('The Ticket Fare : $40')
        
               
def main():
    Age_detail(Age)
    # Country_detail()
    fare_calcul()
    
main()