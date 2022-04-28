#data encapsulation format
class P:

    def __init__(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

#data encapsulation demo
from mutators import P
p1 = P(42)
p2 = P(4711)
p1.get_x()
#Output: 42
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
p1.get_x()
#Output: 4758

#data encapsulation IN PYTHON
class P:

    def __init__(self,x):
        self.x = x
#data encapsulation PYTHON demo
from p import P
p1 = P(42)
p2 = P(4711)
p1.x
#Output: 42
p1.x = 47
p1.x = p1.x + p2.x
p1.x
#Output: 4758

#DEMO 2
class P:

    def __init__(self, x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
#DEMO 3
class P:

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
#DEMO 4
class Robot:

    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 
  
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4 )
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)
#Seems to be okay!
#I feel bad!

#DEMO 5&6
class OurClass:

    def __init__(self, a):
        self.OurAtt = a


x = OurClass(10)
print(x.OurAtt)
#10
class OurClass:

    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)
#10