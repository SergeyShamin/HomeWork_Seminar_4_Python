def input_number_test(text):

    int_test = True
    is_minus = False
    while int_test: 
        coord = input(f"{text}")
        if coord[0] == '-':
            is_minus = True
            coord = coord.replace("-", "")
        if coord.isdigit():
            coord = int(coord)
            if is_minus:
                coord *= -1
            int_test = False
        else:
            print("Not a number, try again")
    return coord