#!/usr/bin/env python
import time


def main():
    num = 1
    while True:
        print(f"Processing {num}")
        time.sleep(0.1)
        num += 1


if __name__ == "__main__":
    main()
