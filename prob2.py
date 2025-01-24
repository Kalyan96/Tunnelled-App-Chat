def solution(S):
    total_iterations = 0

    final_value = 0
    for i in range(len(S)):
        final_value += int(S[i])

    if (final_value % 3 == 0):
        total_iterations += 1

    for i in range(len(S)):
        sum_left = final_value - (int(S[i]))

        for j in range(10):
            if (j != (int(S[i])) and (sum_left + j) % 3 == 0):
                total_iterations += 1

    return total_iterations