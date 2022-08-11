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

            self.stressPoint = self.stressPoint + int(input(question))
        return self.showResult()

    def __str__(self):
        """Returns a string representation of the last roll."""
        return "Your stress point is" + str(self.stressPoint)
