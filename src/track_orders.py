from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        cust_orders = []
        for each in self.orders:
            if each[0] == customer:
                cust_orders.append(each[1])

        return Counter(cust_orders).most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        food_set = set(each[1] for each in self.orders)
        cust_orders = set()
        for each in self.orders:
            if each[0] == customer:
                cust_orders.add(each[1])
        print(food_set)
        print(cust_orders)
        return food_set - cust_orders

    def get_days_never_visited_per_customer(self, customer):
        day_set = set(each[2] for each in self.orders)
        cust_days = set()
        for each in self.orders:
            if each[0] == customer:
                cust_days.add(each[2])
        return day_set - cust_days

    def get_busiest_day(self):
        days = []
        for each in self.orders:
            days.append(each[2])

        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        days = []
        for each in self.orders:
            days.append(each[2])

        return Counter(days).most_common()[-1][0]
