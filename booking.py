from datetime import datetime

class Booking:
    def __init__(self, room_number, number_of_days, date, amount):
        self.room_number = room_number
        self.number_of_days = number_of_days
        self.date = date
        self.amount = amount
'''
def create_bookings():
    bookings = [
        Booking("101", 3, datetime(2024, 5, 10), 30000),
        Booking("201", 2, datetime(2024, 5, 15), 30000),
        Booking("102", 4, datetime(2024, 5, 18), 48000),
        Booking("101", 2, datetime(2024, 5, 22), 20000),
        Booking("201", 3, datetime(2024, 5, 25), 45000)
    ]
    return bookings'''
