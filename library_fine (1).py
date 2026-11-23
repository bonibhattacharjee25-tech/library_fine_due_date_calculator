from datetime import date, timedelta

LOAN_PERIODS = {"student": 14, "faculty": 30}
FINE_PER_DAY = 2
MAX_FINE = 200
GRACE_DAYS = 0


def calculate_due_date(issue_date, member_type):
    loan_days = LOAN_PERIODS[member_type]
    return issue_date + timedelta(days=loan_days)


def calculate_fine(due_date, return_date):
    late_days = (return_date - due_date).days - GRACE_DAYS
    if late_days <= 0:
        return 0, 0
    fine = min(late_days * FINE_PER_DAY, MAX_FINE)
    return late_days, fine


def parse_date(text):
    year, month, day = map(int, text.strip().split("-"))
    return date(year, month, day)


def due_date_option():
    issue = parse_date(input("Enter issue date (YYYY-MM-DD): "))
    member_type = input("Enter member type (student/faculty): ").strip().lower()

    if member_type not in LOAN_PERIODS:
        print("Error: Member type must be 'student' or 'faculty'.")
        return

    due = calculate_due_date(issue, member_type)
    print(f"Book must be returned by: {due.strftime('%d %B %Y')}")


def fine_option():
    due = parse_date(input("Enter due date (YYYY-MM-DD): "))
    returned = parse_date(input("Enter return date (YYYY-MM-DD): "))

    late_days, fine = calculate_fine(due, returned)
    if late_days == 0:
        print("Book returned on time. No fine.")
    else:
        print(f"Book is late by {late_days} day(s).")
        print(f"Fine payable: Rs. {fine}")


def main():
    print("=== Library Fine and Due Date Calculator ===")
    while True:
        print("\n1. Calculate due date")
        print("2. Calculate fine")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                due_date_option()
            elif choice == "2":
                fine_option()
            elif choice == "3":
                print("Thank you. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2 or 3.")
        except ValueError:
            print("Error: Invalid date. Use the format YYYY-MM-DD (e.g. 2026-11-20).")


if __name__ == "__main__":
    main()
