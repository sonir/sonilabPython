def make(val):
    return (val,)

def merge(tuple1, tuple2):
    new_tuple = (tuple1 + tuple2)
    return new_tuple

def sort(tuple1):
    my_list = list(tuple1)
    my_list.sort()
    return tuple(my_list)

def split(tpl,index):
    my_list = list(tpl)
    list_a = my_list[:index]
    list_b = my_list[index:]
    return tuple(list_a), tuple(list_b)

def get_top(tpl):
    splited = split(tpl,1)
    return splited[0][0]
