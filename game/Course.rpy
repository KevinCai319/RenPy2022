init python:

    #name will be course name and is a string
    # numClasses will be the max number of courses
    # for useless classes,
    # num Complete does not impact whether you finish generator or not.

    class Course:
        def __init__(self, name, numClasses, numRequiredComplete, unlocked):
            self.name = name
            self.numClasses = numClasses
            self.numRequiredComplete = numRequiredComplete
            self.unlocked = unlocked
            self.currentClass = 1
            self.complete = False;

        def progressClass(self):
            if (unlocked)
                if(currentClass < numClasses)
                    self.currentClass += 1
                if(currentClass == numRequiredComplete)
                    self.complete = True;
