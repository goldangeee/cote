def solution(my_string, queries):
    for q in queries:
        front = my_string[0:q[0]]
        if q[1]+1 < len(my_string):
            back = my_string[q[1]+1:]
        else:
            back = ''
        target = my_string[q[0]:q[1]+1]
        target = target[::-1]
        my_string = front + target + back
    return my_string