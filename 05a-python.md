# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are both sequences of values that can be any type, but tuples are immutable and lists are not.  Tuples can be keys because of their immutability.  Changing a key after it has been assigned a value will cause unpredictable outcomes when the dictionary looks it up in its hashtable.  So lists cannot be keys, because they are mutable and thus not hashable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists both have lengths and they both support the constructs: "x in (set/list) or "for x in (set/list)." One key difference is that lists are ordered sequences, while sets are unordered collections, which means they don't support slicing, nor do they record element position or order of insertion.  Therefore, it's generally harder to find an element of a set than it is for a list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is an "anonymous" function, which is designed to be executed during runtime.  Python's lambda can be used when sorting, in order to tell which part of a tuple to use for sorting a list.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a way to create a list by specifying a logic for generating the members and a range. For example: 

```
new_list = [x**3 for x in range(1,3)]

[1, 8]

```

>>The map() function would look very similar, but would require a lambda: 

```

map(lambda x: x**3, x in range(1,3))

```

>>Map functions are useful because you can take any iterable and apply a function to it in order to generate a new iterable.

>>The filter() function would correspond to adding an 'if' statement to a list comprehension.  It takes in a boolean function and list and spits out the elements in the list that leave it true.

>>Here's an example of finding the even numbers of the beginnign of the fibonacci sequence:

```

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)

```

>>Dictionary comprehensions can do basically the same thing as a list comprehension, but it will create a dictionary, with the inputs as keys.  Here's an example:

```

D = {x: x**2 for x in [1,2,3,4,5]}

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

```

>>Set comprehensions do pretty much the same thing as list comprehensions except that they can take sets as inputs--sequence doesn't matter.  Set comprehensions are useful for filtering out repeat values, such as the one below:

```

names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]

{ name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }

{ 'Bob', 'John', 'Alice' }

---

```

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> a) 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> b) 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> c) 7850  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





