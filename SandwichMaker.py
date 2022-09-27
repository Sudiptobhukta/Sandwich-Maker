import pyinputplus as pyip
import re , time

prices ={'wheat':15, 'whole wheat':20, 'spinach':30 , 'simple':10 , 
"chicken":50, "turkey": 50,"ham":50,"fish":40,
"paneer": 30, "alloo":20 , "beans":25 , "vegetables":20,
 'cheddar':20 ,'swiss': 20 , 'mozzarella':25,
 }

TotalMoney =0 
Order={}

def takeOrder():
    global TotalMoney
    print("wheat : 15 | whole wheat : 20 | spinach : 30 |  simple : 10")
    Order["bread"] = pyip.inputMenu(['wheat' , 'whole wheat' , ' spinach' , ' simple'], "What type of bread you want:\n")
    veg = pyip.inputMenu(["Veg","Non Veg"], "Vegetarian or Non-Vegetarain:\n")
    if veg == "Non Veg":
        print("Chicken:50 | Turkey: 50 | Ham:50| Fish:40")
        Order["Stuff"] = pyip.inputMenu(["chicken","turkey","ham","fish"])
    else:
        print("Paneer: 30 | Alloo:20 | Beans:25 | Vegetables:20")
        Order["Stuff"] = pyip.inputMenu(["paneer", "alloo" , "beans" , "vegetables"])
    
    Cheese = pyip.inputYesNo("Want cheese yes or not: ")
    if Cheese == "yes":
        Order["cheese"] = pyip.inputMenu(['cheddar','swiss', 'mozzarella'], "Type of Cheese: \n")
    
    Sauce = pyip.inputYesNo("Want to add sauce: ")
    if Sauce =='yes':
        Order["sauce"] = pyip.inputMenu(['mayo','mustard', 'lettuce','tomato'] , "Type of Sauce: \n")
    
    print(Order)

    for i in Order.values():
        if i in prices.keys():
            TotalMoney += prices[i]

takeOrder()

respo = pyip.inputYesNo("Do you want to make another sandwich: ")
if respo == "yes":
    more = pyip.inputNum("How many more sandwich: " , greaterThan= 0)
    for i in range(more):
        takeOrder()

time.sleep(1)
print(Order)
print(TotalMoney)
# response = pyip.inputYesNo("Want to make a sandwich Yes or No: ")
# if response == 'yes':
#     print('Takeout')
#     takeOrder()
