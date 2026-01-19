class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance +=amount


    def withdraw(self, amount, description=""):
        if amount <=self.balance:
            self.ledger.append({'amount': -1*amount, 'description': description})
            self.balance +=-1*amount
            return True
        else:
            return False
        

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category_type):
        if amount <= self.balance:
            self.withdraw(amount, f'Transfer to {category_type.name}')
            category_type.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    temp_cat = []
    for category in categories:
        category_total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                category_total +=item['amount']
        temp_cat.append(category_total)
    
    total_spent = sum(temp_cat)
    percentages = [(x/total_spent*100) for x in temp_cat]
    print(total_spent)
    print(percentages)

    lines = ""
    for i in range(11):
        lines += str(int(100-10*i)).rjust(3) + "|"      
        for e in percentages:
            if e >= int(100-10*i):
                lines += " o "
            else:
                lines += "   "
        lines +=' \n'
    lines += "    " + "---"*len(percentages)+ "-"+'\n'

    category_names = []
    for c in categories:
        category_names.append(c.name)

    max_length = max(len(name) for name in category_names)

    x_axis = ""
    for i in range(max_length):
        x_axis+="     "
        for name in category_names:
            if i < len(name):
                x_axis +=name[i] + "  "
            else:
                x_axis +="   "
        x_axis +='\n'
    x_axis = x_axis.rstrip('\n')

    return title + lines+x_axis
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))