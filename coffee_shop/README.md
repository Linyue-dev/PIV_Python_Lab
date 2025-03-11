

# Queues

We (Sandy and Ian) have given up on teaching and have opened a coffee/tea shop!  We have coded a simulator to see how happy our customers will be. 

-   There is one server (Sandy or Ian).
-   There is a line up of customers, modelled by a queue. We can set the capacity of the queue to model the size of our store.
-   Customers arrive one by one from a "pool" of customers (left-hand side of screen)
-   Served customers appear on the right.
-   Some customers arrive and the queue is full, those will walk away and get coffee/tea at some other shop.
-   Customers who wait in line start to get annoyed. Green means happy, yellow means less happy, and red means angry!


## Run the original version

This project might work best when run from the console. To do this you will need to make a virtual environment and install the `rich` library:

    cd to/the/starter/code
    python3 -m venv .venv       # create the virtual enviroment
    source .venv/bin/activate   # load the venv (your prompt should be prefixed with (.venv) 
    python3 -m pip install rich # install dependency
    python3 coffee_shop.py

The simulation is configured in `coffee_shop.py`, try a few different values to see what happens.


## Customer Priorities

We're hiring you to implement a customer loyalty program.

There are 5 tiers of customers 0-4 that indicate their loyalty, where 0 is the most loyal and 4 is the least. A customer's loyalty will them priority in the shop's line up over less-loyal customers. For example, if Vik is in line with loyalty 2 and Youmna arrives with loyalty 1, we would serve Youmna before Vik.

Customers of all loyalty levels will still walk away if they arrive and the line up is full.


## TODOs

1.  In `coffee_shop_model.py`, create a `PriorityCustomer` class that extends the original `Customer` class.
2.  Define an *ordering* of for priority customers. You do this by implementing the `<` operator for your class. In python, you need to code the `__lt__` method:
    
        def __lt__(self, other: PriorityCustomer) -> bool:
            pass

3.  Implement `__str__` to be the loyalty number of the priority customer, so you can tell the different customers appart:
    
        └──────────────────┘
        0324332
        ┌──────────────────┐

1.  Replace the `Queue` in `coffee_shop_presenter.py` with a `PriorityQueue`. The basic queue operations `put` and `get` are the same.
2.  In `coffee_shop_presenter.py`, replace the pool of customers with random priority customers. See the "Create the customers" section. Recall that `random.randint` can be used to create random numbers.

