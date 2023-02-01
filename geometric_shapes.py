import math


class shape:
    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def setNofSides(self, number):
        self.__nsides = number

    def getNofSides(self):
        return self.__nsides

    def area(self):
        pass

    def premiter(self):
        pass


class rectangle(shape):
    def area(self):
        print(f"your rectangle area is : {self.lenth*self.width}")

    def premiter(self):
        print(f"the premiter is {2*(self.lenth+self.width)}")


class NonRegTriangle(shape):
    def area(self):
        print(f"your triangle area is :  {self.lenth*self.width*0.5}")
        print('if you want premiter "ﻢﻬﻌﻤﺟﺍ"')


class Regular(shape):
    def premiter(self):
        print(f"the premiter is {self.getNofSides()*self.lenth}")

    def area(self):
        print(
            f"the area is {(self.getNofSides()*self.lenth**2)/(4*(math.tan((180/self.getNofSides())*math.pi/180)))}")

class Circle:
    def __init__(self,Xcenter,Ycenter,raduis) :
        self.x=Xcenter,
        self.y=Ycenter,
        self.r=raduis,
        
    def standardForm(self):
        newX=-1*self.x
        newY=-1*self.y
        
        # if x and y are positve
        if newX > 0 and newY > 0:
            return f"(x + {newX})²+(y + {newY})²= {self.r **2}"
        # if x negative and y positve
        elif newX <0 and newY >0:
            return f"(x  {newX})²+(y + {newY})²= {self.r **2}"
        # if x positive and y negative
        elif newX >0 and newY <0:
            return f"(x+ {newX})²+(y  {newY})²= {self.r **2}"
        # if x  and y are  negative
        elif newX >0 and newY <0:
            return f"(x {newX})²+(y  {newY})²= {self.r **2}"


xCenter=float(input('enter the x of centr '))
yCenter=float(input('enter the y of centr '))
raduis=float(input('enter the y of centr '))
mycircle=Circle(Xcenter=xCenter,Ycenter=yCenter,raduis=raduis)
print(mycircle.standardForm())
# polygonOrNot = input('Is it a regular polygon ? (y/n)  : ')
# if polygonOrNot == 'y':
#     user_side_number = int(input('enter the number of sides  : '))
#     user_side_lenth = int(input('enter the lenth of side  : '))
#     mypolygon = Regular(
#         lenth=user_side_lenth,
#         width=user_side_lenth)
#     mypolygon.setNofSides(user_side_number)
#     mypolygon.premiter()
#     mypolygon.area()
# elif polygonOrNot == 'n':
#     user_side_number = int(input('enter the number of sides  : '))
#     if user_side_number == 3:
#         user_lenth = int(input('enter the base lenth  : '))
#         user_hight = int(input('enter the hight lenth  : '))

#         user_triangle = NonRegTriangle(
#             lenth=user_lenth, width=user_hight)
#         user_triangle.area()

#     elif user_side_number == 4:

#         user_side_lenth = int(input('enter the lenth of side  : '))
#         user_side_width = int(input('enter the lenth of width  : '))
#         myrectangle = rectangle(
#             lenth=user_side_lenth, width=user_side_width)
#         myrectangle.premiter()
#         myrectangle.area()
#     else:
#         print('er')
# else:
#     print('erorrrrrrr')
