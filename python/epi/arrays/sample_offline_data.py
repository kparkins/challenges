import random


def sample_data(data, k):
    if len(data) <= k:
        return data
    for i in range(k):
        index = random.randint(i, len(data) - 1)
        data[i], data[index] = data[index], data[i]
    return data
