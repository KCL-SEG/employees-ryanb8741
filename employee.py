"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlyPay, commission = None):
        self.name = name
        self.commission = commission
        self.monthlyPay = monthlyPay

    def get_pay(self):
        total = 0

        if self.commission != None:
            if self.commission[0] == "bonus":
                total = total + self.commission[1]
            else:
                total = total + (self.commission[1] * self.commission[2])
        
        if self.monthlyPay[0] == "salary":
            total = total + self.monthlyPay[1]
        else:
            total = total + (self.monthlyPay[1] * self.monthlyPay[2])
            
        return total
    
    def printMonthly(self):
        if self.monthlyPay[0] == "salary":
            return f"monthly salary of {self.monthlyPay[1]}"
        else:
            return f"contract of {self.monthlyPay[1]} hours at {self.monthlyPay[2]}/hour"

    def printCommission(self):
        build = None
        if self.commission != None:
            if self.commission[0] == "bonus":
                build = f"bonus commission of {self.commission[1]}"
            else:
                build = f"commission for {self.commission[1]} contract(s) at {self.commission[2]}/contract"
                
        return " and receives a " + build if build != None else ""
    
    def __str__(self):
        return f"{self.name} works on a {self.printMonthly()}{self.printCommission()}. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', ("salary", 4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', ("contract", 100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ("salary", 3000), ("contract", 4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ("contract", 150, 25), ("contract", 3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', ("salary", 2000), ("bonus", 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', ("contract", 120, 30), ("bonus", 600))
