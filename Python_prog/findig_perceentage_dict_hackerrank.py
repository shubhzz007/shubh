if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        #name = input()
        scores = list(map(str, input().split()))
        student_marks[scores[0]] = [float(i) for i in scores[1:7]]
    query_name = input()
    add = f'{(sum(student_marks[query_name])/3):.2f}'
    print(add)