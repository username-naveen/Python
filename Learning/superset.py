# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a = set(map(int, raw_input().split()))
    n = int(raw_input())
    b = []
    
    for x in range(n):
        s = set(map(int, raw_input().split()))
        b.append(s)
    
    count = 0
    for i in range(n):
        if (any(j in b[i] for j in range(len(b[i]))) not in list(a)) and (all(k in b[i] for k in range(len(b[i]))) in list(a)):
            count += 1
        else:
            count += 0
    
    if count == n:
        print('True')
    else:
        print('False')