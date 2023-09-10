# Ontario Alcohol Duty Calculator
A calculator to find how much you will have to pay in duties and taxes for importing Ontario Liquor.  
This project was made when abroad in Europe, and not having an easy way to figure out how much I would 
have to pay for importing alcohol into Canada.  The best reference available was sourced from LCBO:
https://www.lcbo.com/content/lcbo/en/corporate-pages/about/aboutourbusiness/importing.html

After seeing the various prices needed to pay, I figured to make a function that can create liquor objects.  
With this function, you input the size of the bottle you are importing, the alcohol%, and retail price that you paid converted into Canadian dollars.  Simply instantiate an object in the 'alcohol_list.py' file
with the format provided.  In the 'main.py' file, add your alcohol of interest into 'import_list', and run the function!

Future updates will include changing the liquor class objects to be instantiated as a dictionary rather than a list with specific values at specific positions.  
