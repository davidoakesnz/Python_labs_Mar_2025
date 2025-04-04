#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines several ADVANCED calculator features
"""
    Advanced Calculator functions including mod, power and sqrt
"""
import sys
def mod(x, z):
    """ Return REMAINDER after x is divided by z """
    return x % z

def power(x, z):
    """ Return x to the power of z """
    return x**z

def sqrt(x):
    """ Return SQUARE ROOT of x """
    return x**0.5

def main():
    print("..............ADVANCED Calculator.............")
    print(f"100 % 30 = {mod(100, 30)}")
    print(f"12 ** 2 = {power(12, 2)}")
    print(f"\N{square root}25 = {sqrt(25)}")
    return None

# Namspace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # Ignore if imported as a module
    main()
    sys.exit(0)