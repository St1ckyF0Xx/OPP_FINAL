from datetime import datetime, timedelta
from room import SingleRoom, DoubleRoom
from booking import Booking

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_number, number_of_days, date):
        if not self._valid_date(date):
            print("Hibás dátum! Kérem adjon meg egy jövőbeli dátumot.")
            return None

        if not self._room_available(room_number, date, number_of_days):
            print("A megadott szoba nem elérhető az adott időpontban.")
            return None

        for room in self.rooms:
            if room.room_number == room_number:
                booking_amount = room.calculate_price(number_of_days)
                booking = Booking(room_number, number_of_days, date, booking_amount)
                self.bookings.append(booking)
                return booking_amount
        return None

    def cancel_booking(self, room_number, date):
        for booking in self.bookings:
            if booking.room_number == room_number and booking.date == date:
                self.bookings.remove(booking)
                return True
        return False

    def list_bookings(self):
        for booking in self.bookings:
            print(f"Foglalás a(z) {booking.date}-kor, szobaszám: {booking.room_number}, {booking.number_of_days} napra, összeg: {booking.amount} Ft")

    def _valid_date(self, date):
        return date > datetime.now()

    def _room_available(self, room_number, date, number_of_days):
        booked_dates = set()
        for booking in self.bookings:
            if booking.room_number == room_number:
                booked_dates.update([booking.date + timedelta(days=i) for i in range(booking.number_of_days)])
        notified_dates = set([date + timedelta(days=i) for i in range(number_of_days)])
        return len(notified_dates.intersection(booked_dates)) == 0

    def list_amenities(self):
        print("\nEgyágyas szobák felszereltsége:")
        single_room_exist = False
        for room in self.rooms:
            if isinstance(room, SingleRoom) and not single_room_exist:
                print(f"Ár: {room.price}")
                print(f"Asztal: {'Van' if hasattr(room, 'asztal') else 'Nincs'}")
                print(f"Minibar: {'Yes' if hasattr(room, 'minibar') else 'Nincs'}")
                print(f"Klíma: {'Van' if hasattr(room, 'klima') else 'Nincs'}")
                print()
                single_room_exist = True

        print("\nKétágyas szobák felszereltsége:")
        double_room_exist = False
        for room in self.rooms:
            if isinstance(room, DoubleRoom) and not double_room_exist:
                print(f"Ár: {room.price}")
                print(f"Erkély: {'Van' if hasattr(room, 'erkely') else 'Nincs'}")
                print(f"TV: {'Van' if hasattr(room, 'TV') else 'Nincs'}")
                print(f"Kilátás: {'Van' if hasattr(room, 'kilatas') else 'Nincs'}")
                print()
                double_room_exist = True


