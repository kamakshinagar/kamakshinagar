import math
import random
#req = input("Enter requests: ")
#dyno = input("Enter dynos: ")

class Routers(object):
    def __init__(self, number, value):
        self.number = number
        self.value = value

def main_function(req,dyno):
    response = None
    available_routers = 4
    my_routers = []
    for i in range(available_routers):
        my_routers.append(Routers(i,200*int(dyno)))
# later
    for obj in my_routers:
      print (obj.number, obj.value)
    selected = random.choice(my_routers)
    print("selected router is = ", selected.number)    
    if selected.value > int(req) :
                response = "200 OK"
    else:
                response = "H11 Error"
    return response
#main_function(700,4)
