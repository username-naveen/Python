# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    eng = int(raw_input())
    eng_s = list(map(int, raw_input().strip().split()))[:eng]
    fre = int(raw_input())
    fre_s = list(map(int, raw_input().strip().split()))[:fre]
    
    print(len(set(eng_s).difference(set(fre_s)))) 
    
    
#     .difference()
# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

# >>> s = set("Hacker")
# >>> print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(['R', 'a', 'n', 'k'])
# set(['c', 'r', 'e', 'H'])

# >>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

# >>> print s.difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])

# >>> s - set("Rank")
# set(['H', 'c', 'r', 'e'])


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    eng = int(raw_input())
    eng_s = list(map(int, raw_input().strip().split()))[:eng]
    fre = int(raw_input())
    fre_s = list(map(int, raw_input().strip().split()))[:fre]
    
    print(len(set(eng_s).symmetric_difference(set(fre_s)))) 
    
# .symmetric_difference()
# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).

# >>> s = set("Hacker")
# >>> print s.symmetric_difference("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

# >>> print s.symmetric_difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

# >>> s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])