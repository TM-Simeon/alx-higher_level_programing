#!/usr/bin/python3
# find the peak in a list of unsorted integers
def find_peak(list_of_integers):
    r = list_of_numbers
    for k in range(len(r)-2):
        k += 1
        if(r[k] >= r[k-1] and r[k] >= r[k+1]):
            return r[k]
            break
        else:
            return None
