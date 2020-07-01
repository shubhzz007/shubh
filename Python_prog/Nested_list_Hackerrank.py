'''if __name__ == '__main__':
    list = []
    lst_score = []
    lst_name = []
    n = int(input())
    list = [[input(), float(input())] for i in range(n)]
    #print(list)
    lst_score.remove(min(lst_score))
    min_score = min(lst_score)
    #print(min_score)
    for i in list:
        #print(i)
        if i[1]==min_score:
            #print(i[0])
            lst_name.append(i[0])
    lst_name.sort(key = lambda x:x[0])
    for i in lst_name:
        print(i)
'''
a = [[input(), float(input())] for i in range(int(input()))]
s = sorted(set(x[1] for x in a))
for name in sorted(x[0] for x in a if x[1]==s[1]):
    print(name)
