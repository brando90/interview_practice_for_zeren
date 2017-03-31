'''
Q: Remove duplicates from linked list.

but solve the problem you need to know something...so ask.

Interviewer has to:
1) Give you the API (= interfence for talking to someone else's software) himself
(if he doesn't use the standard library API, he might have a specific question
with specific restrictions)
2) Use a standard API from python
- http://pythonhosted.org/llist/
- https://pypi.python.org/pypi/llist/
3) Implement your own linked list and use.

'''

from llist import dllist, dllistnode

# if linked_list.first == None:
#     print('1')
# elif linked_list.first.next == None: # to guarantee the it doesn't crash n the definition of prev_node
#     print('2')
# elif linked_list.first.next == None: # to guarantee the it doesn't crash n the definition of prev_node
#     print('3')
# elif linked_list.first.next == None: # to guarantee the it doesn't crash n the definition of prev_node
#     print('3')
# elif linked_list.first.next == None: # to guarantee the it doesn't crash n the definition of prev_node
#     print('4')
# else:
#     print('5')

def remove_duplicates_linked_list(linked_list):
    '''
    returns linked list without duplicates
    '''
    #TODO
    return

def remove_duplicates_linked_list_with_hash_tables2(linked_list):
    '''
    returns linked list without duplicates.

    O(n)
    '''
    # if the linked list is empty, return the empty linked list
    if linked_list.first == None:
        return linked_list
    elif linked_list.first.next == None: # to guarantee the it doesn't crash n the definition of prev_node
        return linked_list
    # start removing duplicates
    #head = linked_list.first # conceptually return
    head = linked_list
    prev_node = linked_list.first
    current_node = linked_list.first.next # this will not crash cuz its not None
    memory = {prev_node.value:True}
    while current_node != None:
        if not has_been_seen(value,memory): # if current value has not been seen, remember it, else do nothing cuz we can ignore duplicates.
            memory[current_node.value] = True
            prev_node = current_node
            current_node = current_node.next
        else: # we have duplicate
            # so we remove it
            # to not point to deleted note, have, prev_node = prev_node
            current_node = current_node.next
    return head

def has_been_seen(value,memory):
    return (current_node.value in memory)

def remove_duplicates_linked_list_with_hash_tables(linked_list):
    '''
    returns linked list without duplicates.

    O(n)
    '''
    # removes duplicates
    d = {}
    for element in linked_list:
        if not element in d:
            d[element] = True
        #else: # this is only ran if its there
        #    pass
    # creates the linked list again
    unique_linked_list = create_linked_list1(d)
    return unique_linked_list

def create_linked_list(d):
    unique_linked_list = dllist( d.keys() )
    return unique_linked_list

##

def test_remains_the_same():
    '''
    tests that a llist with no duplicates remains the same
    '''
    array = [1, 2, 3]
    lst = dllist(array) # creates a linked list with array as elements
    lst_new = remove_duplicates_linked_list(lst)
    print('Are the two list the same? ', lst_new == lst) # this should return true, when the lists are the same.
    print('lst_new: ', lst_new)
    print('lst: ', lst)
    if lst_new == lst:
        print('TEST 1 PASS')

def test_delete_duplicates():
    '''
    tests that duplicates are removed.
    '''
    array = [1, 2, 2, 2, 2, 3]
    lst = dllist(array) # creates a linked list with array as elements
    lst_new = remove_duplicates_linked_list(lst)
    print('Are the two list the same? ', lst_new == dllist([1, 2, 3]) ) # this should return true, when the lists are the same.
    print('lst_new: ', lst_new)
    if lst_new == dllist([1, 2, 3]):
        print('TEST 2 PASS')


test_remains_the_same()
test_delete_duplicates()
