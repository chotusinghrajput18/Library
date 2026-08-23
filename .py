class Library:
    # Dictionary for categories
    book = {
        "Story": ["The Jungle Book", "Mogli", "Chota Bheem"],
        "Coding": ["C", "Python", "Html", "Java", "JavaScript"],
        "Computer": ["MS Excel", "MS Powerpoint", "MS Word"]
    }

    # Dictionary for price
    price = {
        "The Jungle Book": 349,
        "Mogli": 249,
        "Chota Bheem": 299,
        "C": 399,
        "Python": 499,
        "Html": 449,
        "Java": 549,
        "JavaScript": 499,
        "MS Excel": 549,
        "MS Powerpoint": 399,
        "MS Word": 499
    }

    # Initialization
    def __init__(self):
        self.cart = []
        print("You are Logged In")
        self.show_categories()

    # Bill method
    def bill(self):
        total = 0

        for item in self.cart:
            if item in self.price:
                total += self.price[item]

        print("Your Total Bill is:", total)

    # Method for individual items
    def show_individual(self, category):
        print("\nAvailable Books:")
        
        for i, item in enumerate(self.book[category], 1):
            print(i, item)

        opt = input("Choose a book to add or Q for back: ").strip()

        if opt.lower() == "q":
            return

        try:
            choice = int(opt)

            if 1 <= choice <= len(self.book[category]):
                selected_book = self.book[category][choice - 1]
                self.cart.append(selected_book)
                print(f"{selected_book} added to cart.")

            else:
                print("Invalid Choice")

        except ValueError:
            print("Please enter a valid number.")

    # Method for categories
    def show_categories(self):
        while True:
            print("\n----- Welcome to Library -----")

            categories = list(self.book.keys())

            for i, category in enumerate(categories, 1):
                print(i, category)

            print("B. Bill")
            print("Q. Exit")

            ch = input("Choose the Category: ").strip()

            if ch.lower() == "b":
                self.bill()

            elif ch.lower() == "q":
                print("Thank you for visiting the Library!")
                break

            else:
                try:
                    choice = int(ch)

                    if 1 <= choice <= len(categories):
                        category = categories[choice - 1]
                        self.show_individual(category)

                    else:
                        print("Invalid Choice")

                except ValueError:
                    print("Please enter a valid option.")


# Object calling
l1 = Library()