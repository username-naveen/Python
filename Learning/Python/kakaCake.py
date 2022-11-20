n = int(input());
arr = list(map(int, input().split()))
arr2 = [];
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            arr2.append(arr[j]); 