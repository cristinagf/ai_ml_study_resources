# Python

Common commands, snippets.

## Operations
`//`  Floor division

`**` exponential


## Lambdas
Small anonymous functions using on the fly-arguments

```python
x = lambda a: a +10
print(x(5))     
```
Returns 15


## String
arrays that don't allow index assignation

`''.join(reversed(s))`    Reverse string

`for char in string.ascii_lowercase:`  All letters

### Map set of characters into a new map

```python
valid_characters = 'abc'
shifted_characters = 'abf'
trans_map = str.maketrans(valid_characters, shifted_characters)
translated_string = list(s.lower().translate(trans_map))
```

## Lists 

`for i in range(3,6):`  list 3,4,5

`zeros = [0] * 3`  Array of 3 zeros

`for i,c in enumerate('str'):`  For index,val in enumerate(my_list)

`def func_a(a: List[int]) -> int:`  from typing import List

### Sorting Lists

in place, modify data
`list.sort(key = lambda a: a[1], reverse=True)`  Sort tuple-array by input[1]
Uses Timsort algorithm, with a runtime complexity O(n logn).


return new structure
`sorted(list, key = lambda a: a[1], reverse=True)` O(n log n)

### Search in Lists

`list.index(elementSearched, start, end)` Returns index of first occurrence

### Remove last element
`list.pop()`  Return and remove last element

`index = np.where(arr==specified_index)`

## Dictionaries

`sorted(dict.items())`  Returns a sorted list

## Classes

```python
class X:
    def __init__(sef, a:str, b:int):
        self.a = a //atribute
        self.b = b
    def methodA():
        print('-')

instance_X = X('A', 4)
```

# Common useful commands
`isalnum()` method returns True if all the characters are alphanumeric



# Math
circle
diameter = 2r
circumference = 2 pi r
area = pi r^2
arc-len = thetao/360 2pi r
sector-area = theta/360 pi r^2
pi = 180
x^2 + y^2 = r^2
