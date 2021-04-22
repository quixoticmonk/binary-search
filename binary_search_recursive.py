def binary_search_2(arr: list, item, start, end):
    lower_index = start
    higher_index = end-1

    while lower_index <= higher_index:
        mid_index = lower_index + (higher_index - lower_index) // 2
        mid_value = arr[mid_index]

        if mid_value == item:
            return mid_index
        elif mid_value > item:
            return binary_search_2(arr, item, 0, mid_index)
        elif mid_value < item:
            return binary_search_2(arr, item, mid_index + 1, higher_index+1)

    return None


print(binary_search_2([1, 2, 30, 41, 55, 64, 65, 66, 76], 66, 0, 9))
