def faktoryelalacamzorundayim (x):
    if x == 0:
        return 1
    elif isinstance(x , int):
        return x * faktoryelalacamzorundayim(x-1)
    else:
        return "int gir"

print(faktoryelalacamzorundayim())


