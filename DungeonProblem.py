
R, C = 5, 7

m = [['S', '.', '.', '#', '.', '.', '.'],
     ['.', '#', '.', '.', '.', '#', '.'],
     ['.', '#', '.', '.', '.', '.', '.'],
     ['.', '.', '#', '#', '.', '.', '.'],
     ['#', '.', '#', 'E', '.', '#', '.']]
sr, sc = 0, 0
rq, cq = [], []

move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False
visited = [[False] * C] * R


def checkSurround(r, c):
    # Define the direction vectors
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Skip invalid cells
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue

        print((rr, cc))
        # rr, cc are the neighboring cells
        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        global nodes_in_next_layer

        nodes_in_next_layer += 1


def solve():

    global move_count
    global nodes_left_in_layer
    global nodes_in_next_layer
    global reached_end

    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)
        if m[r][c] == 'E':
            reached_end = True
            break
        checkSurround(r, c)

        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


print(solve())
