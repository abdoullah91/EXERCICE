class Passenger:
    def __init__(self, name, age, ticket_number):
        self.name = name
        self.age = age
        self.ticket_number = ticket_number

    def buy_ticket(self):
        print("Le passager achète un billet.")

    def show_ticket(self):
        print("Le passager présente son billet.")

    def find_seat(self):
        print("Le passager cherche sa place dans le train.")

    def request_assistance(self):
        print("Le passager demande de l'aide.")
