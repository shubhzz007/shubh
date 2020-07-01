class Pair:
    def pairing(self,queu):

        for j in queu:
            cnt_x = 0
            cnt_y = 0
            for k in j:
                for i in k:
                    if i=='x':
                        cnt_x = cnt_x +1
                    else :
                        cnt_y = cnt_y +1

            if cnt_x == cnt_y:
                print(cnt_y)
            elif cnt_y > cnt_x :
                print(cnt_x)
            else:
                print(cnt_y)
p = Pair()
n = int(input())
queu = []
for i in range(n):
    a = input()
    queu.append([a])
p.pairing(queu)