#a example list below
nest=[[[1,'a',['cat'],2],[[[3]],'dog'],4,5]]

def flatten_list(x):
    for item in x:
        if type(item) in [list]:
            for num in flatten_list(item):
                yield(num)
        else:
            yield(item)
list(flatten_list(nest))
