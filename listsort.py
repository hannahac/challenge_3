def list_sort(jumbled_list):
    sorted_dict = {}
    evens = []
    odds = []
    characters = []

    for item in jumbled_list:
        if type(item) == int:
            # these are numbers
            if item % 2 == 0:
                # this is even
                evens.append(item)
            else:
                # this is odd
                odds.append(item)
        if type(item) == str:
            # these are characters
            characters.append(item)
        if type(item) == float:
            # these are floats, just skip them
            # continue
            odds.append(item)
    # end of for loop

    # now do the sorting
    sorted_evens = sorted(evens)
    sorted_odds = sorted(odds)
    sorted_chars = sorted(characters)

    sorted_dict = {
        'evens': sorted_evens,
        'odds': sorted_odds,
        'chars': sorted_chars
    }
    return sorted_dict

unsorted_list = [8.0,'f', 9.0,'o', 2, 76, 0, 'i', 44.7, 'x', 'e',0.9, 5, 33, 0,'g',3.1]
print("before sorting")
print(unsorted_list)
result = list_sort(unsorted_list)
print("after sorting")
print(result)
