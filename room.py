from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price

    @abstractmethod
    def calculate_price(self, number_of_days):
        pass

class SingleRoom(Room):
    def __init__(self, room_number, asztal=None, minibar=None, klima=None):
        super().__init__(room_number, 10000)
        self.asztal = asztal
        self.minibar = minibar
        self.klima = klima

    def calculate_price(self, number_of_days):
        return self.price * number_of_days

class DoubleRoom(Room):
    def __init__(self, room_number, erkely=None, TV=None, kilatas=None):
        super().__init__(room_number, 15000)
        self.erkely = erkely
        self.TV = TV
        self.kilatas = kilatas

    def calculate_price(self, number_of_days):
        return self.price * number_of_days