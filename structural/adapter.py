# Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.


# Existing codebase
class Order:
    order_type: str
    price: int
    qty: int

    def __init__(self, order_type, price, qty):
        self.order_type = order_type
        self.price = price
        self.qty = qty


class IInternalService:  # Interface
    def process_order():
        pass


class InternalService(IInternalService):
    # Can only process Order instance
    def process_order(self, order: Order):
        print(
            "Processing order:",
            order.order_type,
            order.price,
            order.qty,
        )


class ExternalService:
    # Can only process a dict
    def service_process_order(self, order: dict):
        print(
            "Service crocessing order:",
            order["order_type"],
            order["price"],
            order["qty"],
        )


class ExternalServiceAdapter(IInternalService):
    service: ExternalService

    def __init__(self, service: ExternalService):
        self.service = service

    def process_order(self, order: Order):
        order = {
            "order_type": order.order_type,
            "price": order.price,
            "qty": order.qty,
        }
        self.service.service_process_order(order)


def main():
    order = Order("limit", 25000, 1)
    # service = InternalService() # Before
    service = ExternalServiceAdapter(ExternalService())  # After use adapter
    service.process_order(order)

    # Why not directly convert data and call external service method?
    # Because If ExternalService method interface change, we have to modify the client code
    # If we use adapter, we only need to update the ExternalServiceAdapter class
    # order = {
    #     "order_type": order.order_type,
    #     "price": order.price,
    #     "qty": order.qty,
    # }
    # ExternalService().service_process_order(order)


main()
