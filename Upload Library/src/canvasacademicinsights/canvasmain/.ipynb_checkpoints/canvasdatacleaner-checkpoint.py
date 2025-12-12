from datetime import datetime

dateFormat = "%Y-%m-%dT%H:%M:%SZ"

def cleanData(data):
    cleandata = []
    for courseList in data:
        coursedata = []
        gradeList = []
        for i in range(len(courseList)):
            if i == 0:
                coursedata.append(courseList[0]) #course id
            elif i == 1:
                coursedata.append(courseList[1]) #course name
            elif i == 2:
                coursedata.append(courseList[2]) #course enrollment
            else:
                item = courseList[i]
                name = item[0]
                score = item[1]
                total = item[2]
                date = None
                if item[3] is not None:
                    date = datetime.strptime(item[3], dateFormat)
                if (len(name) < 4 and 'q' in name.lower()) or 'quiz' in name.lower():
                    gradeList.append(QuizGrade(name, score, total, date))
                else:
                    gradeList.append(AssignmentGrade(name, score, total, date))
        coursedata.append(gradeList)
        cleandata.append(coursedata)
    return cleandata
        
        
class Grade():
    def __init__(self, name, score, total, date):
        self.__name = name
        self.__score = score
        self.__total = total
        self.__date = date
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value
    
    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, value):
        self.__total = value
        
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, value):
        self.__date = value
        
    def __str__(self):
        strList = []
        strList.append(self.__name)
        strList.append(self.__score)
        strList.append(self.__total)
        strList.append(self.__date)
        return strList
        
class AssignmentGrade(Grade):
    def isAssignment(self):
        return True
    
    def isQuiz(self):
        return False
    
    def __str__(self):
        strList = []
        strList.append(self.__name)
        strList.append(self.__score)
        strList.append(self.__total)
        strList.append(self.__date)
        strList.append('Assignment')
        return strList
    
class QuizGrade(Grade):
    def isAssignment(self):
        return False
    
    def isQuiz(self):
        return True
    
    def __str__(self):
        strList = []
        strList.append(self.__name)
        strList.append(self.__score)
        strList.append(self.__total)
        strList.append(self.__date)
        strList.append('Quiz')
        return strList