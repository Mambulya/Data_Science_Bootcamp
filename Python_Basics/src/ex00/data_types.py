def data_types():
    v1 = 1
    v2 = "python"
    v3 = 1.03
    v4 = True
    v5 = []
    v6 = dict()
    v7 = tuple()
    v8 = set()

    types = []
    types.append(type(v1).__name__)
    types.append(type(v2).__name__)
    types.append(type(v3).__name__)
    types.append(type(v4).__name__)
    types.append(type(v5).__name__)
    types.append(type(v6).__name__)
    types.append(type(v7).__name__)
    types.append(type(v8).__name__)

    print(types)


if __name__ == '__main__':
    data_types()