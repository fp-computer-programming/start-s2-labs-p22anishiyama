# Author: ATN 1/25/22

def comes_after(st, l):
    # creating an empty list for the result to be stored 
    chars = []
    for i in range(len(st) - 1):
        # if the item is equal to the letter specified and is not a number or special symbol, add it to the list
        if st.lower()[i] == l.lower() and not st[i+1].isnumeric() and st[i+1].isalnum():
            chars.append(st[i+1])
    # the list will be translated into a string in order to print for the user
    return ''.join(chars)
    