# def list(lists):
lists = [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b',
        'c', 'd', 'e', 'f', 'g', 'h']
evens = []
odds = []
# chars = []
for value in lists:
    if value % 2 == 0:
                evens.append(value)
    else: 
                odds.append(value)
    # else:
    #             chars.append('others')        
print("evens: ", evens )
print("odds: ", odds)
# print("chars: ", chars)
