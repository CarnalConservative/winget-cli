class warBot:
    def __init__(self): # then creating the init function
        self.locationX = 10 # then initialising the variables and 
        self.locationY = 10 # setting it's initial values 
        self.fuel = 100

    def moveLeft(self):
        if self.fuel >= 5:
            self.locationX -= 1
            self.fuel -= 5
        if self.fuel < 5:
            print("Insufficient fuel to perform action")
        self.captainsLog()

    def moveRight(self):
        if self.fuel >= 5:
            self.locationX += 1
            self.fuel -= 5
        if self.fuel < 5:
            print("Insufficient fuel to perform action")
        self.captainsLog()

    def moveUp(self):
        if self.fuel >= 5:
            self.locationY -= 1
            self.fuel -= 5
        if self.fuel < 5:
            print("Insufficient fuel to perform action")
        self.captainsLog()

    def moveDown(self):
        if self.fuel >= 5:
            self.locationY += 1
            self.fuel -= 5
        if self.fuel < 5:
            print("Insufficient fuel to perform action")
        self.captainsLog()

    def openFire(self):
        if self.fuel >= 15:
            self.fuel -= 15
            print("Pew! Pew!")
        if self.fuel < 15:
            print("Insufficient fuel to perform action")
        self.captainsLog()
        
    def statusReport(self):
        print(f"({self.locationX},{self.locationY}) - Fuel: {self.fuel}.")
        self.captainsLog()

    def finalFrontier(self):
        print("Goodbye")
        quit()

    def captainsLog(self):
        new_orders = input("Enter command: ")
        
        if new_orders == "left":
            self.moveLeft()           
        if new_orders == "right":
            self.moveRight()
        if new_orders == "up":
            self.moveUp()
        if new_orders == "down":
            self.moveDown()
        if new_orders == "fire":
            self.openFire()
        if new_orders == "status":
            self.statusReport()
        if new_orders == "quit":
            self.finalFrontier()
        else:
            print("Invalid command. Try again.")
            self.captainsLog()

def startEngines():
    ship = warBot()    
    ship.captainsLog()
    
if __name__ == "__main__":
    startEngines()