def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    """
    count = 0
    for word in words:
        if (len(word) > 1):
            if (word[0] == word[-1]):
                count += 1
    return count


##print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
##print 3
##print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
##print 2
##print match_ends(['aaa', 'be', 'abc', 'hello'])
##print 1

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    """
    sort = sorted(words)
    index = 0
    for word in sort[:]:
        if word[0] == 'x':
            sort.insert(index, sort.pop(sort.index(word)))
            index += 1
    return sort
    

##print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
##print ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
##print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
##print ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
##print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
##print ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    """
    index = 9
    ordered = []
    while index > -1:
        for group in tuples[:]:
            if group[len(group)-1] == index:
                ordered.insert(0, group)
        index += -1
    return ordered
        

##print sort_last([(1, 3), (3, 2), (2, 1)])
##print [(2, 1), (3, 2), (1, 3)]
##print sort_last([(2, 3), (1, 2), (3, 1)])
##print [(3, 1), (1, 2), (2, 3)]
##print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
##print [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    """
    if len(nums) < 1:
        return []
    uniques = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            uniques.append(nums[i])
    return uniques
            
        

##print remove_adjacent([1, 2, 2, 3])
##print [1, 2, 3]
##print remove_adjacent([2, 2, 3, 3, 3])
##print [2, 3]
##print remove_adjacent([3, 2, 3, 3, 3])
##print [3, 2, 3]
##print remove_adjacent([])
##print []

def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    """
    merge = []
    while (len(list1) & len(list2)):
        if list1[-1] > list2[-1]:
            merge.append(list1.pop())
        else:
            merge.append(list2.pop())
    merge += (list1 + list2)[::-1]
    merge.reverse()
    return merge

##print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
##print ['aa', 'bb', 'cc', 'xx', 'zz']
##print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
##print ['aa', 'bb', 'cc', 'xx', 'zz']
##print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
##print ['aa', 'aa', 'aa', 'bb', 'bb']
