# my_str = 'Hi'
# my_str2 = 'Mike'
# new_str = my_str + my_str2
# print(new_str)

class Room:
    def __init__(self, l, w):
        self.l = l
        self.w = w 

    def get_s(self):
        return self.l * self.w
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.get_s() + other 
        elif isinstance(other, Room):
            return self.get_s() + other.get_s()
        return 0


room_1 = Room(2, 3)
print(room_1.get_s())

room_2 = Room(3, 4)
print(room_2.get_s())

s = room_1 + room_2
print(s)