
def getNumberGroup(num: int):
    return (num.bit_length() - 1) % 2


if __name__ == "__main__":

    number = input("Please enter a number: ")
    print("The gropup for this number is: " + str(getNumberGroup(int(number))))

    