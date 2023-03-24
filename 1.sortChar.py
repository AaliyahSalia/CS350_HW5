# Write a function/method to sort char type elements in stack by ONLY temporary
# stack (shown in the example programs) or one variable without using list. For
# example, given a stack stk, the result should be as follows after calling srt(stk)

def sort_stack(stk):
    temp_stk = []
    while stk:
        temp = stk.pop()
        while temp_stk and temp_stk[-1] > temp:
            stk.append(temp_stk.pop())
        temp_stk.append(temp)
    while temp_stk:
        stk.append(temp_stk.pop())

stk = ['t', 'r', 'o', 's']
print("Unsorted Stack: ", stk)

sort_stack(stk)
print("Sorted Stack: ", stk)

