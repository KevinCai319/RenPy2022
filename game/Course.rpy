init python:

    #name will be course name and is a string
    # numClasses will be the max number of courses
    # for useless classes,
    # num Complete does not impact whether you finish generator or not.

    class Course:
        course_listing = []
        def __init__(self, name, label,numRequiredComplete, lectureContent, unlocked,extra = "looks like an interesting course..."):
            self.name = name
            self.label = label
            self.numClasses = len(lectureContent)
            self.numRequiredComplete = numRequiredComplete
            self.lectureContent = lectureContent
            assert numRequiredComplete <= numClasses, "Number of classes for completion is more than number of total classes"
            self.unlocked = unlocked
            self.currentClass = 1
            self.extra = extra
            self.complete = False
            Course.course_listing.append(self)

        def progressClass(self):
            if (self.unlocked):
                if(self.currentClass < self.numClasses):
                    self.currentClass += 1
                if(self.currentClass >= self.numRequiredComplete):
                    self.complete = True;
