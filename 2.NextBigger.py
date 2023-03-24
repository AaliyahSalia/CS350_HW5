# Assuming that there is a series of int type values in stack, such as
# stck ->"5 3 2 10 6 8 1 4 12 7 4", write a program to get next bigger value for each
# element ONLY using stack allowed operations, like 5->10, 3->10, 2->10, 10->12,
# 6->8, 8->12, 1->4, 4->12, 12->none, 7->none, 4->none

def next_bigger_value(stk):
    result = {}
    temp_stk = []
    while stk:
        current = stk.pop()
        while temp_stk and current > temp_stk[-1]:
            temp_stk.pop()
        if temp_stk:
            result[current] = temp_stk[-1]
        else:
            result[current] = None
        temp_stk.append(current)
    while temp_stk:
        result[temp_stk.pop()] = None 
    return result

stk = [5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4]

result = next_bigger_value(stk)

for key, value in result.items():
    print(f"{key} -> {value}, ", end=" ")



