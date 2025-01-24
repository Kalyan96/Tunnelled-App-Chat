def solution(A, Y):
    # write your code in Python 3.6
    total_add=0
    total_points=0
    for i in range(0,len(A)):
        for j in range(i+1,len(A)):
            for k in range(j+1,len(A)):
                total_add=A[i]+A[j]+A[k]
                if total_add%Y == 0:
                    total_points=total_points+1
    return total_points