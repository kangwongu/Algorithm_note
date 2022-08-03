num_arr = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max = array[0];
    for i in array:
        if i > max:
            max = i;
    return max


result = find_max_num(num_arr)
print(result)
