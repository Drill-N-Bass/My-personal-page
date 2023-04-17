# production = True
local_dev = False

x = None
try:
    if production == True:
        x = False 
    if production == False:
        x = True
except NameError:
    if local_dev == True:
        x = False
    if local_dev == False:
        x = True
print(x)