import time
menu_card={
    "Espresso":{
        "Coffee":18,
        "Water":50,
        "Price":1.50
    },
    "Latte":{
        "Coffee":24,
        "Water":200,
        "Milk":150,
        "Price":2.50
    },
    "Cappacino":
        {
            "Coffee":24,
            "Water":250,
            "Milk":100,
            "Price":3
        }
}
coffee_machine_resources={
    "Water":300,
    "Milk":200,
    "Coffee":100  
}

your_wallet=float(input("How much money do you have in your wallet?"))

while True:
    your_choice=int(input("\nWhich type of coffee do you want to order,\nIf you want to order Espresso Coffee then enter the 1\nIf you want to order Latte Coffee then enter the 2\nIf you want to order Cappacino Coffee then enter the 3\nIf you want to see the resource report then enter the 4\nIf you want to see the how much money left in your wallet then enter the 5\nIf you want to exit from the coffee machine then enter the 6\nEnter the your choice?"))

    if your_choice==1:        
        if your_wallet<menu_card["Espresso"]['Price']:
            print("\nSorry! you don't have sufficient money for buying the coffee!")
        
        elif coffee_machine_resources["Coffee"]<menu_card["Espresso"]['Coffee'] or coffee_machine_resources["Water"]<menu_card["Espresso"]["Water"]:
            print("\nSorry! i don't have sufficient ingredients for making the coffee!")
            
        # elif coffee_machine_resources["Coffee"]<menu_card["Espresso"]['Coffee'] and coffee_machine_resources["Water"]<menu_card["Espresso"]["Water"] and your_wallet<menu_card['Espresso']['Price']:
        #     print("\nSorry! i don't have sufficient ingredients for making the coffee and you don't have sufficient money also!")
        
        # if coffee_machine_resources["Coffee"]>menu_card["Espresso"]['Coffee'] and coffee_machine_resources["Water"]>menu_card["Espresso"]["Water"] and your_wallet>menu_card["Espresso"]['Price']:
        else:
            print("\nCofee making...")
            time.sleep(3)
            print("Cofee almost ready...")
            time.sleep(2)
            print("Here, is your coffee, enjoy it!")
            your_wallet=your_wallet-menu_card["Espresso"]['Price']
            coffee_machine_resources["Coffee"]=coffee_machine_resources["Coffee"]-menu_card['Espresso']['Coffee']
            coffee_machine_resources["Water"]=coffee_machine_resources["Water"]-menu_card['Espresso']['Water']
            
    elif your_choice==2:
            
        if your_wallet<menu_card["Latte"]['Price']:
            print("\nSorry! you don't have sufficient money for buying the coffee!")
        
        elif coffee_machine_resources["Coffee"]<menu_card["Latte"]['Coffee'] or coffee_machine_resources["Water"]<menu_card["Latte"]["Water"] or coffee_machine_resources["Milk"]<menu_card["Latte"]["Milk"]:
            print("\nSorry! i don't have sufficient ingredients for making the coffee!")
        
        # elif coffee_machine_resources["Coffee"]<menu_card["Latte"]['Coffee'] and coffee_machine_resources["Water"]<menu_card["Latte"]["Water"] and coffee_machine_resources["Milk"]<menu_card["Latte"]["Milk"] and your_wallet<menu_card["Latte"]['Price']:
        #     print("\nSorry! i don't have sufficient ingredients for making the coffee and you don't have sufficient money also!")
        
        # if coffee_machine_resources["Coffee"]>menu_card["Espresso"]['Coffee'] and coffee_machine_resources["Water"]>menu_card["Espresso"]["Water"] and your_wallet>menu_card["Espresso"]['Price']:
        else:
            print("\nCofee making...")
            time.sleep(3)
            print("Cofee almost ready...")
            time.sleep(2)
            print("\nHere, is your coffee, enjoy it!")
            your_wallet=your_wallet-menu_card["Latte"]['Price']
            coffee_machine_resources["Coffee"]=coffee_machine_resources["Coffee"]-menu_card['Latte']['Coffee']
            coffee_machine_resources["Water"]=coffee_machine_resources["Water"]-menu_card['Latte']['Water']
            coffee_machine_resources["Milk"]=coffee_machine_resources["Milk"]-menu_card['Latte']['Milk']

    elif your_choice==3:
        if your_wallet<menu_card["Cappacino"]['Price']:
            print("\nSorry! you don't have sufficient money for buying the coffee!")
        
        elif coffee_machine_resources["Coffee"]<menu_card["Cappacino"]['Coffee'] or coffee_machine_resources["Water"]<menu_card["Cappacino"]["Water"] or coffee_machine_resources["Milk"]<menu_card["Cappacino"]["Milk"]:
            print("\nSorry! i don't have sufficient ingredients for making coffee!")
        
        # elif coffee_machine_resources["Coffee"]<menu_card["Cappacino"]['Coffee'] and coffee_machine_resources["Water"]<menu_card["Cappacino"]["Water"] and coffee_machine_resources["Milk"]<menu_card["Cappacino"]["Milk"] and your_wallet<menu_card["Cappacino"]['Price']:
        #     print("\nSorry! i don't have sufficient ingredients for making the coffee and you don't have sufficient money also!")
            
        # if coffee_machine_resources["Coffee"]>menu_card["Espresso"]['Coffee'] and coffee_machine_resources["Water"]>menu_card["Espresso"]["Water"] and your_wallet>menu_card["Espresso"]['Price']:
        else:
            print("\nCofee making...")
            time.sleep(3)
            print("Cofee almost ready...")
            time.sleep(2)
            print("Here, is your coffee, enjoy it!")
            your_wallet=your_wallet-menu_card["Cappacino"]['Price']
            coffee_machine_resources["Coffee"]=coffee_machine_resources["Coffee"]-menu_card['Cappacino']['Coffee']
            coffee_machine_resources["Water"]=coffee_machine_resources["Water"]-menu_card['Cappacino']['Water']
            coffee_machine_resources["Milk"]=coffee_machine_resources["Milk"]-menu_card['Cappacino']['Milk']
            
    elif your_choice==4:
        print(f"\nThe left resources is {coffee_machine_resources.items()}")

    elif your_choice==5:
        print(f"\nThe left money in your wallet is {your_wallet}")

    elif your_choice==6:
        print("\nThank you for visiting our cafe, visit again!")
        time.sleep(2)
        print(exit(0))

    else:
        print("\nSorry! you entered the wrong choice!")