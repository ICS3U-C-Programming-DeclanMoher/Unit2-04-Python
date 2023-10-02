import math


def main():
    # input
    
    diameter = float(input("diameter: "))

    # process1
    subtotal = diameter * 1.5 + 4.25
    tax = subtotal * 0.13
    total = subtotal + tax

    # output
    print("")
    print("total = {} $".format(total))


if __name__ == "__main__":
    main()
