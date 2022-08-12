from survey import Survey

from datetime import datetime

employer = Survey()


def do():
    employer.takeSurvey()


def logStatus(userName):
    file = open("log.txt", "a")

    # Create a date/time object to get the current date and time
    now = datetime.now()
    # Formatting the output of the date and time to dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("\n\ndate and time = " + dt_string)
    # Writing the statistics to a file

    stressPoint = employer.getStressPointValue()

    file.write("\n" + userName + ":" + stressPoint)


def main():
    # Play one game
    userName = input("Welcome to employee survey.\nWhat is your name?:")
    do()
    logStatus(userName)


if __name__ == "__main__":
    main()
