# ============================================================================
# things we might render
# ============================================================================
from coffee_shop_model import Customer, PriorityCustomer, PRIORITY_CUSTOMER_NUMBER_PRIORITIES
from our_queue import Queue
from queue import PriorityQueue


# ============================================================================
# Fancy console stuff
# ============================================================================
from rich import box
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.align import Align
from rich.protocol import rich_cast
from rich.panel import Panel

LAYOUT_SHOP = "Shop"
LAYOUT_SERVER = "Server"
LAYOUT_TITLE = "Title"
LAYOUT_LINE = "Line"
LAYOUT_PUBLIC = "Public"
LAYOUT_SERVED = "Served"
LAYOUT_WALKED_AWAY = "NotServed"

TITLE_PUBLIC = "Daily Customers"
TITLE_SERVED = "Served Customers"
TITLE_WALKED_AWAY = "Customers who walked away"

SHOP_TITLE = "Sandy and Ian's Coffee"

console: Console = Console() # color_system="truecolor")
panel = Panel("", box.ROUNDED)


priority_colors = ["white", "yellow1", "green4",  "orange3", "red"]
MAX_WAIT_TIME = 20

# =============================================================================
# add rendering methods to required classes
# =============================================================================

def queue_str(self: Queue | PriorityQueue):
    line = "".join(map(rich_cast, self.queue))
    top = "└" + ("─" * (self.maxsize - 2)) + "┘"
    bot = "[white]┌" + ("─" * (self.maxsize - 2)) + "┐"
    return "\n".join((top, line, bot))


def colored_customer_str(self: Customer | PriorityCustomer):
    
    customer_str = str(self)
    
    if self.arrival_time is None:
        return f"[gray30]{customer_str}"

    if self.served_time is not None:
        elapsed_time = self.served_time - self.arrival_time
    else:
        elapsed_time = self.current_time - self.arrival_time

    # to simplify the calculation
    half_wait_time = MAX_WAIT_TIME / 2

    # linear transition from green rgb(0,255,0) to red rgb(255,0,0) by way of yellow rgb(255,255,0)
    # - add red to green until the halfway point
    # - remove green from yellow from the halfway point onwards.
    
    if elapsed_time > MAX_WAIT_TIME:
        red = 255
        green = 0
    elif elapsed_time < half_wait_time:
        red = int(255 * elapsed_time / half_wait_time)
        green = 255
    else:
        red = 255
        green = int(255 * (1 - (elapsed_time - half_wait_time) / half_wait_time))
   
    colour = f"rgb({red},{green},0)"
    return f"[{colour}]{customer_str}"

PriorityQueue.__rich__ = queue_str
Queue.__rich__ = queue_str
Customer.__rich__ = colored_customer_str # customer_str
PriorityCustomer.__rich__ = colored_customer_str # priority_customer_str


# =============================================================================
# background
# =============================================================================

def layout_background(serve_time) -> Layout:
    """Clear the screen and draw the basics of the store background"""
    console.clear()
    layout: Layout = Layout()
    layout.split_column(
        Layout(name=LAYOUT_TITLE),
        Layout(name=LAYOUT_SHOP)
    )
    layout[LAYOUT_SHOP].split_row(
        Layout(name=LAYOUT_SERVER),
        Layout(name=LAYOUT_LINE),
        Layout(name=LAYOUT_PUBLIC)
    )
    layout[LAYOUT_SERVER].split_column(
        Layout(name=LAYOUT_SERVED),
        Layout(name=LAYOUT_WALKED_AWAY)
    )
    table = Table()
    table.add_column(SHOP_TITLE, justify="center", style="cyan", no_wrap=True)
    table.add_row(f"Served in {serve_time} seconds or it's free!")
    layout[LAYOUT_TITLE].update(Align.center(table, vertical="middle"))

    return layout


# =============================================================================
# update
# =============================================================================

def update_image(customers: list[PriorityCustomer],
                 layout: Layout,
                 left: list[PriorityCustomer],
                 line_up: Queue | PriorityQueue,
                 served: list[PriorityCustomer]):
    console.clear()
    layout[LAYOUT_LINE].update(Align.center(line_up, vertical="middle"))
    layout[LAYOUT_PUBLIC].update(Panel.fit("".join(map(rich_cast, customers)), title=TITLE_PUBLIC))
    layout[LAYOUT_SERVED].update(panel.fit("".join(map(rich_cast, served)), title=TITLE_SERVED))
    layout[LAYOUT_WALKED_AWAY].update(panel.fit("".join(map(rich_cast, left)), title=TITLE_WALKED_AWAY))
    console.print(layout)
