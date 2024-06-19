def difficulty():
    while True:
        try:
            level = int(input("Please enter your level of difficulty (1-3): "))
            if level not in [1, 2, 3]:
                print("ERROR: Please enter a level number between 1 and 3")
            else:
                return level
        except:
            print("ERROR: Please enter a valid number.")
difficulty()

def number_questions():
    while True:
        try:
            number_of_questions = int(input("Please enter your number of questions(3-10): "))
            if number_of_questions not in [3, 4, 5, 6, 7, 8, 9, 10]:
                print("ERROR: Please enter a number of questions between 3 and 10")
            else:
                return number_of_questions
        except:
            print("ERROR: Please enter a valid number.")
number_questions()

def main():
    while True:
        



main()
