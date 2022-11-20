if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        print(scores)
        scores = map(float, scores)
        print(scores)
        student_marks[name] = scores
    query_name = input()
    
    print(student_marks.items())
    tot = 0
    lst = []
    for name,val in student_marks.items():
        if name == query_name:
            lst.append(val)
    print(lst)