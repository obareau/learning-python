def find_average(values) -> float:
    result = 0
    for v in values:
        result += v
    return result / len(values)


print("average", find_average([5, 6, 7, 8]))

