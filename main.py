class Library:
    cart=[]
    book={
        "Story":["The Jungle Book","Mogli","Chota Bheem"],
        "Coding":["C","Python","Html","Java","JavaScript"],
        "Computer":["MS Excel","MS Powerpoint","MS Word"]
    }
    price={
        "The Jungle Book":349,
        "Mogli":249,
        "Chota Bheem":299,
        "C":399,
        "Python":499,
        "Html":449,
        "Java":549,
        "JavaScript":499,
        "MS Excel":549,
        "MS Powerpoint":399,
        "MS Word":499
    }
    def __init__(self):
        print("You are LogedIn")
        self.show_categories()
    def bill(self):
        total=[]
        for category in self.book:
            for item in self.cart:
                if item in self.book[category] and item in self.price:
                    total.append(self.price[item])
        print("Your Total Bill is:",sum(total))
        
        
    def show_individual(self,individual):
        print(list(self.book[individual]))
        opt=str(input("choose an option to add or q/Q for back:").title())
        if opt in self.book[individual]:
            self.cart.append(opt)
        elif opt in "qQ":
            self.show_categories()
        else:
            print("Invalid Choice")


    def show_categories(self):
        print("-----Welcome to Library-----")
        print(list(self.book.keys()))
        ch=str(input("Chose the Category or b/B for Bill: ").title())
        if ch in "bB":
            self.bill()
        else: 
            for ch in list(self.book.keys()):
                self.show_individual(ch)

l1=Library()
