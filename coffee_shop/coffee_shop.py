from coffee_shop_model import Stats
from coffee_shop_presenter import coffee_shop_simulator

LINE_CAPACITY = 20
SERVE_TIME = 45
NEXT_CUSTOMER_ARRIVAL_TIME_LOW = 10
NEXT_CUSTOMER_ARRIVAL_TIME_HIGH = 60
NUMBER_OF_CUSTOMERS_IN_A_DAY = 150


# random.seed(123)
stats: Stats = coffee_shop_simulator(NUMBER_OF_CUSTOMERS_IN_A_DAY, LINE_CAPACITY, SERVE_TIME,
                                     (NEXT_CUSTOMER_ARRIVAL_TIME_LOW, NEXT_CUSTOMER_ARRIVAL_TIME_HIGH))
