from datetime import datetime
from room import SingleRoom, DoubleRoom


class UserInterface:
    def __init__(self, hotel):
        self.hotel = hotel
        self.load_data()

    def load_data(self):
        self.hotel.add_room(SingleRoom("101", 10000))
        self.hotel.add_room(SingleRoom("102", 10000))
        self.hotel.add_room(DoubleRoom("201", 15000))
        self.hotel.add_room(DoubleRoom("202", 15000))


    def run(self):
        while True:
            print("\nVálasszon egy számot (1-5)-ig, hogy elérje a kívánt műveletet:")
            print("1. Foglalás felvétele")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Szobák felszereltsége")
            print("5. Kilépés")
            choice = input("Választás: ")

            if choice == "1":
                date = self._input_date()
                if date:
                    self._list_rooms()
                    room_number = input("Adja meg a foglalandó szoba számát: ")
                    num_days = int(input("Adja meg mennyi napot szeretne lefoglalni: "))
                    booking_amount = self.hotel.book_room(room_number, num_days, date)
                    if booking_amount:
                        print(f"Sikeres foglalás! A fizetendő összeg: {booking_amount} Ft")
                    else:
                        print("Nem sikerült foglalni a megadott szobaszámmal.")

            elif choice == "2":
                room_number = input("Add meg a lemondandó foglalásának a szobaszámát: ")
                date = self._input_date()
                if date:
                    cancellation_success = self.hotel.cancel_booking(room_number, date)
                    if cancellation_success:
                        print("A foglalás sikeresen törölve lett.")
                    else:
                        print("Nem található foglalás a megadott szobaszámmal és dátummal.")

            elif choice == "3":
                self.hotel.list_bookings()

            elif choice == "4":
                self.hotel.list_amenities()

            elif choice == "5":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen szám. Kérem válasszon újra (1-5)-ig.")

    def _input_date(self):
        while True:
            date_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                if date < datetime.now():
                    print("A megadott dátumnak valósnak kell lennie.")
                else:
                    return date
            except ValueError:
                print("Hibás dátumformátum. Kérem próbálja újra.")

    def _list_rooms(self):
        print("Elérhető szobák:")
        for room in self.hotel.rooms:
            if isinstance(room, SingleRoom):
                print(f"Szobaszám: {room.room_number} (Egyágyas), Ár: {room.price} Ft/éjszaka")
            elif isinstance(room, DoubleRoom):
                print(f"Szobaszám: {room.room_number} (Kétágyas), Ár: {room.price} Ft/éjszaka")

