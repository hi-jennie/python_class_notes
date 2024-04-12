
def main():
    name, house = get_student()
    print(f"{name} from {house}")
    #student = get_student()
    #if student[0] == "Jennie":
    #    student[1] = "sichuan"  #因为get_student返回的是tuple，所以这条赋值命令其实无法执行（tuple不可修改）,如果要修改，可以将返回值改为list或dict
    # print(f"{student[0]} from {student[1]})


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house
    #return [name, house]————这样作为一个list返回的话，就可以通过index修改了
    
    
def get_student_dict():
    student = {}
    student["name"] = input("Name:")   
    student["house"] = input("House:")   
    return student
    #name = input("Name:")   
    #house = = input("House:")
    #return{"name":name,"house":house}
    
    
if __name__ == "__main__":
    main()