def test_input(low, high, test):
    while True:
        try:
            if int(low) <= int(test) <= int(high):
                break
            else:
                test = input("number must be in " + low + "-" + high + " range, please try again")
        except ValueError:
            test = input("please enter a number")
    return test