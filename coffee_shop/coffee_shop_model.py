from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from rich.console import RenderResult, ConsoleOptions
from rich import console


# ============================================================================
# Customer
# ============================================================================
@dataclass
class Customer:
    """
    Customer
    :param number: the number refers to the number they were given when they entered the store
    :param delta_time_between_customers: the time between the previous customer, and this customer
    """
    number: int
    delta_time_between_customers: int
    arrival_time: Optional[int] = None
    current_time: Optional[int] = None
    served_time: Optional[int] = None
    
    def __str__(self):
        return "@"

    def __repr__(self):
        return str(self)

    def __lt__(self, other) -> bool:
        """comparison between customers is the based on the `number` property"""
        return self.number < other.number


# ============================================================================
# PriorityCustomer
# ============================================================================
PRIORITY_CUSTOMER_NUMBER_PRIORITIES = 5

@dataclass
class PriorityCustomer(Customer):
    """
    PriorityCustomer
    Customer
    :param number: the number refers to the number they were given when they entered the store
    :param delta_time_between_customers: the time between the previous customer, and this customer
    :param priority: the customers with the lower priority numbers get served before the higher priority
    """
    # TODO complete this class!
    priority: int = 0

    def __lt__(self, other) -> bool:
        return ((self.priority, self.number) < (other.priority, self.number))

    def __str__(self) -> str:
        return str(self.priority)
    
# ============================================================================
# Stats
# ============================================================================
@dataclass
class Stats:
    """Data class for collecting simulation statistics."""
    server_idle: int = 0
    customers_served: int = 0
    customers_turned_away: int = 0
