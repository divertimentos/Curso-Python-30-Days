items3 = ["Mic", "Telefone", 23432.22, 23432.244, "Justin", "Bag", "Detonator", 234]

def my_sum(my_num_list):
    total = 0
    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
    return total

# print(my_sum(items3))

def count_nums(my_num_list):
        total = 0
        for i in my_num_list:
            if isinstance(i, float) or isinstance(i, int):
                total += 1
        return total


def my_avg(my_num_list):
    the_sum = my_sum(my_num_list)
    # num_of_items = len(my_num_list)
    num_of_items = count_nums(my_num_list)
    return the_sum / (num_of_items * 1.0)

print("Average:", my_avg(items3))
