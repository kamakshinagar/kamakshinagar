import math
import random
requests = input("Enter requests: ")
dynos = input("Enter dynos: ")
available_routers=3

class Routers(object):
    def __init__(self, number, value):
        self.number = number
        self.value = value

my_routers = []

for i in range(available_routers):
    my_routers.append(Routers(i,200*dynos))

# later
for obj in my_routers:
    print (obj.number, obj.value)

selected = random.choice(my_routers)
print("selected router is = ", selected.number)

if selected.value > requests :
    print("200 OK")
else:
    print("H11 Error")


