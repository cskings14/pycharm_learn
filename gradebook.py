class Gradebook:
    def __init__(self, grades = []):
        self.grades = grades
        self.count = 0


    @property
    def get_grades(self):
        return self.grades

    def add(self, grade):
        self.grade = grade
        self.grades.append(grade)
        self.count += grade

    def getMean(self):
        return self.count / len(self.grades)

    def getMedian(self):
        self.grades.sort()
        middlenum = 0
        if len(self.grades) % 2 != 0:
            middlenum = len(self.grades) // 2
            return self.grades[middlenum]
        else:
            middle1 = len(self.grades) // 2
            middle2 = len(self.grades) // 2 - 1
            middle = (self.grades[middle1] + self.grades[middle2]) / 2
            return middle

    def getMode(self):

        fval = 0
        ipos = 0
        for i in range(0, len(self.grades)):
            counter = 1
            for j in range(i+1, len(self.grades)):
                if self.grades[i] == self.grades[j]:
                    counter += 1
            if counter > fval:
                fval = counter
                ipos = i
        return self.grades[ipos]




        # mode return the most frequently added grade






GBook = Gradebook()
GBook.add(53)
GBook.add(68)
GBook.add(89)
GBook.add(68)
GBook.add(53)
GBook.add(68)

print(GBook.getMean())

print(GBook.getMedian())

print(GBook.getMode())























