' ----------------------------------------------------------------------------
' Function match_ends
' Given a list of strings, this function returns the count of the number 
' of strings where the string length is 2 or more and the first and last chars 
' of the string are the same. 
' Note: python does not have a ++ operator, but += works.
' ----------------------------------------------------------------------------
def match_ends(words):
    cnt = 0
    for x in words:
        if len(x) >= 2 and x[0].lower() == x[-1].lower(): cnt += 1
    return cnt

print match_ends(["toto", 'tatat', 'bb', 'a', '', 'kayak'])
print match_ends(["toto", 'tatat', 'bb', 'a', '', 'kayak', 'Kayak'])


' ----------------------------------------------------------------------------
' Function front_x
' Given a list of strings, return a list with the strings in sorted order, 
' except group all the strings that begin with "x" first. Hint: this can be 
' done by making 2 lists and sorting each of them before combining them.
' ----------------------------------------------------------------------------
def front_x(words):
    return  sorted([x.lower() for x in words if x[0].lower() == 'x']) +\
            sorted([x.lower() for x in words if x[0].lower() != 'x'])

print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
print front_x(['mix', 'Xyz', 'xapple', 'xanadu', 'axrdvark'])


' ----------------------------------------------------------------------------
' Function sort_last
' Given a list of non-empty tuples, return a list sorted in increasing order 
' by the last element in each tuple.
' ----------------------------------------------------------------------------
def sort_last(tuples):    
    return sorted(tuples, key=lambda orderfunction: orderfunction[-1] )

print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])


' ----------------------------------------------------------------------------
' Test of the functions above' 
' ----------------------------------------------------------------------------
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)
    
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

main()


' ----------------------------------------------------------------------------
' Function remove_adjacent
' Given a list of numbers, return a list where all adjacent == elements 
' have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. 
' You may create a new list or modify the passed in list.
' ----------------------------------------------------------------------------
def remove_adjacent(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: return remove_adjacent(nums[:i-1]+nums[i:])
    return nums

print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([1, 1, 2, 2, 3])
print remove_adjacent([1, 1, 2, 2, 3, 4, 4])


' ----------------------------------------------------------------------------
' Function linear_merge
' Given two lists sorted in increasing order, create and return a merged list 
' of all the elements in sorted order. You may modify the passed in lists. 
' Ideally, the solution should work in "linear" time, making a single pass of 
' both lists.
' ----------------------------------------------------------------------------
def linear_merge(list1, list2):
    
    if list1 == []: return list2
    if list2 == []: return list1
        
    if list1[0] <= list2[0]: return [list1[0]] + linear_merge(list1[1:], list2)    
    return [list2[0]] + linear_merge(list1, list2[1:])


' ----------------------------------------------------------------------------
' Test of the functions above' 
' ----------------------------------------------------------------------------
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()


' ----------------------------------------------------------------------------
' Function donuts
' Given an int count of a number of donuts, return a string of the form 
' Number of donuts: , where is the number passed in. However, if the count 
' is 10 or more, then use the word many instead of the actual count.
' ----------------------------------------------------------------------------
def donuts(count):
    return 'Number of donuts: ' + (str(count) if count<10 else 'many')

print donuts(5)
print donuts(23)


' ----------------------------------------------------------------------------
' Function both_ends
' Given a string s, return a string made of the first 2 and the last 2 chars
' of the original string, so spring yields spng. However, if the string 
' length is less than 2, return instead the empty string.
' ----------------------------------------------------------------------------
def both_ends(s):
    return (s[:2] + s[-2:] if len(s)>=2 else '')


' ----------------------------------------------------------------------------
' Function fix_start
' Given a string s, return a string where all occurences of its first char 
' have been changed to *, except do not change the first char itself.
' e.g. babble yields ba**le
' Assume that the string is length 1 or more. 
' Hint: s.replace(stra, strb) returns a version of string s where all 
' instances of stra have been replaced by strb.
' ----------------------------------------------------------------------------
def fix_start(s):
    return s[0] + s[1:].replace(s[0], '*')
    

' ----------------------------------------------------------------------------
' Function MixUp
' Given strings a and b, return a single string with a and b separated by 
' a space <a> <b>, except swap the first 2 chars of each string.
' e.g. mix, pod -> pox mid
' dog, dinner -> dig donner
' Assume a and b are length 2 or more.
' ----------------------------------------------------------------------------
def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


' ----------------------------------------------------------------------------
' Test of the functions above' 
' ----------------------------------------------------------------------------
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)


def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

main()



' ----------------------------------------------------------------------------
' Function verbing
' Given a string, if its length is at least 3, add ing to its end. 
' Unless it already ends in ing, in which case add ly instead. If the string
' length is less than 3, leave it unchanged. Return the resulting string.
' ----------------------------------------------------------------------------
def verbing(s):
    return (s if len(s)<3 else s+'ly' if s[-3:] == 'ing' else s+'ing')


' ----------------------------------------------------------------------------
' Function not_bad
' Given a string, find the first appearance of the substring not and bad. 
' If the bad follows the not, replace the whole not...bad substring with good.
' Return the resulting string.
' So This dinner is not that bad! yields: This dinner is good!
' ----------------------------------------------------------------------------
def not_bad(s):
    if -1 < s.find('not') < s.find('bad'): 
        return not_bad(s[:s.find('not')] + 'good' + s[s.find('bad')+3:])
    return s


' ----------------------------------------------------------------------------
' Function front_back
' Consider dividing a string into two halves. If the length is even, the 
' front and back halves are the same length. If the length is odd, we will 
' say that the extra char goes in the front half.
' e.g. abcde, the front half is abc, the back half de.
' Given 2 strings, a and b, return a string of the form 
' a-front + b-front + a-back + b-back
' ----------------------------------------------------------------------------
def front_back(a, b):
    m_a = (len(a)+1)/2
    m_b = (len(b)+1)/2
    return a[:m_a] + b[:m_b] + a[m_a:] + b[m_b:]


' ----------------------------------------------------------------------------
' Test of the functions above' 
' ----------------------------------------------------------------------------
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')
    
main()




