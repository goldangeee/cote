# 송용진
def solution(keyinput, board):
    current = [0,0]
    for direction in keyinput:
        if direction == "up" and abs(current[1] + 1) <= board[1] // 2:
            current[1] += 1
        elif direction == "down" and abs(current[1] - 1) <= board[1] // 2:
            current[1] -= 1
        elif direction == "left" and abs(current[0] - 1) <= board[0] // 2:
            current[0] -= 1
        elif direction == "right" and abs(current[0] + 1) <= board[0] // 2:
            current[0] += 1
        else:
            continue

    return current