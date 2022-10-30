def sorted_numbers(sorted_num):
    sorted_num.sort
    for sorted_num in number:
        sort_list.append(sorted_num)
    return sort_list


number = [int(sorted_num) for sorted_num in input().split()]
sort_list = list()

print(sorted(number))