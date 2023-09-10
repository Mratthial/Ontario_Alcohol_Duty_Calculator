import sys

#Class to create liquor bottle objects
class Liquor(): #define alcohol content and LLA (absolute alcohol)
    def __init__ (self, alcohol_type, name, liters, alcohol_content, retail_price, cost_at_LCBO = 0, unit_bottles = 1):
        #inputed variables to be accessible once the object is instantiated
        self.name = name
        self.alcoholcontent = alcohol_content #alcohol content in %
        self.unit_bottles = unit_bottles #how many bottles/units of this item you are bringing
        self.liters = liters
        self.lla = liters * alcohol_content #LLA (absolute alcohol content)
        self.retail_price = retail_price #Retail Price in CAD
        self.cost_at_LCBO = cost_at_LCBO
        self.alcohol_type = alcohol_type
        
        #Bottle Deposit
        if liters >= 0.63:
            self.bottle_deposit = 0.20
        elif liters < 0.63:
            self.bottle_deposit = 0.10
        
        if alcohol_type == 'liquor':
            #alcohol import duty at a rate of $0.0492 per liter of absolute alcohol 
            self.alcohol_import_duty = round((self.lla)*0.0492, 4)
            #excise tax/duty at $11.696 per liter
            self.excise_tax = round((11.696*(self.lla)), 4)
            #Border Levy at a rate of 59.9% of the (retail price + import duty + excise tax)
            self.border_levy = round((0.599 * (retail_price + self.alcohol_import_duty + self.excise_tax)), 2)
            #HST
            self.HST = round((0.13*(retail_price + self.alcohol_import_duty + self.excise_tax)), 2)

        elif alcohol_type == 'wine':
            #alcohol import duty at a rate of $0.0187 per liter of wine
            self.alcohol_import_duty = round((self.liters * 0.0187), 4) #round to 4 decimals
            #excise tax/duty at $0.62 per liter of wine
            self.excise_tax = round((0.62*(self.liters)), 4) #round to 4 decimals
            #Border Levy at a rate of 39.6% of the retail price + import duty + excise tax
            self.border_levy = round(0.396 * ((retail_price) + (self.alcohol_import_duty) + (self.excise_tax)), 2) #round to 2 decimals 
            #HST
            self.HST = round((0.13*(retail_price + self.alcohol_import_duty + self.excise_tax)), 2) #round to 2 decimal places

        elif alcohol_type == 'beer':
            #no import duty's for beer 
            self.alcohol_import_duty = 0 
            #excise tax/duty at $0.31 per liter of beer
            self.excise_tax = 0.31 * (self.liters)
            #Border Levy at a rate of $0.676 per liter of beer
            self.border_levy = self.liters * 0.676
            #HST
            self.HST = 0.13*(retail_price + self.alcohol_import_duty + self.excise_tax)

        #TOTAL COST OF THE LIQUOR AFTER IMPORTING
        self.total_cost = round((self.retail_price + self.alcohol_import_duty + self.excise_tax + self.border_levy + self.HST + self.bottle_deposit), 2)

#Function to return any options we might be interested in for the bottles.
def return_all_info(bottle):
    print(f'Inputed Variables for {bottle.name}: Volume of {bottle.liters} with a {bottle.alcoholcontent}% alcohol content at ${bottle.retail_price} per bottle.')
    print(f'The LLA content is {bottle.lla}')
    print(f'The "Import Duty" for absolute alcohol to be paid is ${bottle.alcohol_import_duty}')
    print(f'The "Excise Tax/Duty\'s" for absolute alcohol to be paid is ${bottle.excise_tax}')
    print(f'The "Border Levy" to be paid is ${bottle.border_levy}')
    print(f'The HST to be paid per bottle is ${bottle.HST}')
    print(f'The total cost is {bottle.total_cost}')
    print(f'You save ${bottle.cost_at_LCBO - bottle.total_cost}\n')

def return_bottle_info(bottle):
    print(f'{bottle.name}: \nVolume of {bottle.liters} with a {bottle.alcoholcontent}% alcohol content at ${bottle.retail_price} per unit.\n')

def return_final_price_with_initial(bottle):
    print (f'\n{bottle.name}')
    print (f'You are bringing {bottle.unit_bottles} units of {bottle.name}.')
    print (f'The "Border Levy" to be paid is ${(bottle.unit_bottles)*(bottle.border_levy)} and HST of ${(bottle.unit_bottles)*(bottle.HST)}')
    print(f'The total cost is {(bottle.unit_bottles) * (bottle.total_cost)}\n')

def return_duties_and_taxes(bottle):
    print (f'\n{bottle.name}')
    print (f'You are bringing {bottle.unit_bottles} units of {bottle.name}.')
    print (f'The "Border Levy" to be paid for {bottle.unit_bottles} unit(s) is ${(bottle.unit_bottles)*(bottle.border_levy)} and HST of ${(bottle.unit_bottles)*(bottle.HST)}')

#While loop to ask which function we would like to run that were defined above.  Will continue to loop until a valid option is given.  
#When a valid option is given, returns the function, and asks if you want more info.  Loops until valid answer or told 'no' to break loop.
def give_info():
    need_info = True
    while need_info == True:
        try:
            ask_function = input(
                '''\nWhat information are you interested in?
                \n1. All bottle information.
                \n2. Initital Price and all applicable duties and taxes.
                \n3. Only the the applicable duties and taxes for all bottles.
                \n4. Relevant info for Canada Border Service Agents for all bottles.
                \nPlease respond with "1", "2", "3", or "4"\n'''
                )
            
            if ask_function == '1':
                for item in import_list:
                    return_all_info(item)
                
            elif ask_function == '2':
                for item in import_list:
                    return_final_price_with_initial(item)
                    
            elif ask_function == '3':
                for item in import_list:
                    return_duties_and_taxes(item)
            
            elif ask_function == '4':
                for item in import_list:
                    return_bottle_info(item)
            else:
                print('Please enter a valid input!')
        except:
            print('An error occurred. Please enter a valid option!')
        
        #asks if wanted to run another option of the functions.  
        while True:    
            continue_helping = input('''\nWould you like any more information?  Please respond with '1' for Yes and '2' for no.\n''')
            if continue_helping == '1':
                need_info = True
                break
            elif continue_helping == '2':
                print('Okay. Goodbye!')
                need_info = False
                break
            else:
                print('Please enter a valid input!')



#won't work without this as there is no import_list instantiated.  If i try to instantiate it in main, it
#of course is unable to do this as there is no Liquor class to instantiate it.  Ask for help on the best practice to organize
#all these functions

from main import import_list