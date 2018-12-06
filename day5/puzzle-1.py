import copy
with open('day-5-input') as f:
    data = f.readline()

data_copy = copy.deepcopy(data)

def will_react(a, b):
    if a == b:
        return False
    return (a.upper() == b) or (a.lower() == b)

deleted_chars = 0
idx = 0

while idx <  (len(data) - deleted_chars-1):
    print(idx, end='->')
    if  idx < (len(data) - deleted_chars):
        if will_react(data_copy[idx],data_copy[idx+1]):
            data_copy = data_copy[:idx] + data_copy[idx+2:]
            if idx > 2:
                idx -= 3
            else:
                idx = -1
            deleted_chars +=2
    idx+=1


print(len(data_copy))
