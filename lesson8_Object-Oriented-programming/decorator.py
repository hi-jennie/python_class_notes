'''
def len(func):
    names = []
    def inner(*args, **kwargs):
        name = func(*args, **kwargs)
        names.append(name)
        return name
    return inner

@len()
def get_name():
    name = input("What's your name?")
    return name

get_name()
print(get_name.__name__)

'''


if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = [name, score]
        records.append(record)
        scores.append(score)
    
    scores = list(set(sorted(scores)))
    print(scores)
    sorted_student = sorted(records, key=lambda line:(line[1],line[0]))
    print(sorted_student)
    
    students = []
    for line in sorted_student:
        student, score_ = line
        if len(scores) == 2:
            if score_ == scores[0]:
                students.append(student)
        elif len(scores) > 2:
            if score_ == scores[1]:
                students.append(student)
    students = sorted(students)
    print(students)
    for i in students:
        print(i)
            
    
    