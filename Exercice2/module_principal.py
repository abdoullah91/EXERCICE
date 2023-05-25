from train import Train
from station import Station
from passenger import Passenger

def main():
    # Instanciation des objets
    train = Train("Express", 200, 100)
    station = Station("Gare Centrale", "Ville A", 3)
    passenger = Passenger("John Doe", 30, "T12345")

    # Utilisation des objets
    train.accelerate()
    station.announce_arrival()
    passenger.buy_ticket()

    # ...

if __name__ == "__main__":
    main()
