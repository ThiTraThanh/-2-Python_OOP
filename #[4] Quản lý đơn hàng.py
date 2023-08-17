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
products = ["san pham 1", "san pham 2"]
total_amount = [10, 25]
a = order("id1", products, total_amount)
print(a.total_bill(total_amount))