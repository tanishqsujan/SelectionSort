A = list(map(int, input("Enter numbers in array: ").split()))

for i in range(len(A)):
    min_id= i
    for j in range(i+1, len(A)):
        if A[min_id] > A[j]:
            min_id= j
            
    A[i], A[min_id]= A[min_id], A[i]
    
print("Sorted Array: ")
print(" ".join(map(str, A)))
