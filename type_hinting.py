from typing import List


# we can hint the type of value we are passing as argument
def list_avg(my_list: List) -> float:
    return sum(my_list) / len(my_list)


print(list_avg([1, 2, 3]))
