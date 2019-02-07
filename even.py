#check if number is even
def number(itemz):
 
        if isinstance(itemz, int):
            if itemz % 2 == 0:
                return ('true')
        return('False')    

itemz = 88
print(number(itemz)) 

