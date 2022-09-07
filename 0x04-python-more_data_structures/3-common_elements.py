#!/usr/bin/python3

def common_elements(set_1, set_2):
    return [s for s in set([i for i in set_1 for j in set_2 if i == j])]

print(common_elements({'java', 'gr', 'c'}, {'iu', 'c', 'op', 'c'}))
