import math as m
import random as r
import platform as p


def student_result():
    print("\n===== Student Result =====")
    name = input("Enter your Name: ")
    roll_no = input("Enter your Roll Number: ")
    try:
        math_marks = float(input("Enter Math marks: "))
        physics = float(input("Enter Physics marks: "))
        computer = float(input("Enter Computer marks: "))
        english = float(input("Enter English marks: "))
        Urdu = float(input("Enter Urdu marks: "))
        Chemistry = float(input("Enter Chemistry marks: "))
        Biology = float(input("Enter Biology marks: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
        return

    subjects = [math_marks, physics, computer, english, Urdu, Chemistry, Biology]

    # Basic validation: marks should be between 0 and 100
    if any(mark < 0 or mark > 100 for mark in subjects):
        print("Invalid marks entered. Marks must be between 0 and 100.\n")
        return

    total = sum(subjects)
    percentage = (total / 700) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "Pass"
    else:
        grade = "Fail"

    print("\n===== Student Result =====")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_no}")
    print(f"Total Marks: {total}/400")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

    save = input("\nSave this result to a file? (y/n): ").strip().lower()
    if save == "y":
        with open("results.txt", "a") as f:
            f.write(f"Name: {name}, Roll No: {roll_no}, Total: {total}, "
                     f"Percentage: {percentage:.2f}%, Grade: {grade}\n")
        print("Result saved to results.txt")


def student_id():
    print("\n===== Student ID Generator =====")
    name = input("Enter your name: ")
    new_id = r.randint(1000, 9999)
    print(f"Name : {name}")
    print(f"Student ID : {new_id}")


def random_motivation():
    print("\n===== Random Motivation =====")
    motivations = [
        "Believe in yourself!",
        "You can do it!",
        "Never give up!",
        "Stay positive!",
        "Keep pushing forward!"
    ]
    print(f"Motivation: {r.choice(motivations)}")


def platform_info():
    print("\n===== Platform Information =====")
    print(f"System : {p.system()}")
    print(f"OS Version : {p.version()}")
    print(f"Platform : {p.platform()}")
    print(f"Processor : {p.processor()}")


def math_tools():
    while True:
        print("\n===== Math Tools =====")
        print("1. Square root\n2. Power\n3. Factorial\n4. Ceiling\n5. Floor\n6. Back")
        choice = input("Enter the tool you want to use: ")

        try:
            if choice == "1":
                num = float(input("Enter a number to find its square root: "))
                if num < 0:
                    print("Cannot find square root of a negative number.")
                else:
                    print(f"The square root of {num} is: {m.sqrt(num)}")
            elif choice == "2":
                num = float(input("Enter a number: "))
                power = float(input("Enter the power: "))
                print(f"{num} raised to the power {power} is: {m.pow(num, power)}")
            elif choice == "3":
                num = int(input("Enter a number to find its factorial: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"The factorial of {num} is: {m.factorial(num)}")
            elif choice == "4":
                num = float(input("Enter a number to find its ceiling value: "))
                print(f"The ceiling value of {num} is: {m.ceil(num)}")
            elif choice == "5":
                num = float(input("Enter a number to find its floor value: "))
                print(f"The floor value of {num} is: {m.floor(num)}")
            elif choice == "6":
                print("Going back to the main menu...")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def main():
    while True:
        print("\n===== Student Utility System =====")
        print("1. Student Result\n2. Student ID\n3. Random Motivation\n"
              "4. Platform Information\n5. Math Tools\n6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_result()
        elif choice == "2":
            student_id()
        elif choice == "3":
            random_motivation()
        elif choice == "4":
            platform_info()
        elif choice == "5":
            math_tools()
        elif choice == "6":
            print("Exiting the program... Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
