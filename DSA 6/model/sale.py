class Sale:
    def __init__(self, transaction_id, product, region, quantity, unit_price, total_sales, date):
        self.transaction_id = transaction_id
        self.product = product
        self.region = region
        self.quantity = int(quantity)
        self.unit_price = float(unit_price)
        self.total_sales = float(total_sales)
        self.date = date #keep as string for simplicity

    def __repr__(self):
        return(f"Sale({self.transaction_id}, {self.product},"
               f"{self.region}, Qty={self.quantity},"
               f"Total={self.total_sales})")