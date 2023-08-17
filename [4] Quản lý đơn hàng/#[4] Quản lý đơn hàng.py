#[4] Quản lý đơn hàng
class order:
    def __init__(self, order_id, products, total_amount):
        self.order_id = order_id
        self.products = products
        self.total_amount = total_amount
    def total_bill(self, total_amount):
        s = 0
        for i in total_amount:
            s = s + i
        return s
print("Nhap so san pham")
n = int(input())
products = []
total_amount = []
for i in range(n):
    products.append(input())
    total_amount.append(int(input()))
a = order("id1", products, total_amount)
print("Total amount =", a.total_bill(total_amount))