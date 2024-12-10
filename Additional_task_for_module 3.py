def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, int):
        return data
    elif isinstance(data, str):
        return len(data)
    else:
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    total_sum += calculate_structure_sum(key) + calculate_structure_sum(value)
            else: total_sum += calculate_structure_sum(item)
        return total_sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)