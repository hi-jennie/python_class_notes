#找出输入中的第二大的值

def wang():
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
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

       
def main():
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])

    records.sort()
    second_lowest_score = next(score for score, name in records if score != records[0][0])
    print(second_lowest_score)
    second_lowest_students = sorted(name for score, name in records if score == second_lowest_score)

    for student in second_lowest_students:
        print(student)


# 保留两位小数  print('{:.2f}'.format(f))  和map的用法 map（func, iterable)       
def average_scores():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total_score = 0
    for score in student_marks[query_name]:
        total_score +=score
    print('{:.2f}'.format(total_score/3))
    
def operation():
    N = int(input())
    n = []
    final_list = []
    for _ in range(N):
        cammand = input()
        n.append(cammand)
    for j in n:
        action = j.split(" ")
        if action[0]=="insert":
            final_list.insert(int(action[1]), int(action[2]))
        elif action[0]=="print":
            print(final_list)
        elif action[0]=="remove":
            final_list.remove(int(action[1]))
        elif action[0]=="append":           
            final_list.append(int(action[1]))
        elif action[0]=="sort":
            final_list.sort()
        elif action[0]=="pop":
            final_list.pop(-1)
        elif action[0]=="reverse":
            final_list.reverse()


      
      