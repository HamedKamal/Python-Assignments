class shape:

    def __init__(self, lenth, width, numberOfSides):
        self.lenth = lenth
        self.width = width
        self.nsides = numberOfSides


class rectangle(shape):
    def area(self):
        print(f"your rectangle area is : {self.lenth*self.width}")

    def premiter(self):
        print(f"the premiter is {self.lenth+self.width+self.lenth+self.width}")


class square(shape):
    def premiter(self):
        print(f"the premiter is {self.nsides*self.lenth}")

    def area(self):
        print(f"your square area is : {self.lenth*self.width}")


class triangle(shape):

    def area(self):
        print(f"your triangle area is :  {self.lenth*self.width*0.5}")


while True:
    user_side = int(input('enter the number of sides  : '))

    if user_side == 4:
        user_lenth = int(input('enter the side lenth  : '))
        user_width = int(input('enter the side width  : '))
        if user_lenth == user_width:
            user_square = square(
                lenth=user_lenth, width=user_width, numberOfSides=user_side)

            user_square.area()
            user_square.premiter()

        else:
            user_rectangle = rectangle(
                lenth=user_lenth, width=user_width, numberOfSides=user_side)
            user_rectangle.area()
            user_rectangle.premiter()

    elif user_side == 3:
        user_lenth = int(input('enter the base lenth  : '))
        user_hight = int(input('enter the hight lenth  : '))

        user_triangle = triangle(
            lenth=user_lenth, width=user_hight, numberOfSides=user_side)
        user_triangle.area()
    break