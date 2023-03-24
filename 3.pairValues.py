# Given a stack saving a group of int type values from the bottom to the top, find
# whether or not there exist pair values in consecutive sequence for all elements by a
# program and print these pairs. For instance, two stacks are as follows

stack_input = input("Enter the stack values separated by spaces: ")
stack = [int(x) for x in stack_input.split()]
consecutive_pairs_exist = False

for i in range(len(stack)-1):
    for j in range(i+1, len(stack)):
        if stack[i] == stack[j] + (j-i):
            print(f"({stack[j]}, {stack[i]})")
            consecutive_pairs_exist = True
    if consecutive_pairs_exist:
        break

if consecutive_pairs_exist:
    print('yes')
else:
    print('no')
