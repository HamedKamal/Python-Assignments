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
        print(type(self.lenth))

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

class Circle(shape):
    def generalForm(self):
        newX=-2*self.lenth
        newY=-2*self.width
        r=self.getNofSides()
        newR=(self.lenth**2)+(self.width**2)-(r**2)
        #  if all is positive
        condition=(self.lenth**2)+(self.width**2)-newR
        if condition>0:
            print(f"general equation : x² + y² + {newX}x + {newY}y + {newR} = 0")
        else:
            print('general equation eroeoeoerrr')
    def standardForm(self):
        newX=-1*self.lenth
        newY=-1*self.width
        
            
        r=self.getNofSides()
        
        newY=float(newY)
        newX=float(newX)
        r=float(r)
        # if x and y are positve
        if newX > 0 and newY > 0:
            print(f"standard equation = (x + {newX})²+(y + {newY})²= {r**2}")
        # if x negative and y positve
        elif newX <0 and newY >0:
            print(f"standard equation = (x  {newX})²+(y + {newY})²= {r**2}")
        # if x positive and y negative
        elif newX >0 and newY <0:
            print(f"standard equation = (x+ {newX})²+(y {newY})²= {r**2}")
        # if x  and y are  negative
        elif newX <0 and newY <0:
            print(f"standard equation = (x {newX})²+(y {newY})²= {r**2}")
    def premiter(self):
        r=self.getNofSides()
        
        print(f"the Circle Circmfrance = {2*math.pi*r}")
    def area(self):
        r=self.getNofSides()
        
        print(f"the Circle Area = {math.pi*(r**2)}")
    


polygonOrNot = input('Is it a regular polygon ? (y/n)  : ')
if polygonOrNot == 'y':
    isitcircle=input('Is it a regular circle ? (y/n)  :')
    if isitcircle=="y":
        xCenter=float(input('enter the x of center '))
        yCenter=float(input('enter the y of center '))
        raduis=float(input('enter the Radius of circle '))
        mycircle=Circle(lenth=xCenter,width=yCenter,)
        mycircle.setNofSides(raduis)
        mycircle.standardForm()
        mycircle.generalForm()
        mycircle.premiter()
        mycircle.area()
    elif isitcircle == "n":
        user_side_number = int(input('enter the number of sides  : '))
        user_side_lenth = int(input('enter the lenth of side  : '))
        mypolygon = Regular(
            lenth=user_side_lenth,
            width=user_side_lenth)
        mypolygon.setNofSides(user_side_number)
        mypolygon.premiter()
        mypolygon.area()
    else:
        print('erererrrrrrrrooeroeroero')
elif polygonOrNot == 'n':
    user_side_number = int(input('enter the number of sides  : '))
    if user_side_number == 3:
        user_lenth = int(input('enter the base lenth  : '))
        user_hight = int(input('enter the hight lenth  : '))

        user_triangle = NonRegTriangle(
            lenth=user_lenth, width=user_hight)
        user_triangle.area()

    elif user_side_number == 4:

        user_side_lenth = int(input('enter the lenth of side  : '))
        user_side_width = int(input('enter the lenth of width  : '))
        myrectangle = rectangle(
            lenth=user_side_lenth, width=user_side_width)
        myrectangle.premiter()
        myrectangle.area()
    else:
        print('er')
else:
    print('erorrrrrrr')
