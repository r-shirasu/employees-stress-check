from survey import Survey


def do():

    employer = Survey()
    employer.takeSurvey()


# def logStats():
    # 実装中


def main():
    # Play one game
    print("Welcome to employee survey.")
    do()
    number = 0

    while number <= 0 or number > 5:
        user_input = input("How many games would you want to have tested: ")

        # Check if a valid number is entered
        try:
            number = int(user_input)

            # check if the number entered is > 0
            if number <= 0:
                print("Please enter in a positive number.")
                number = 0
            elif number > 5:
                print("Please enter number less than five.")
                number = 0
        except ValueError:
            print("Please enter in a number from 1~5.")


if __name__ == "__main__":
    main()
