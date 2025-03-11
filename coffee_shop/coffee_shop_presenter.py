import random
from coffee_shop_model import Customer, PriorityCustomer, Stats, PRIORITY_CUSTOMER_NUMBER_PRIORITIES
from coffee_shop_view import layout_background, update_image
import coffee_shop_view

from our_queue import Queue
from queue import PriorityQueue
from time import sleep

"""Sandy and Ian's Coffee Shop!"""


def coffee_shop_simulator(number_of_customers: int, line_capacity: int,
                          serve_time: int,
                          min_max_wait_time_next_customer: tuple[int, int]) -> Stats:
    """
    Simulate the serving line at a coffee shop using a queue.
    :param number_of_customers: The number of customers served in a day.
    :param line_capacity: The maximum number of people who can stand in line.
    :param serve_time: The time in seconds to serve a customer.
    :param min_max_wait_time_next_customer: The lowest/highest amount of time for the arrival of the next customer.
    :return: The statistics accumulated during the simulation.
    """

    # ------------------------------------------------------------------------
    # initial setup
    # ------------------------------------------------------------------------
    layout = layout_background(serve_time)
    coffee_shop_view.MAX_WAIT_TIME = line_capacity*serve_time

    # store customers in a queue data structure
    line_up: PriorityQueue[PriorityCustomer] = PriorityQueue(maxsize=line_capacity)

    # track statistics throughout simulation
    stats: Stats = Stats()

    # countdown to next coffee served
    next_serve_time: int = serve_time

    # stats
    served: list[PriorityCustomer] = []
    turned_away: list[PriorityCustomer] = []

    # ------------------------------------------------------------------------
    # create the customers
    # ------------------------------------------------------------------------
    customers: list[Customer] = []
    for i in range(number_of_customers):
        wait_time = random.randint(*min_max_wait_time_next_customer)

        customer: PriorityCustomer = PriorityCustomer(
            number=i + 1,
            delta_time_between_customers=wait_time,
            priority = random.randint(1,5)
        )

        customers.append(customer)

    # ------------------------------------------------------------------------
    # open the shop and start server customers
    # ------------------------------------------------------------------------
    time = 0
    next_customer_arrival_time: int = customers[0].delta_time_between_customers
    while len(customers) > 0 or not line_up.empty():
        time += 1

        sleep(0.01)  # slow down the simulation a bit
        changed = False

        next_customer_arrival_time -= 1
        next_serve_time = max(next_serve_time-1, 0)

        # --------------------------------------------------------------------
        # next customer arrives and is either turned away or enters the line.
        # --------------------------------------------------------------------
        if next_customer_arrival_time == 0 and len(customers) != 0:
            changed = True
            next_customer: Customer = customers.pop(0)
            next_customer.arrival_time = time
            if line_up.full():
                stats.customers_turned_away += 1
                next_customer.current_time = time
                turned_away.append(next_customer)
            else:
                line_up.put(next_customer)

            # set up the arrival of the next customer.
            next_customer_arrival_time = customers[0].delta_time_between_customers if len(customers) != 0 else 0

        # --------------------------------------------------------------------
        # Is the server idle or not? if not make coffee
        # --------------------------------------------------------------------
        if line_up.empty():
            stats.server_idle += 1

        else:
            if next_serve_time == 0:
                cust: Customer = line_up.get(False)
                cust.served_time = time
                served.append(cust)
                stats.customers_served += 1
                next_serve_time = serve_time
                changed = True

        if changed:
            for customer in line_up.queue:
                customer.current_time = time
            update_image(customers, layout, turned_away, line_up, served)

    # --------------------------------------------------------------------
    # final report
    # --------------------------------------------------------------------
    print(f"Served {stats.customers_served} customers.")
    print(f"Was idle for {stats.server_idle} seconds.")
    print(f"Turned away {stats.customers_turned_away} customers.")

    return stats
