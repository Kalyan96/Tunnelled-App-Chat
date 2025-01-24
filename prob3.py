def solution(blocks):
    # write your code in Python 3.6
    num = len(blocks)
    ressssults = 0
    for iter in range(num):
        tempvar = iter
        # move left while A are less than or equal to current block
        while tempvar > 0 and blocks[tempvar-1] >= blocks[tempvar]:
            tempvar -= 1
        low = tempvar
        tempvar = iter
        # move right while A arblocks less than or equal to current block
        while tempvar < num-1 and blocks[tempvar+1] >= blocks[tempvar]:
            tempvar += 1
        high = tempvar
        ressssults = max(ressssults, high - low )
    return ressssults+1
    pass