
def info ():
    print("To play this game, you will need to know some things.")
    input()
    print("1. Every time you see a blank press the 'Enter' key")
    input()
    print("2. To leave the game you have to type 'stopgame'")
    input()
    print("3. When you start the game the text will have obvious things, people, or places that you can go to. To go to them, type them in in all caps.")


info()

input("The knight's of Balore! (press enter)")
print("Once upon a time, there was a place called Balore.")
input()
print("There was a king. And the king had his 7 knights, to protect the kingdom.")
input()
print("Their names were, Black, Red, Blue, Yellow, Green, Purple, and White")
input()
print("The king also had a royal advisor. His name was Rafiel. He was EVIL.")
input()
print("Then, there was you. You loved the knights, and wanted to be one of them.")
input()
print("You knew about Rafiel's evil plans and wanted to stop them.")
input()
print("So you went on a quest. And here you are, starting now. (game starts)")
input()
begin = input("Right now there is a PEASENT, SIGN, and a SHOP")

#variables
title = "RPG"
empty = "..."
coins = 0
lv = 1
health_potion_num = 0
health_price = 10
heatlh_cata_num = 2
sword_num = 0
sword_price = 25
sword_cata_num = 1



while (lv == 1):
 begin = input("Right now there is a PEASENT, SIGN, and a SHOP")
 if (begin == "PEASENT"):
     print("Hi! I'm Joe! Can you do a job for me? I will give you ten coins if you do.")
     job1 = input ("Type yes for yes and no for no")
     if (job1 == "yes"):
         q1 = input("Great! What is 7 x 20?")
         if (q1 == "140"):
             print("Good job!")
             coins = 10
             print("Now you have" , coins, "coins")
         else: print ("No, your wrong!")
     else: print ("Oh, okay...")
 elif (begin == "SHOP"):
    print("You have", coins, "coins. Type in BUY to see what you can buy.")
    shop = input()
    if (shop == "BUY"):
        print("Catalog number: 1 Sword: you have", sword_num, ". The price for 1 Sword is", sword_price)
        print("Catalog number: 2 Heatlh potion: you have", health_potion_num, ". The price for 1 Heatlh potion is", health_price)
        print("What would you like to buy? You currently have", coins, "coins. (enter catalog number)")
        buy_item = input()
        if (buy_item == "1" and coins > sword_price or coins == sword_price):
            sword_num += 1
            coins -= sword_price
            print("You just bought the Sword! Now you have", coins, "coins")
        elif (buy_item == "2" and coins > health_price or coins == health_price):
            health_potion_num += 1
            coins -= health_price
            print("You just bought the Heatlh potion! Now you have", coins, "coins")
        else: print("You dont have enough coins")
    elif (begin == "SIGN"):
        print("To go to the next level, you have to buy a health potion.")
     
   
         





         
