import datetime
from colorama import Fore, Back

with open("main.txt","r") as file:
    data=file.read()


date=datetime.date.today()
run=True

while run:
    print(Fore.BLACK+Back.WHITE+"Choose what do you want")
    fir=input("1-Add balance, 2-Clear balance, 3-See balance, 4-Quit:")

    if fir=="1":
        sec=int(input("Enter quantity:"))
        thir=input("Enter currency(USD, UAH, RUB, EUR):").upper()
        four="Your balance:", str(sec), thir, str(date)
        last=""
        for i in four:
            last+=i
        else:
            print(last)
        with open("main.txt","a") as file:
            file.write("||"+last)

    elif fir == "2":
        with open("main.txt", "w") as file:
            pass

    elif fir == "3":
        with open("main.txt", "r") as file:
            data = file.read()
            print(data)

    elif fir=="4":
        run=False