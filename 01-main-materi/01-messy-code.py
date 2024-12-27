# messy code

def process_data(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2)
        else:
            result.append(item * 3)
    return result

data = [1, 2, 3, 4, 5]
print(process_data(data))
