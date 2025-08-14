# Payment Management System
# Author: Parwaz

# Store all customers and their payments
customers = {}

def add_customer():
    name = input("Enter customer name: ")
    if name in customers:
        print("Customer already exists!")
    else:
        customers[name] = []
        print(f"Customer '{name}' added successfully.")

def record_payment():
    name = input("Enter customer name: ")
    if name not in customers:
        print("Customer not found! Please add customer first.")
        return
    amount = float(input("Enter payment amount: ₹"))
    customers[name].append(amount)
    print(f"Payment of ₹{amount} recorded for {name}.")

def view_customers():
    if not customers:
        print("No customers found.")
        return
    for name, payments in customers.items():
        total = sum(payments)
        print(f"{name} → Payments: {payments} | Total Paid: ₹{total}")

def save_data():
    with open("payments.txt", "w") as file:
        for name, payments in customers.items():
            file.write(f"{name}:{payments}\n")
    print("Data saved to payments.txt")

def load_data():
    try:
        with open("payments.txt", "r") as file:
            for line in file:
                name, payments_str = line.strip().split(":")
                payments = eval(payments_str)
                customers[name] = payments
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

# Main menu loop
def main():
    load_data()
    while True:
        print("\n--- Payment Management System ---")
        print("1. Add Customer")
        print("2. Record Payment")
        print("3. View All Customers")
        print("4. Save & Exit")

        choice = input("Enter choice (1-4): ")
        
        if choice == "1":
            add_customer()
        elif choice == "2":
            record_payment()
        elif choice == "3":
            view_customers()
        elif choice == "4":
            save_data()
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()

