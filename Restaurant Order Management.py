# Task 1
# Design a queue-based data structure to represent the kitchen's order queue, 
# where orders are processed in the order they are received. The first order in is the first one out.

class OrderQueue:
    def __init__(self):
        self.orders = []

    # Task 2
    # Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.

    def is_empty(self):
        return len(self.orders) == 0

    def add_order(self, order):
        self.orders.append(order)

        print("Order added!")

    def remove_order(self):
        if not self.is_empty():
            removed_order = self.orders.pop(0)

            print("Order removed!")

            return removed_order

        print("No orders to remove!")

order_queue = OrderQueue()

order_queue.add_order({"id": 1, "item": "Cajun Risotto", "quantity": 1})
order_queue.remove_order()
order_queue.remove_order()