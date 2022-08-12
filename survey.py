from questions import Questions


class Survey(object):

    def __init__(self):
        self.count = 0
        self.stressPoint = 0
        self.directive = "Please enter your answer as a number from 1~5.\n1: Not satisfied at all\n2: Not satisfied\n3: Neither\n4: Satisfied\n5: Very satisfied"
        self.questions = Questions().getValue()

    def showResult(self):
        if self.stressPoint >= 45:
            print('No abnormalities at all. You are in good shape!')
        elif self.stressPoint >= 31:
            print(
                'Your stress level is within the appropriate range. Try to maintain this state.')
        elif self.stressPoint >= 16:
            print(
                'You are in a somewhat stressful situation. Pay attention to the daily changes in your mind.')
        else:
            print(
                'You are in a very stressed state. Please take a break or talk to your supervisor now.')

    def takeSurvey(self):
        while self.count < 10:
            self.count += 1
            if self.count == 1:
                print(self.directive)

            question = "Question No." + \
                str(self.count) + " " + self.questions[self.count] + ':'

            try:
                user_input_to_int = int(input(question))

                if user_input_to_int <= 0 or user_input_to_int > 5:
                    raise ValueError
            except ValueError:
                print("Please enter in a number from 1~5.")
                self.count -= 1
                continue

            self.stressPoint = self.stressPoint + user_input_to_int
        return self.showResult()

    def getStressPointValue(self):
        return str(self.stressPoint)
