def StarterFinder(d): #GTP nin yalancısıyım valla
    unique_pairs = set()
    pairs = set()
    for key, value in d.items():
        for pair in value:
            if pair in pairs:
                unique_pairs.discard(pair)
            else:
                pairs.add(pair)
                unique_pairs.add(pair)
    unique_keys = set()
    for key, value in d.items():
        for pair in value:
            if pair in unique_pairs:
                unique_keys.add(key)
    print(f"starting options are:    {unique_keys}\nwe will start with the first one")
    return tuple(unique_keys)

d = {'A': (('A', 'B'), ('A', 'D')), 'B': (('A', 'B'), ('B', 'C')), 'C': (('B', 'C'), ('C', 'E')), 'D': (('A', 'D'), ('B', 'D')), 'E': (('C', 'E'), ('E', 'F')), 'F': (('E', 'F'), ('C', 'F'))}
print(StarterFinder(d))
