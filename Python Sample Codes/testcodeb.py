class Robot:

    def __init__(self):
        self.fuel=100#assigning intial fuel as 100 and x,y coordinate as 10
        self.x_coordinate=10
        self.y_coordinate=10
    

    def left(self):
        if(self.fuel<5): #checking whether the action can be performed
            print("Insufficient fuel to perform action")
        else:
            self.fuel-=5#performing action
            self.x_coordinate-=1

    def right(self):
        if(self.fuel<5):
            print("Insufficient fuel to perform action")
        else:
            self.fuel-=5
            self.x_coordinate+=1

    def down(self):
        if(self.fuel<5):
            print("Insufficient fuel to perform action")
        else:
            self.fuel-=5
            self.y_coordinate+=1

    def up(self):
        if(self.fuel<5):
            print("Insufficient fuel to perform action")
        else:
            self.fuel-=5
            self.y_coordinate-=1

    def fire(self):
        if(self.fuel<15):
            print("Insufficient fuel to perform action")
        else:
            self.fuel-=15
            print("Pew! Pew!")

    def status(self):
        print("x_coordinate : "+str(self.x_coordinate)+" y_coordinate : " +str(self.y_coordinate)+" Fuel : "+str(self.fuel))

if __name__ == "__main__":
    
    r=Robot()
    print("Choices : left right up down fire status and quit")
    while(True):
        ch=input()
        if(ch=="left"):
            r.left()
        if(ch=="right"):
            r.right()
        if(ch=="up"):
            r.up()
        if(ch=="down"):
            r.down()
        if(ch=="fire"):
            r.fire()
        if(ch=="status"):
            r.status()
        if(ch=="quit"):
            print("Goodbye")
            break