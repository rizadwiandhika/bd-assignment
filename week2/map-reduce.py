import json
from itertools import groupby;

def mapFunction(word):
    cleanword = ''.join([i for i in word if i.isalpha()])
    return [cleanword, 1]

def reduceFunction(key, values):
    return [key, sum(map(lambda x: x[1], values))]


def main():
    with open('data.txt', 'r') as f:
        words = [word for line in f for word in line.split()]

    mapResult = map(mapFunction, words)
    mapResult = sorted(mapResult, key=lambda x: x[0])

    result = []
    for k, g in groupby(mapResult, key=lambda x: x[0]):
        result.append(reduceFunction(k, g))

    print(result)


if __name__ == '__main__':
    main()