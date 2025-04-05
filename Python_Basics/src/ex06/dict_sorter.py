def from_tuple_to_dict() -> dict:
    res = dict()
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    for tup in list_of_tuples:
        res[tup[0]] = int(tup[1])

    return res

def sort_dict(d:dict) -> dict:
    countries = d.keys()
    nums = [v for k, v in d.items()]
    uniq_nums = list(set([v for k, v in d.items()]))
    nums.sort(reverse=True)
    uniq_nums.sort(reverse=True)
    for n in uniq_nums:
        if nums.count(n) > 1:
            several_c = []
            for c in countries:
                if d[c] == n:
                    several_c.append(c)
            for sc in sorted(several_c):
                print(sc)
        else:
            for c in countries:
                if d[c] == n:
                    print(c)


if __name__ == "__main__":
    countries = from_tuple_to_dict()
    sort_dict(countries)
