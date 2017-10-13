def 함수():
    pairs = [(1, 'one','D'), (2, 'two','C'), (3, 'three','B'), (4, 'four','A')]
    pairs.sort(key=lambda pair: pair[0])
    return pairs

print(함수())