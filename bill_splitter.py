print("=== WELCOME TO THE SMART BILL SPLITTER ===")

try:
    # 1. Take inputs from the user
    total_bill = float(input("Enter the total food bill amount (₹): "))
    tip_percentage = int(input("Enter tip percentage you want to give (e.g., 5, 10, 15): "))
    number_of_people = int(input("How many people are splitting the bill? "))

    # 2. Perform the logic calculations
    tip_amount = total_bill * (tip_percentage / 100)
    grand_total = total_bill + tip_amount
    share_per_person = grand_total / number_of_people

    # 3. Display the final broken-down results
    print("\n--- BILL BREAKDOWN ---")
    print(f"Original Food Bill : ₹{total_bill:.2f}")
    print(f"Tip Added ({tip_percentage}%): ₹{tip_amount:.2f}")
    print(f"Grand Total Amount : ₹{grand_total:.2f}")
    print(f"Each Person Pays   : ₹{share_per_person:.2f}")
    print("----------------------")

except ValueError:
    print("Error: Please enter valid numbers only!")
