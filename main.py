"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost/SEMESTERS_PER_YEAR
    


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost/MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost)/CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost)/credits

def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER * (credits/CS1430_CREDITS))

def cost_of_skipped_class(annual_cost, credits):
    return cost_per_class(annual_cost, credits)


# ---- PROGRAM ----

def main():

    annual_costs = float(input("How much are you paying per year? "))
    credits = int(input("How many credits are you taking this semester? "))
    while True:
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost of skipped class")
        print("Q. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"${cost_per_semester(annual_costs):.2f} per semester.")
        elif choice == "2":
            print(f"${cost_per_month(annual_costs):.2f} per month.")
        elif choice == "3":
            print(f"${cost_per_day(annual_costs):.2f} per day.")
        elif choice == "4":
            print(f"${cost_per_credit(annual_costs, credits):.2f} per credit.")
        elif choice == "5":
            print(f"${cost_per_class(annual_costs, credits):.2f} every day of class.")
        elif choice == "6":
            skipped_classes = int(input("How many classes have you skipped? "))
            print(f"You lose ${cost_of_skipped_class(annual_costs, credits) * skipped_classes:.2f} by skipping {skipped_classes} classes.")
        elif choice == "Q":
            break
        else:
            print("Not an option, try again.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
