import sys


def sort(my_arr):
    result = []
    for i in my_arr:
        if i == 0:
            result.append(i)
    for i in my_arr:
        if i == 1:
            result.append(i)
    for i in my_arr:
        if i == 2:
            result.append(i)

    return result


if __name__ == '__main__':
    arr = sys.argv[1].split(',')
    new_arr = []
    for i in arr:
        new_arr.append(int(i))
    print(f"Provided Array: {new_arr}")
    print(f"Outcome of a sort function: {sort(new_arr)}")
