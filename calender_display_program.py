import calendar 
import time

def display_calendar():
    print("Welcome to my Python Calender.")
    while True:
        try:
            start_time =time.time()
            year =int(input("Enter the year:"))
            month =int(input("Enter the month:"))

            end_time =time.time()
            time_duration =end_time -start_time

            if 1<= month <= 12:
                print("\n" + calendar.month(year ,month))
                print(f"\nThe time duration information is: {time_duration:.2f}second.\n")
            else:
                print("Invalid number,Please Enter the number beteen 1 to 12.")
        except ValueError:
            print("Invalid Syntax,Please enter the numeric number.")

        choice =input("Do you want to check another month? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting The Calender GoodBye!")
            break
        

display_calendar()




