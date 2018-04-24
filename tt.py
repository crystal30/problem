# n = 3
# v = 2
# t = [1,2,1]
# p = [2,7,3]
#买糖果（京东2016实习生真题）
#未通过,不知道什么原因
while 1:
    t = []
    p = []
    r = raw_input()
    if r != '':
        n,v = map(int,r.strip().split())
        for _ in range(n):
            ti,pi = map(int,raw_input().strip().split())
            t.append(ti)
            p.append(pi)

        number = [i for i in range(1,n+1)]
        if sum(t)<= v:
            print(sum(p))
            print(' '.join(str(nu) for nu in number))
        while sum(t)>v:
            i = p.index(min(p[::-1]))
            p.pop(i)
            t.pop(i)
            number.pop(i)
        print(str(sum(p)))
        print(' '.join(str(nu) for nu in number))

