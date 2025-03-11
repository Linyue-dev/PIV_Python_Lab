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
from typing import Generic, TypeVar, Iterator, Optional


class StackOverflowError(Exception):
    """Stack overflow error."""
    pass


class StackUnderflowError(Exception):
    """Stack underflow error."""
    pass


T = TypeVar("T")


class Stack(Generic[T]):
    """A last-in first-out (LIFO) collection of elements."""

    def __init__(self, elements: Optional[list[T]] = None, capacity: Optional[int] = None):
        """
        Create a stack.
        :param elements:
        :param capacity:
        """
        self._elements: list[T] = [] if elements is None else elements.copy()
        self._cursor: int = 0
        self._capacity: Optional[int] = capacity

    def push(self, element: T):
        """
        Add an element on the top of the stack. Precondition: stack not full.
        :param element: The element to add to the stack.
        """
        if self.is_full():
            raise StackOverflowError()
        self._elements.append(element)

    def pop(self) -> T:
        """
        Remove the topmost element of the stack. Precondition: stack not empty.
        :return: The element removed from the stack.
        """
        if self.is_empty():
            raise StackUnderflowError()
        return self._elements.pop()

    def top(self) -> T:
        """
        Get the topmost element of the stack. Precondition: stack not empty
        :return:
        """
        if self.is_empty():
            raise StackUnderflowError()
        return self._elements[len(self._elements) - 1]

    def is_empty(self) -> bool:
        """Determine if the stack is empty."""
        return len(self._elements) == 0

    def is_full(self) -> bool:
        """Determine if the stack is full."""
        if self._capacity is not None:
            return len(self._elements) == self._capacity
        else:
            return False

    def __iter__(self) -> Iterator[T]:
        self._cursor = len(self._elements)
        return self

    # not 100% sure if this is supposed to return something, or what
    # I think it returns some kind of 'Reverse' Object
    def __reversed__(self):
        new_stack: Stack = Stack(self._capacity)
        for i in self:
            new_stack.push(i)
        return new_stack

    def reverse(self) -> Stack:
        new_stack: Stack = reversed(self)
        self._elements = new_stack._elements
        return self

    def __next__(self) -> T:
        if self._cursor == 0:
            raise StopIteration
        self._cursor -= 1
        return self._elements[self._cursor]

    def __str__(self):
        return f"{self._elements} <-- TOP"

    def __repr__(self):
        if self._capacity is None:
            return f"Stack({repr(self._elements)})"
        else:
            return f"Stack({repr(self._elements)}, {self._capacity})"
