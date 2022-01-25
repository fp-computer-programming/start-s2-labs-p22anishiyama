# Author: ATN 1/25/22

def double_every_other(lst):
    for i, v in enumerate(lst):
        # finding each odd item in the list
        if i % 2 != 0:
            # if the item is odd, then i will double its value
            lst[i] *= 2
    return lst