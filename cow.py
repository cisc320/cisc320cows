
class Cow:

    def __init__(self, id):
        self.id = id
        self.latest_weight = None
        self.lowest_weight = None
        self.num_milkings = 0
        self.total_milk_prod = 0
        self.temp = None

    def set_weight(self, weight):
        self.latest_weight = weight
        if self.lowest_weight == None:
            self.lowest_weight = weight
        else:
            if weight < self.lowest_weight:
                self.lowest_weight = weight

    def set_temperature(self, temperature):
        self.temp = temperature

    def add_milk(self, milk):
        self.num_milkings += 1
        self.total_milk_prod += milk

    def get_avg_milk_prod(self):
        return self.total_milk_prod/self.num_milkings

    def get_status(self):
        return "{} {} {} {}".format(self.id, self.lowest_weight, self.latest_weight, self.get_avg_milk_prod())