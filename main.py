# game about поле и развитие
from operator import truediv
from random import random


def main():
    pole = pole_c()
    zaic1= zaic(1,2,10)
    pole.add_object(zaic1)

    while True:
        draw_pole(pole)
        pole.iteration

def print_char(x, y, char):
        print("\033["+str(y)+";"+str(x)+"H"+char)

def draw_pole(pole):
    pass
    
    


class pole_c():
    def __init__(o):
        o.objects = list()

    def add_object( o, object  ):
        o.objects.append(object) 

    def iteration(o):
        for object in o.objects:
            object.next()


class zaic():
    def __init__(o,x=1, y=1, id = None, move=True):  #add "move" : if true animal, if false plant.
        if id is None : id = gen_unic_id()
        o.id = id
        o.x = x
        o.y = y

    def move_up(o):
        o.x = o.x + 1
        
    def next(o):
        pass


def gen_unic_id():
    return 1                # TODO : make random id


class sushestvo:
    x = 0
    y = 0
    id = 0
    def __init__(t, id):
        t.id = id

        



if __name__ == "__main__":
    main()