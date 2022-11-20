# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input
# 5
# 2 3 6 6 5
# Sample Output
# 5

# code:
if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    arr = []
    for i in a:
        if i not in arr:
            arr.append(i)
            print(arr)
    for j in range(0, len(arr)):
        for k in range(j+1,len(arr)):
            if arr[j]>arr[k]:
                temp = arr[j]
                arr[j]=arr[k]
                arr[k]=temp
    
    print(arr[-2])