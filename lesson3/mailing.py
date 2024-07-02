from address import Address


class Mailing:
    to_address = Address
    from_address = Address
    cost = 0
    track = ""

    def __init__(self, to_address, from_address, cost, track):
        self.to = to_address
        self.fr = from_address
        self.c = cost
        self.t = track
