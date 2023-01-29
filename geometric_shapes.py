import math
class shape:

    def __init__(self, lenth, width, numberOfSides):
        self.lenth = lenth
        self.width = width
        self.nsides = numberOfSides


class rectangle(shape):
    def area(self):
        print(f"your rectangle area is : {self.lenth*self.width}")

    def premiter(self):
        print(f"the premiter is {2*(self.lenth+self.width)}")

class NonRegTriangle(shape):

    def area(self):
        print(f"your triangle area is :  {self.lenth*self.width*0.5}")
        print(' if you want premiter "ﻢﻬﻌﻤﺟﺍ"')
    
class Regular(shape):
    def premiter(self):
        print(f"the premiter is {self.nsides*self.lenth}")
    def area(self):
        print(f"the area is {(self.nsides*self.lenth**2)/(4*(math.tan((180/self.nsides)*math.pi/180)))}")
        
    

polygonOrNot = input('Is it a regular polygon ? (y/n)  : ')
if polygonOrNot=='y':
    user_side_number = int(input('enter the number of sides  : '))
    user_side_lenth = int(input('enter the lenth of side  : '))
    mypolygon=Regular(lenth=user_side_lenth,width=user_side_lenth,numberOfSides=user_side_number)
    mypolygon.premiter()
    mypolygon.area()
elif polygonOrNot=='n':
    user_side_number = int(input('enter the number of sides  : '))
    if user_side_number ==3:
        user_lenth = int(input('enter the base lenth  : '))
        user_hight = int(input('enter the hight lenth  : '))

        user_triangle = NonRegTriangle(
            lenth=user_lenth, width=user_hight, numberOfSides=user_lenth)
        user_triangle.area()

    if user_side_number==4:
        
        user_side_lenth = int(input('enter the lenth of side  : '))
        user_side_width = int(input('enter the lenth of width  : '))
        myrectangle=rectangle(lenth=user_side_lenth,width=user_side_width,numberOfSides=user_side_number)
        myrectangle.premiter()
        myrectangle.area()
