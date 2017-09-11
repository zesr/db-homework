import os

def deal(a):
    time=0
    ans=''
    isalp=False
    flag=False
    for i in a:
        if i.isalnum():
            if i.isalpha():
                if isalp==False:
                    ans+="'"
                isalp=True
            ans+=i
            flag=True
        else:
            if flag:
                if isalp:
                    ans+="'"
                    isalp=False
                ans+=','
                time+=1
                flag=False
    ans=ans[:-1]
    return (ans,time)

file_name=os.getcwd()
with open(file_name+r'\a.txt','r') as f:
    for temp in f.readlines():
        ans1 = 'insert into emp2016154082'
        ans,time=deal(temp)
        if time==10:
            ans1+='(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO)'
        else:
            ans1 += '(EMPNO,ENAME,JOB,  MGR,HIREDATE,SAL,DEPTNO)'
        ans1+='values'
        ans1+='('+ans+');'+'\n'
        print(ans1)