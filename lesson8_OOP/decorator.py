def merge_the_tools(string, k):
    length_of_substring = int(len(string)/int(k))
    str_lst = list(string)
    final_lst = []
    for i in range(int(k)):
        sub_set = add(length_of_substring,str_lst)
        final_lst.append(sub_set)
        delete(length_of_substring,str_lst)
        
    for i in final_lst:
        my_string = ''.join(map(str, i))
        
        for item in i:
            print(item,end="")
        print()           
def add(length_of_substring,str_lst):
    sub_lst = []
    for i in range(length_of_substring):        
        sub_lst.append(str_lst[i])
    return  sub_lst         

def delete(length_of_substring,str_lst):
    for i in range(length_of_substring):
        str_lst.remove(str_lst[0])    
    
if __name__ == '__main__':  # noqa: E999
    string, k = input(), int(input())
    merge_the_tools(string, k)