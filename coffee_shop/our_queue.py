#  Copyright (c) 2024 Sandy Bultena and Ian Clement.
#
#  This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
#  License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any
#  later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with this program. If not,
#  see <https://www.gnu.org/licenses/>.
from __future__ import annotations
from typing import Iterator, Generic, TypeVar, Optional
from rich.protocol import rich_cast

T = TypeVar("T")


class QueueOverflowError(Exception):
    """Queue overflow error."""
    pass


class QueueUnderflowError(Exception):
    """Queue underflow error."""
    pass


class Queue(Generic[T]):
    """A first-in first-out (FIFO) collection of elements."""

    def __init__(self, elements: Optional[list[T]] = None, maxsize: Optional[int] = None):
        """
        Create a queue
        :param elements:
        :param capacity:
        """
        self._elements: list[T] = [] if elements is None else elements.copy()
        self._cursor: int = 0
        self._capacity: Optional[int] = maxsize

    def put(self, element: T):
        """
        Add an element on the rear of the queue. Precondition: queue not full.
        :param element: The element to add to the queue.
        """
        if self.full():
            raise QueueOverflowError()
        self._elements.append(element)

    def get(self, block=True) -> T:
        """
        Remove the front element of the queue. Precondition: queue not empty.
        :return: The element removed from the queue.
        """
        if self.empty():
            raise QueueUnderflowError()
        return self._elements.pop(0)

    @property
    def not_empty(self):
        return not self.empty()

    # These next two propertie are needed to match the API of the Priority queue
    @property
    def queue(self) -> Queue:
        return self

    @property
    def maxsize(self) -> int:
        return self._capacity
    

    def front(self) -> T:
        """
        Get the front element of the queue. Precondition: queue not empty
        :return:
        """
        if self.empty():
            raise QueueUnderflowError()
        return self._elements[0]

    def empty(self) -> bool:
        """Determine if the queue is empty."""
        return len(self._elements) == 0

    def full(self) -> bool:
        """Determine if the queue is full."""
        if self._capacity is not None:
            return len(self._elements) == self._capacity
        else:
            return False

    def __iter__(self) -> Iterator[int]:
        self._cursor = -1
        return self

    def __next__(self) -> T:
        if self._cursor >= len(self._elements) - 1:
            raise StopIteration
        self._cursor += 1
        return self._elements[self._cursor]

    def __str__(self):
        return f"FRONT --> {self._elements} <-- REAR"



    def __repr__(self):
        if self._capacity is None:
            return f"Queue({repr(self._elements)})"
        else:
            return f"Queue({repr(self._elements)}, {self._capacity})"
