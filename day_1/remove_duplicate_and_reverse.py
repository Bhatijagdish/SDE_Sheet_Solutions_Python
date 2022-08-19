import sys


def remove_duplicate_and_reverse(input_string):
    isReverse = False
    from_left = 0
    from_right = len(input_string) - 1
    while from_left <= from_right:
        if not isReverse:
            if input_string.count(input_string[from_left]) > 1:
                input_string = input_string[:from_left]+input_string[from_left+1:]
                from_right -= 1
                isReverse = True
            else:
                from_left += 1
        else:
            if input_string.count(input_string[from_right]) > 1:
                input_string = input_string[:from_right]+input_string[from_right+1:]
                from_right -= 1
                isReverse = False
                from_left = 0
            else:
                from_right -= 1

    return input_string


if __name__ == '__main__':
    check_string = str(sys.argv[1])
    print(f"OUTPUT STRING: {remove_duplicate_and_reverse(check_string)}")


