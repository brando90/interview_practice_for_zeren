
def bucket(array):
    '''
    uses buck sort to sort. takes O(n+d)
    '''
    sorted_array = [None]*max(array)
    for element in array:
         sorted_array[element] = element
    remove_nones(sorted_array)
    return sorted_array

def remove_none(array):
    # TODO
    return

'''
if you want to sort array = [5,2,1]
d = max([5,2,1]) return 5
d = max(array) # 5
array = [None, None, None, None, None]
O(d)
array[5] = 5
array[2] = 2
array[1] = 1
O(n)
array = remove_nones(array)
[1,2,5]

only time its good (in theory):

d = O(n)

but if d = 2^n
run in O(n+2^n)=> bad

bucket sort is bad for [1,2,3,2**1000]

~2**1000

vs

~4 log 4

'''
