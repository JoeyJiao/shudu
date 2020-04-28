import sys
import collections

class GetOutOfLoop(BaseException):
    pass

array = [([0] * 9) for i in range(9)]
array = [
    [3, 0, 0, 0, 0, 0, 0, 0, 4],
    [2, 0, 0, 8, 9, 0, 6, 0, 0],
    [8, 0, 0, 6, 0, 0, 0, 2, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 9, 0],
    [0, 0, 3, 0, 0, 0, 2, 0, 0],
    [6, 0, 0, 0, 0, 1, 0, 0, 5],
    [9, 0, 4, 0, 0, 7, 1, 0, 0],
    [0, 5, 8, 0, 0, 6, 0, 0, 0],
]

# Works
#array = [
#    [2, 0, 1, 5, 4, 0, 0, 0, 6],
#    [0, 0, 5, 6, 0, 2, 1, 3, 0],
#    [0, 0, 8, 3, 0, 0, 0, 5, 7],
#    [8, 0, 4, 0, 3, 0, 0, 7, 2],
#    [3, 9, 2, 4, 7, 0, 6, 0, 0],
#    [0, 0, 6, 9, 0, 8, 5, 4, 0],
#    [5, 2, 3, 0, 6, 0, 4, 0, 0],
#    [0, 0, 9, 0, 0, 0, 0, 0, 1],
#    [1, 6, 0, 0, 0, 0, 0, 2, 0],
#]

array_orig = list(array)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

candidates = {}
for i in range(9):
    candidates[i] = {}
    for j in range(9):
        candidates[i][j] = []

def remove_candidate(i, j, v):
    global candidates
    try:
        candidates[i][j].remove(v)
    except:
        pass

def find_candidates(i, j):
    global candidates, array
    if array[i][j] != 0:
        candidates[i][j] = [array[i][j]]
        return
    for k in range(9):
        if array[i][k] != 0:
            remove_candidate(i, j, array[i][k])
    for k in range(9):
        if array[k][j] != 0:
            remove_candidate(i, j, array[k][j])
    x = 3 * int(i/3)
    y = 3 * int(j/3)
    if array[x][y] != 0:
        remove_candidate(i, j, array[x][y])
    if array[x][y+1] != 0:
        remove_candidate(i, j, array[x][y+1])
    if array[x][y+2] != 0:
        remove_candidate(i, j, array[x][y+2])
    if array[x+1][y] != 0:
        remove_candidate(i, j, array[x+1][y])
    if array[x+1][y+1] != 0:
        remove_candidate(i, j, array[x+1][y+1])
    if array[x+1][y+2] != 0:
        remove_candidate(i, j, array[x+1][y+2])
    if array[x+2][y] != 0:
        remove_candidate(i, j, array[x+2][y])
    if array[x+2][y+1] != 0:
        remove_candidate(i, j, array[x+2][y+1])
    if array[x+2][y+2] != 0:
        remove_candidate(i, j, array[x+2][y+2])
    # remove candidates in closer row/column
    if len(candidates[i][j]) != 1:
        # Find duplicated number in upper and lower row
        Row1 = [array[x][k] for k in range(9) if array[x][k] != 0]
        Row2 = [array[x+1][k] for k in range(9) if array[x+1][k] != 0]
        Row3 = [array[x+2][k] for k in range(9) if array[x+2][k] != 0]
        D1 = [item for item, count in collections.Counter(Row1 + Row2 + Row3).items() if count > 1]
        # Find duplicated number in upper and lower row
        Col1 = [array[k][y] for k in range(9) if array[k][y] != 0]
        Col2 = [array[k][y+1] for k in range(9) if array[k][y+1] != 0]
        Col3 = [array[k][y+2] for k in range(9) if array[k][y+2] != 0]
        D2 = [item for item, count in collections.Counter(Col1 + Col2 + Col3).items() if count > 1]
        D = [item for item, count in collections.Counter(D1 + D2).items() if count > 1]
        for d in D:
            if d in candidates[i][j]:
                candidates[i][j] = [d]
                array[i][j] = d
                break
 
def is_done():
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) != 1:
                return False
    return True

def count():
    global candidates
    count = 0
    for i in range(9):
        for j in range(9):
            count += len(candidates[i][j])
    print("candidate count=" + str(count))

def count_array():
    global array
    count = 0
    for i in range(9):
        for j in range(9):
            if array[i][j] != 0:
                count += 1
    print("array count=" + str(count))
    return count

def print_candidates():
    global candidates
    for i in range(9):
        out = ''
        for j in range(9):
            out += ';'.join([str(x) for x in candidates[i][j]]) + ','
        if out[-1] == ',':
            out = out[:-1]
        print(out)

is_first_run = True
    
def update_candidates():
    global candidates, is_first_run, array
    for i in range(9):
        for j in range(9):
            if is_first_run:
                candidates[i][j] = list(num)
            find_candidates(i, j)
    is_first_run = False
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 1 and array[i][j] == 0:
                array[i][j] = candidates[i][j][0]

def main():
    global is_first_run, candidates, array
    while True:
        update_candidates()
        count()
        if is_done():
            break
        count_array()
    
    print_candidates()
        

if __name__ == '__main__':
    main()
