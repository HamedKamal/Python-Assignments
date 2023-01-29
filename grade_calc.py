class Student:
    studetsDict = {}
    studetGrade = {}
    def __init__(self, name, ids):
        self.name = name
        self.id = ids
    def setGrade(self, mathGrade, englishGrade, arabicGrade):
        self.mathGrade = mathGrade
        self.englishGrade = englishGrade
        self.arabicGrade = arabicGrade
    def gradeCalculatue(self):
        if self.mathGrade>=90:
            Student.studetGrade.update({'Math grade':'A'})
        elif self.mathGrade>=70:
            Student.studetGrade.update({'Math grade':'B'})
        elif self.mathGrade>=50:
            Student.studetGrade.update({'Math grade':'C'})
        else:
            Student.studetGrade.update({'Math grade':'F'})    

        if self.englishGrade>90:
            Student.studetGrade.update({'English grade':'A'})
        elif self.englishGrade>=70:
            Student.studetGrade.update({'English grade':'B'})
        elif self.englishGrade>=50:
            Student.studetGrade.update({'English grade':'C'})
        else:
            Student.studetGrade.update({'English grade':'F'})
            
        if self.arabicGrade>=90:
            Student.studetGrade.update({'Arabic grade':'A'})
        elif self.arabicGrade>=70:
            Student.studetGrade.update({'Arabic grade':'B'})
        elif self.arabicGrade>=50:
            Student.studetGrade.update({'Arabic grade':'C'})
        else:
            Student.studetGrade.update({'Arabic grade':'F'})
        print(Student.studetGrade)
one = Student(name=input('enter your name : '),
            ids=input('enter your id : '))

one.setGrade(
    mathGrade=float(input('enter your math grade : ')),
    englishGrade=float(input('enter your english grade : ')),
    arabicGrade=float(input('enter your  arabic grade : '))
)
one.gradeCalculatue()
