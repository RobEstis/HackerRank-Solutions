#!/usr/bin/env python3
"""
HackerRank Problem: Designer Door Mat

Print a door mat pattern of size N x M where:
- N is an odd natural number
- M = 3 * N
- Pattern uses only '.', '|', and '-'
- 'WELCOME' appears centered on the middle row
"""


def designer_door_mat(n: int, m: int) -> None:
    # Top half
    for i in range(n // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))

    # Middle row
    print("WELCOME".center(m, "-"))

    # Bottom half (mirror)
    for i in range(n // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))


def main() -> None:
    n, m = map(int, input().split())
    designer_door_mat(n, m)


if __name__ == "__main__":
    main()
