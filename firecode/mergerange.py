def merge_ranges(input_range_list):
    total_range = input_range_list[len(input_range_list) - 1]
    input_range_list.pop()
    for item in input_range_list:
        if item[0] < total_range[0]:
            total_range[0] = item[0]
        if item[1] > total_range[1]:
            total_range[1] = item[1]
    return total_range

in_list = [[1,10], [5,8], [8,15]]
print(merge_ranges(in_list))