class WrongPaymentException(Exception):
    pass


class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, item, price, quantity):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        tot_price = 0.00
        for i in range(0, len(self.items)):
            tot_price += self.prices[i] * self.quantities[i]
        return round(tot_price, 2)

    def payment_process(self, payment_type, sec_code):
        if payment_type == "debit":
            print(f"Entered security code: {sec_code}")
            print("processing...")
            print("Transaction Successful")
        elif payment_type == "credit":
            print(f"Entered security code: {sec_code}")
            print("processing...")
            print("Transaction Successful")
        else:
            print(f"An exception occurred during handling")
            raise WrongPaymentException("Wrong Payment type")


new_d = Order()
new_d.add_item("Bulb", 5.1, 3)
new_d.add_item("Phone case", 6.25, 1)
new_d.add_item("Beer", 0.45, 6)
new_d.add_item("Nuts", 0.3, 6)


tp = new_d.total_price()
print(f"The total price is {tp}")

new_d.payment_process("Oora",125)

