import datetime,json 

class NewCustomer():
    
    def customer(self):
        name = input("Enter your name: ").capitalize()
        file_name = f"{name}.txt"
        pin = int(input("Create a new pin: "))
        person = {}
        person["name"]  = name
        person["PIN"] = pin
        person["total_amount"] = 0
        person["transactions"] = []
        person = json.dumps(person)
        with open(file_name, "w")as file:
            file.write(person)
        return name

        

class BankingActivity():
    def __init__(self, name):
        self.name = name
        date = datetime.datetime.now()
        day = date.strftime("%d")
        month = date.strftime("%B")
        year = date.strftime("%Y")
        hour = date.strftime("%I")
        min = date.strftime("%M")
        sec  = date.strftime("%S")
        am_pm = date .strftime("%p")
        self.date = f"{day} {month} {year} {hour}:{min}:{sec} {am_pm}"
    def deposit(self,total_amount):
        file_name = f"{self.name}.txt"
        amount_deposited = int(input("Enter the Amount you need to deposit : "))
        total_amount = total_amount + amount_deposited
        transaction =f"{self.name} sir, You deposited {amount_deposited} amount of money and the balance is {total_amount} on {self.date}"

        file = open(file_name, "r")
        person = file.read() 
        person = json.loads(person)
        person["total_amount"] = total_amount
        person["transactions"].append(transaction)
        person = json.dumps(person)
        file.close()
        with open (file_name,"w") as file:
            file.write(person)
        return total_amount
    def withdraw(self, total_amount):
        file_name = f"{self.name}.txt"
        amount_withdrawn = int(input("Enter the Amount you need to withdraw : "))
        total_amount = total_amount - amount_withdrawn
        transaction =f"{self.name} sir, You deposited {amount_withdrawn} amount of money and the balance is {total_amount} on {self.date}"
        with open (file_name, "r")as file:
            data = file.read() 
            person = json.loads(data)
            person["total_amount"] = total_amount
            person["total_amount"] = total_amount
            person["transactions"].append(transaction)
            person = json.dumps(person)
            file.close()
            with open (file_name,"w") as file:
                file.write(person)
        return total_amount
    def balance(self, total_amount):
        file_name = f"{self.name}.txt"
        print(f"{self.name} sir, your balance is {total_amount}")
        with open (file_name, "r")as file:
            data = file.read() 
            person = json.loads(data)
            person["total_amount"] = total_amount
            json.dumps(person)

    def transaction_read(self):
        file_name = f"{self.name}.txt"
        with open(file_name, "r") as file:
            if file.readline() == "":
                print("No history")
        with open(file_name, "r") as file:
            data = file.read() 
            person = json.loads(data)
            transactions = person["transactions"]
            for line in transactions:
                print(line)

    def y_or_n(self):
        while True:
                    y_or_n = input("Sir, you need to continue the service (Y/N) : ").upper()
                    if y_or_n == "N":
                        print("Thank you, sir")
                        with open ("Transactions.txt","w")as file:
                            file.write("")
                        option = False
                        break
                    elif y_or_n == "Y":
                        option = True
                        break
                    else:
                        print("I didn't understand sir")
        return option
class MainAction():
    def __init__(self,name):
        
        file_name = f"{name}.txt"
        with open(file_name,"r")as file:
            person = file.read()
            person = json.loads(person)
            self.name = person["name"]
            self.pin = person["PIN"]
            self.total_amount = person["total_amount"]
            
    def main(self):
        name = self.name
        act_pin = self.pin
        total_amount =self.total_amount
        print(f"Welcome {name}")
        pin_loop = True
        while pin_loop == True:
            pin = int(input("Enter your pin : "))
            if pin == act_pin:
                pin_loop = False
                print("How may i help you")
                option = True
                while option == True:
                    option = int(input("Enter 1 to deposit, 2 to withdraw, 3 to show the balance amount and 4 to show transaction history : "))
                    match option:
                        case 1:
                            option = False
                            banking_activity = BankingActivity(name)
                            total_amount = banking_activity.deposit(total_amount)
                            banking_activity.balance(total_amount)
                            option = banking_activity.y_or_n()
                        case 2:
                            banking_activity = BankingActivity(name)
                            total_amount= banking_activity.withdraw(total_amount)  
                            banking_activity.balance(total_amount)
                            option = banking_activity.y_or_n()
                        case 3:
                            banking_activity = BankingActivity(name)
                            banking_activity.balance(total_amount)
                            option = banking_activity.y_or_n()
                        case 4:
                            banking_activity = BankingActivity(name)
                            banking_activity.transaction_read()
                            option = banking_activity.y_or_n()
                        case _:
                            option = True
                            print("You choose the wrong option, Try again")
            else:
                print("Incorrect pin, Try again")




#-------------------------------------------------
        
print("Welcome to bank of Basil")
customer = input("Are you a new customer? (Y/N) :").upper()
if customer == "Y":
    customer = NewCustomer()
    name = customer.customer()
    main = MainAction(name)
    main.main()
else:
    name = input("May i know your name : ")
    main = MainAction(name)
    main.main()
    