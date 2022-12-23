# class Cars:
#     __objects=0
#     def __init__(self,  model, max_speed, min_spped,state):
#         self.cars_maximum_speed = max_speed
#         self.cars_state=state
#         self.cars_model = model
#         self.cars_minmun_spped = min_spped
        
    
#     def info(self):
#         print( f"cars name {self.cars_model}\ncars maximum speed {self.cars_maximum_speed}\ncars minimum speed {self.cars_minmun_spped}")
#     def state(self):
#         if self.state ==True:
#             print(f"cars  speed before go {self.cars_minmun_spped}")
#             while self.cars_minmun_spped<self.cars_maximum_speed:
#                 self.cars_minmun_spped+=10
#             print(f"cars  speed after go {self.cars_minmun_spped}")
#         else :
#             print('hello from brake ')
    
    


# first_car=Cars(model='audi',max_speed=50,min_spped=20,state=False)
# secound_car=Cars(model='ferari',max_speed=70,min_spped=10,state=False)

# # first_car.color='blue'
# # secound_car.color='red'

# # first_car.state()
# first_car.info()
# print('*'*25)
# secound_car.info()

# # print(dir(Cars)) 
# # print(Cars.color)
# first_car._Cars__objects=5  
# print(first_car._Cars__objects)
class BankAccount:
    def __init__(self,name) :
        self.__name=name
        # self.__balance=balance
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name

var=BankAccount('hamed')
print(var.getname())
var.__class__name='mohamed'
print(var.__class__name)
