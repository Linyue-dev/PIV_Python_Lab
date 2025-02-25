# Review Questions 1

## Dictionaries: prefixes

A *prefix* is a substring of a word from the start of that word. For example, the prefixes of the word "ant" are: "a", "an" and "ant". Yes, a word is a prefix of itself&#x2026;

Code a function `prefixes(..)` whose input is a list of words. The function will count up all the different the word prefixes in the list and return a dictionary with these counts. For example, calling this method on the list:

```python
[ "abc", "ca", "cab" ]
```

will return this dictionary:

```python
{ "ca": 2, "abc": 1, "ab": 1, "cab": 1, "a": 1, "c": 2 }
```


## Dictionaries: pets

Ian has a file with all his pets arranged by species. But, Ian wants to go on vacation and needs to
prepare care notes for each pet by their name not their species.

Write a function that takes in a dictionary where the key=species, and the value is a list of pet names and returns another dictionary of pets (key=name, value=species). Raise an error if you encounter any issues with converting.

For example, the input:

```python
{ RAT: ["Lydian", "Elvira"], GUINEA_PIG: ["Egon"], TARANTULA: ["Freddie", "Katrina"] }
```

will be:

```python
{ "Egon": GUINEA_PIG, "Elvira": RAT, "Freddie": TARANTULA,
      "Lydian": RAT, "Katrina": TARANTULA } 
```

## Sets

Here's a function takes two `list` and returns a `list` containing all the elements either `l1` or in `l2` with no duplicates. The function only works if `l1` and `l2` do not contain duplicates themselves. 

For example, `all_elements([3,2,7,4], [1,2,3])` returns the list `[3,7,2,4,1]`. The order of the elements in the list doesn't matter.

```python
def all_elements(l1: list, l2: list) -> list:

    results: list = []

    for x in l1:
        results.append(x)
        
    for x in l2:
        found: bool = False
        for y in l1:
            if x == y:
                found = True
                break
        if not found:
            results.append(x)

    return results
```

Re-write this function using a `set` to efficiently construct the `list`.  Does your function work if `l1` and `l2` contain duplicates?
