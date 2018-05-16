from src.Booking import Booking
from datetime import datetime
from src.Location import *
class BookingException(Exception):
    def __init__(self, field, msg=None):
        self._field = field
        self._msg = msg


class CarRentalSystem:
    def __init__(self):
        self._cars = []
        self._customers = []
        self._bookings = []

    def car_search(self, name=None, model=None):
        #  pass
        if name is None and model is None:
            return self._cars
        cars = []

        for car in self._cars:
            c_name = car.get_name()
            c_model = car.get_model()
            if name is not None and name.lower() in c_name.lower():
                cars.append(car)
            elif model is not None and model.lower() in c_model.lower():
                cars.append(car)
        return cars

    def make_booking(self, customer, start, end, car, pickup, dropoff):

        if (start is None):
            raise BookingException('start_date','Specify a valid start date ')
        if (end is None):
            raise BookingException('end_date','Specify a valid end date ')
        if (pickup is None):
            raise BookingException('pickup','Specify a valid pickup ')
        if (dropoff is None):
            raise BookingException('dropff','Specify a valid dropoff ')
        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(start, date_format)
        end_date = datetime.strptime(end, date_format)
        if (start_date > end_date):
            raise BookingException('period','Specify valid booking period')
        location = Location(pickup, dropoff)
        new_booking = Booking(customer, start_date,end_date , car, location)
        self._bookings.append(new_booking)
        car.add_booking(new_booking)
        return new_booking

    def get_customer(self, username):
        """
        Just returns the first customer, should do a search but not
        needed for this use case. Will break if no customers in list
        """
        return self._customers[0]

    def add_car(self, car):
        self._cars.append(car)

    def new_customer(self, customer):
        self._customers.append(customer)

    def validate_login(self, username, password):
        for c in self._customers:
            if c.username == username and c.validate_password(password):
                return c
        return None

    def get_user_by_id(self, user_id):
        for c in self._customers:
            if c.get_id() == user_id:
                return c
        return None

    @property
    def cars(self):
        return self._cars

    def get_car(self, rego):
        for c in self._cars:
            if c.get_rego() == rego:
                return c
        return None
