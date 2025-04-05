
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
        if (tup[1] in res.keys()):
            res[tup[1]].append(tup[0])
        else:
            res[tup[1]] = []
            res[tup[1]].append(tup[0])

    return res

def print_dict(d:dict):
    for k, v in d.items():
        print("'{}' : ".format(k), end="")
        for country in v:
            print("'{}'".format(country), end=" ")
        print()


if __name__ == "__main__":
    res_dict = from_tuple_to_dict()
    print_dict(res_dict)