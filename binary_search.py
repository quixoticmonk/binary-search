def binary_search(arr: list, item):
    lower_index = 0
    higher_index = len(arr) - 1

    while lower_index <= higher_index:
        mid_index = lower_index + (higher_index - lower_index) // 2
        mid_value = arr[mid_index]
        if mid_value < item:
            lower_index = mid_index + 1
        elif mid_value > item:
            higher_index = mid_index - 1
        else:
            return mid_index

    return None


print(binary_search([1, 2, 30, 41, 55, 64, 65, 66, 76], 66))
