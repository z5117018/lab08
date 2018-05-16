class PeriodError(Exception):
    pass

class Booking(object):

    def __init__(self, customer, start, end, car, location):
        self._customer = customer
        self._start = start
        self._end = end
        self._car = car
        self._location = location
    
    @property
    def booking_fee(self):
        fee = self._car.get_fee(self._period)
        return fee

    def get_period(self):
        period = self._end - self._start
        return period.days
    @property
    def location(self):
        return self._location

    def __str__(self):
        return "Booking for: {}, {}".format(self._customer, self._car)
