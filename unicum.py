#Class to create liquor bottle objects
class Liquor(): #define alcohol content and LLA (absolute alcohol)
    def __init__ (self, name, liters, alcohol_content, retail_price, cost_at_LCBO):
        #inputed variables to be accessible once the object is instantiated
        self.name = name
        self.alcoholcontent = alcohol_content #alcohol content in %
        self.lla = liters*alcohol_content #LLA (absolute alcohol content)
        self.retail_price = retail_price #Retail Price in CAD
        self.cost_at_LCBO = cost_at_LCBO

        #alcohol import duty at a rate of $0.0492 per liter of absolute alcohol 
        self.alcohol_import_duty = (self.lla)*0.049
        #excise tax/duty at $11.696 per liter
        self.excise_tax = 11.696*(self.lla)
        #Border Levy at a rate of 59.9% of the retail price + import duty + excise tax
        self.border_levy = ((0.599)*(retail_price)) + (self.alcohol_import_duty) + (self.excise_tax)
        #HST
        self.HST = retail_price*0.13 + self.alcohol_import_duty + self.excise_tax
        #Bottle Deposit
        if liters >= 0.63:
            self.bottle_deposit = 0.20
        elif liters < 0.63:
            self.bottle_deposit = 0.10

        #TOTAL COST OF THE LIQUOR AFTER IMPORTING
        self.total_cost = self.retail_price + self.HST+ self.border_levy + self.bottle_deposit

#Function to return any options we might be interested in for our object.
def return_bottle_info(bottle):
    print(f'Inputed Variables for {bottle.name}: {bottle.alcoholcontent}% alcohol content at ${unicum_magyar.retail_price} per bottle.')
    print(f'The LLA content is {bottle.lla}')
    print(f'The "Import Duty" for absolute alcohol to be paid per bottle are ${bottle.alcohol_import_duty}')
    print(f'The "Excise Tax/Duty\'s" for absolute alcohol to be paid per bottle are ${bottle.excise_tax}')
    print(f'The "Border Levy" for to be paid per bottle is ${bottle.border_levy}')
    print(f'The HST to be paid per bottle is ${bottle.HST}')

    print(f'The total cost per bottle is {bottle.total_cost}')
    print(f'You save ${bottle.cost_at_LCBO - bottle.total_cost}')

#Example Liquors to Import into Ontario: 
unicum_magyar = Liquor('Unicum', 0.5, 0.345, 16.85, 34.00)
fortnite_chugjug = Liquor('Chug Jug', 1, 0.5, 20, 1000) 


return_bottle_info (unicum_magyar)
return_bottle_info (fortnite_chugjug)