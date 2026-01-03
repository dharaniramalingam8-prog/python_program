#!/usr/bin/env python3

def is_even(n: int) -> bool:
    return n % 2 == 0


n = int(input("Enter an integer: ").strip())
print(f"{n} is {'even' if is_even(n) else 'odd'}.")

