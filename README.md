# Shuffle List with restrictions

The following method was implemented to shuffle the elements of a list with some restrictions.
Here are the restrictions:
* Elements on the list can move randomly to the left or to the right
* Elements must not move more than one position away from the original one
* The list is non circular.

```
Input Value = [21, 22, 23, 24, 25, 26, 27, 28]
Output Value: [22, 21, 24, 23, 26, 25, 28, 27]
```

## Requirement

This code has been tested in the following environments

* Python (3.6)

## Process
For this I created 2 solutions:

### Solution 1
Solution one is an approach that doesnt always return the desired result but adheres to all the restrictions

```python
def main():
    ids_list = [21, 22, 23, 24, 25, 26, 27, 28]
    # Possible positions element can move
    position = [-1, 1]
    # Shuffled List Initialization
    shuffled_list = []

    while len(ids_list):
        # Randomly pick the element to shift
        # Move the element to a random index of shift 1
        random_movement = random.randrange(0, len(position), 1)
        new_position = position[random_movement]

        # Pop element from the list,
        # Since restriction say the element can move,
        # Means the element doesnt need to necessarily move
        # To be sure we are not going to pop an element with a negative index
        # we do a logical testing and set to 0 if we have a negative value
        pop_element = 0 if position[random_movement] != -1 else 1

        # Pop element from list
        new_value = ids_list.pop(pop_element)

        # Insert element to new position to ensure we not inserting
        # element in a negative position we use the abs() function
        # to set it to a positive integer
        ids_list.insert(abs(new_position), new_value)

        # Shuffling one of the first to element will affect the
        # next element to be shuffle, so it safe to take out the first two element
        # and equate the list to a offset 2 split of itself
        shuffled_list += ids_list[0:2]
        ids_list = ids_list[2:]

        # Iterate this process until list is empty

    return shuffled_list
```


### Solution 1
Solution one is an approach that doesnt always returns the desired result
```python
def main():
    ids_list = [21, 22, 23, 24, 25, 26, 27, 28]
    # Shuffled List Initialization
    shuffled_list = []

    while len(ids_list):
        # Move second element to first index, which
        # shifts the first element to the second index
        new_value = ids_list.pop(1)
        ids_list.insert(0, new_value)

        # With the above the first and second element have a shift already
        # It safe to take them out the list and equate the list to a offset 2 split of itself
        shuffled_list += ids_list[0:2]
        ids_list = ids_list[2:]

        # Iterate this process until list is empty
    return shuffled_list
```