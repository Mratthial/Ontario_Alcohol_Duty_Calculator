from Ontario_Alcohol_Duties import * 

'''
Please create a list of any alcohol that you would like to have information for.  The format is as follows:
    (alcohol type, Name of alcohol, Bottle Volume in Liters, Alcohol Content%, Price Paid, Cost at the LCBO)
    
    Index's 0 to 4 are necessary to calculate the cost of all applicable duties and fees needed to be paid once imported.
    
    Index 0: alcohol type    
        Alcohol type can either be: 
            1. liquor
            2. wine
            3. beer
        All of these types of alcohol types have their own respective duties and fees associated.
    
    Index 1: Name of alcohol
        What is the name of the alcohol that you are importing.  This is given to return the name with the information
        you are requesting, so it is clear what information pertains to which bottle.

    Index 2: Bottle Volume
        The volume of the entire bottle in Liters.  Can include as many decimal points as the bottle gives. 
        Bottle volume is used to calculate the bottle deposit (either 10 or 20 cents per bottle) and the amount of 
        total pure alcohol content in the bottle with information given in alcohol percentage content
    
    Index 3: Alcohol Content %
        The percentage of alcohol that is in the bottle.  This is used to calculate total pure alcohol content in the bottle.

    Index 4: Price Paid
        What is the price paid for the bottle that you are importing.  This must be in Canadian dollars.

    Index 5: Price at the LCBO
        This is not a necessary field.  The price at the LCBO is used for interrest to determine the value of importing a specific alcohol
        into Canada.  If the price at the LCBO is similar or cheaper than the price paid overseas, duties, and taxes, it is in your best 
        interest to not import this alcohol and purchase it in Ontario.  However, certain alcohols will not be purchasable at the LCBO 
        and are only available over seas.  In this case, it is logical to import the bottle.
'''

#Example Liquors to Import into Ontario: 
unicum_magyar = Liquor('liquor', 'Unicum', 0.50, 0.345, 16.85, 34.00)
fortnite_chugjug = Liquor('liquor', 'Chug Jug', 1.00, 0.50, 20, 1000.00) 
tokaj = Liquor('wine', 'Tokaj Szamorodni', 0.50,  0.05, 8.00, 15.00)
yummy_beer = Liquor('beer','Yummy Beer', 3.785, 0.03, 15.00, 20.00) #A 12 pack of 12 OZ cans = 3.785 Liters
test1_alcohol_LCBO_website = Liquor('liquor', 'Test_Liquor1', 0.75, 0.40, 21.95, 0)
vajk_wine = Liquor('wine', 'King Vajk', 0.6, 0.10, 23, 36)

#THINGS I AM BRINGING TO CANADA
Fütyülös_Palinka = Liquor('liquor', 'Fütyülös Palinka', 0.500, 0.245, 11.10, 30.00,)
Tokaji = Liquor('wine', 'Tokaji Basic', 0.500, 0.10, 10.35)
Tokaji_öt_Puntos = Liquor('wine', 'Tokaji Öt Pontos', 0.500, 0.10, 17.26, 40.00)
Sparkling_Selection_2x750ml = Liquor('wine', 'Sparkling Selection 2 750ml', 1.5, 0.12, 44.11, 80.00)
Sparkling_Selection_3x200ml = Liquor('wine', 'Sparking Selection 3 Minis', 0.600, 0.115, 22.05, 40.00, 2)

#change list of characteristics to a dictionary for key item pairs