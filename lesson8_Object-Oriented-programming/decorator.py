
name = ["wangxue","Jennie",["王雪","刘晓波",["鳌拜","turkey"]]]

def print_name(lst):
    for i in lst:
        if type(i) == list:
            print_name(i)
        else:
            print(i)
print_name(name)
        