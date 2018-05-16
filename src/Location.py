class Location:
    def __init__(self, pickup, dropoff):
        if (pickup is None or dropoff is None):
            raise ValueError
        self._pickup = pickup
        self._dropoff = dropoff

    @property
    def pickup(self):
        return self._pickup

    @property
    def dropoff(self):
        return self._dropoff

    def __str__(self):
        return "Location Details: pickup - {}, dropoff - {}".format(self.pickup, self.dropoff)
