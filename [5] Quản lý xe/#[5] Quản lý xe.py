#[5] Quản lý xe
class car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    def tang_so_km(self, mileage):
        self.mileage = self.mileage + mileage
        return self.mileage
    def hien_thi_tt(self):
        print("Make: ", self.make)
        print("Model: ", self.model)
        print("Year: ", self.year)
        print("Mileage: ", self.mileage)
a = car("Honda", "Wave alpha", 2015, 66655)
a.hien_thi_tt()
mileage = int(input())
a.tang_so_km(mileage)
a.hien_thi_tt()