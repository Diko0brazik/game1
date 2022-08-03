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
    for x, y in pole.pole:
        char = pole.pole[(x,y)]
        print_char(x, y, char)

    


class pole_c():
    def __init__(o):
        o.objects = list()
        max_x = 50
        max_y = 20
        keys = []
        for x in range(1, max_x):
            for y in range(1, max_y):
                keys.append((x,y,))
        o.pole = dict((k, '.') for k in keys )


    def add_object( o, object  ):
        o.objects.append(object) 

    def iteration(o):
        for object in o.objects:
            object.next(o)
            o.chek_object_position(object)

    def chek_object_position(o, object):
        pass

    def place_objects(o):
        for k in o.pole:
            o.pole[k] = '.'
        for object in o.objects:





class zaic():
    def __init__(o,x=1, y=1, id = None, move=True):  #add "move" : if true animal, if false plant.
        if id is None : id = gen_unic_id()
        o.id = id
        o.x = x
        o.y = y
        o.xy = [o.x, o.y]


    def move_down(o):
        o.x = o.x - 1
        
    def next(o, pole):
        o.move_down()
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