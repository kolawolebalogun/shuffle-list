"""
The following method was implemented to shuffle the elements of a list with some restrictions.
Here are the restrictions:
• Elements on the list can move randomly to the left or to the right
• Elements must not move more than one position away from the original one
• The list is non circular.

Input Value = [21, 22, 23, 24, 25, 26, 27, 28]
Output Value: [22, 21, 24, 23, 26, 25, 28, 27]
"""


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


if __name__ == "__main__":
    print(main())
