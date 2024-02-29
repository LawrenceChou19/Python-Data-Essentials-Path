def separate_section():
    print("-" * 80)


def print_params(x,*args):
    print("x:",x)
    print("args:",args)
    print("args[0]",args[0])
print_params("a","b","c","d")
separate_section()
    
def print_params(x,*args, **kwargs):
    print("x:",x)
    print("args:",args)
    print("args[0]",args[0])
    print("kwargs:",kwargs)
    print("kwargs['first']:",kwargs['first'])
print_params("a","b","c","d",first="e",second="f")

def print_params(x,*args,**kwargs):
    for item in args:
        print(item)
    for val in kwargs.values():
        print(val)
print_params("a","b","c","d",first="e",second="f")
