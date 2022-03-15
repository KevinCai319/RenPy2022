init python:

    #name will be course name and is a string
    # numClasses will be the max number of courses
    # for useless classes,
    # num Complete does not impact whether you finish generator or not.

    class Course:
        course_listing = []
        def __init__(self, name,label, numClasses, numRequiredComplete, unlocked,extra = "looks like an interesting course..."):
            self.name = name
            self.label = label
            self.numClasses = numClasses
            self.numRequiredComplete = numRequiredComplete
            self.unlocked = unlocked
            self.currentClass = 1
            self.extra = extra
            self.complete = False
            Course.course_listing.append(self)

        def progressClass(self):
            if (unlocked):
                if(currentClass < numClasses):
                    self.currentClass += 1
                if(currentClass >= numRequiredComplete):
                    self.complete = True;
