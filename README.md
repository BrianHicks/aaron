# Aaron

[![Build Status](https://secure.travis-ci.org/BrianHicks/aaron.png)](http://travis-ci.org/BrianHicks/aaron)

Aaron adds some syntactic sugar to Python function composition.

## How?

Say you have the following functions:

```python
def add_one(n):
    return n + 1

def double(n):
    return n * 2

def ints_less_than(n):
    return range(1,n)

def product(*ns):
    result = 1
    for n in ns:
        result *= n

    return result
```

You could do something like this:

```python
def two_n_plus_one(n):
  return add_one(double(n))

def product_of_lesser_numbers(n):
  return product(*ints_less_than(n))
```

Or, you could use Aaron, decorate your functions with `composable`, and do this:

```python
two_n_plus_one = double > add_one

product_of_lesser_numbers = ints_less_than >> product
```

## Aaron? What?

Yeah, the [composer](http://en.wikipedia.org/wiki/Aaron_Copland). Get it?
