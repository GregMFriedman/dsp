# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
    if count >= 10:
        count = 'many'
    return 'Number of donuts: ' + str(count)



##print donuts(4)
##print 'Number of donuts: 4'
##print donuts(9)
##print 'Number of donuts: 9'
##print donuts(10)
##print 'Number of donuts: many'
##print donuts(99)
##print 'Number of donuts: many'
    
def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    """
    if len(s) < 2:
        return ""
    start = s[0:2]
    end = s[-2:]
    return start + end

    
##print both_ends('spring')
##print 'spng'
##print both_ends('Hello')
##print 'Helo'
##print both_ends('a')
##print ''
##print both_ends('xyz')
##print 'xyyz'

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    
    """
    start = s[0]
    end = s[1:]
    if end.rfind(start) == -1:
        return s
    for c in range(len(end)):
        if end[c] == start:
            new_end = end.replace(end[c], '*')
    return start + new_end

##print fix_start('babble')
##print 'ba**le'
##print fix_start('aardvark')
##print 'a*rdv*rk'
##print fix_start('google')
##print 'goo*le'
##print fix_start('donut')
##print 'donut'

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    """
    return a.replace(a[:2], b[:2], 1) + " " + b.replace(b[:2], a[:2], 1)
    
##print mix_up('mix', 'pod')
##print 'pox mid'
##print mix_up('dog', 'dinner')
##print 'dig donner'
##print mix_up('gnash', 'sport')
##print 'spash gnort'
##print mix_up('pezzy', 'firm')
##print 'fizzy perm'

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    
    """
    if len(s) < 3:
        return s
    elif s[-3:] == 'ing':
        return s + 'ly'
    else:
        return s + 'ing'

##print verbing('hail')
##print 'hailing'
##print verbing('swiming')
##print 'swimingly'
##print verbing('do')
##print 'do'

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    """
    start = s.rfind('not')
    if start == -1:
        return s
    if s[start:].find('bad') == -1:
        return s
    end = s.find('bad') + 3
    return s.replace(s[start:end], 'good')
    


##print not_bad('This movie is not so bad')
##print 'This movie is good'
##print not_bad('This dinner is not that bad!')
##print 'This dinner is good!'
##print not_bad('This tea is not hot')
##print 'This tea is not hot'
##print not_bad("It's bad yet not")
##print "It's bad yet not"


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    """
    if len(a) % 2 == 0:
        afront = a[:len(a)/2]
        aback = a[len(a)/2:]
    else:
        afront = a[:1 + len(a)/2]
        aback = a[1 + len(a)/2:]
        
    if len(b) % 2 == 0:
        bfront = b[:len(b)/2]
        bback = b[len(b)/2:]
    else:
        bfront = b[:1 + len(b)/2]
        bback = b[1 + len(b)/2:]
    return afront + bfront + aback + bback

    
##print front_back('abcd', 'xy')
##print 'abxcdy'
##print front_back('abcde', 'xyz')
##print 'abcxydez'
##print front_back('Kitten', 'Donut')
##print 'KitDontenut'
