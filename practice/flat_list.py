# create flat list from list of list

def create_flat_list(uneven_list):
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    flat_list = list(flatten(uneven_list))
    return flat_list
  
# convert list of dic to dict
from functools import reduce 
final_result_dict = reduce(lambda a, b: dict(a, **b), output_list) 
