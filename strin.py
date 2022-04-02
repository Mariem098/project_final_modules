def is_palindrome(s):
    try:
        s1 = s[::-1]
        s2 = s.lower()
        s3 = s1.lower()

        return s2 == s3
    except:
        print('no no wrong input')






def find_nth_occurrence(substring, string, occurrence=1):
    try:
        start = 0
        lst = []
        for i in range(len(string)):
            x = string.find(substring, start)
            if x == -1:
                break
            start = x + 1
            lst.append(x)

        if occurrence > len(lst):
            return -1
        else:
            return lst[occurrence - 1]
    except:
        print('not right input')






def solve(a, b):
    try:
        length_a = len(a)
        length_b = len(b)
        starlength = length_b - length_a + 1
        substring = ''
        starplace = a.find('*')

        if a.find('*') == -1:
            if a == b:
                return True
            else:
                return False

        for i in range(length_b):
            if b[i] != a[i]:
                if a[i] == '*':
                    substring = b[i:i + starlength]
                    break
                else:
                    return False
        print('The substring is : ', substring)

        a = a.replace('*', substring)
        if a == b:
            return True
        else:
            return False
    except:
        print('wrong input')





def f(s):
    try:
        sub=''
        c=True
        for i in s:
            sub+=i
            k=s.count(sub)
            if sub*k==s and c==True :
                tuple = (sub,k)
                return tuple
                c = False
    except:
        print('try again')
    



def f(s):
    try:
        sub = ''
        for i in s:
            sub += i
            k = s.count(sub)
            if sub * k == s:
                return (sub, k)
    except:
        print('oops wrong input')



