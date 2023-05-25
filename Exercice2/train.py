class Train:
    def __init__(self, name, capacity, speed):
        self.name = name
        self.capacity = capacity
        self.speed = speed

    def accelerate(self):
        print("Le train accélère.")

    def brake(self):
        print("Le train freine.")

    def board_passenger(self):
        print("Un passager monte à bord du train.")

    def disembark_passenger(self):
        print("Un passager descend du train.")
