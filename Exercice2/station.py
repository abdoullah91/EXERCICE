class Station:
    def __init__(self, name, location, platform_count):
        self.name = name
        self.location = location
        self.platform_count = platform_count

    def announce_arrival(self):
        print("Annonce : Le train arrive en gare.")

    def announce_departure(self):
        print("Annonce : Le train quitte la gare.")

    def check_tickets(self):
        print("Le contrôleur vérifie les billets des passagers.")

    def open_barrier(self):
        print("Les barrières s'ouvrent pour laisser passer le train.")
