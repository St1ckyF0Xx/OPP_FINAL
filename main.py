from Interface import UserInterface
from hotel import Hotel
from booking import Booking
from datetime import datetime

def main():
    hotel = Hotel("St1ckyF0Xx")
    bookings = [
        Booking("101", 3, datetime(2024, 5, 10), 30000),
        Booking("201", 2, datetime(2024, 5, 15), 30000),
        Booking("102", 4, datetime(2024, 5, 18), 48000),
        Booking("101", 2, datetime(2024, 5, 22), 20000),
        Booking("201", 3, datetime(2024, 5, 25), 45000)
    ]
    hotel.bookings.extend(bookings)

    interface = UserInterface(hotel)
    interface.run()

if __name__ == "__main__":
    main()


