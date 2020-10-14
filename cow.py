
class Cow:

    def __init__(self, id):
        self.id = id
        self.num_milkings = 0
        self.total_milk_prod = 0
        self.latest_weight = None
        self.lowest_weight = None
        self.temp = None
        self.parent = None
        self.left = None
        self.right = None

    def set_weight(self, weight):
        self.latest_weight = weight
        if not self.lowest_weight:
            self.lowest_weight = weight
        else:
            if weight < self.lowest_weight:
                self.lowest_weight = weight

    def set_temperature(self, temperature):
        self.temp = temperature

    def add_milk(self, milk):
        self.num_milkings += 1
        self.total_milk_prod += milk

    def get_lowest_weight(self):
        return self.lowest_weight

    def get_latest_weight(self):
        return self.latest_weight

    def get_temperature(self):
        return self.temp

    def get_avg_milk_prod(self):
        return int(self.total_milk_prod/self.num_milkings)

    def get_status(self):
        if self.num_milkings == 0 or not self.latest_weight:
            return None
        return "{} {} {} {}".format(self.id, self.lowest_weight, self.latest_weight, self.get_avg_milk_prod())