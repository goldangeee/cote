# def solution(ineq, eq, n, m):
#     answer = 1 if (ineq == '>' and ((eq == '='and n >= m) or (eq == '!' and n > m))) or (ineq == '<' and ((eq == '=' and n <= m) or (eq == '!' and n < m))) else 0
#     return answer
def solution(ineq, eq, n, m):
    operators = {
        ('>','='): lambda x, y: x >= y,
        ('>','!'): lambda x, y: x > y,
        ('<','='): lambda x, y: x <= y,
        ('<','!'): lambda x, y: x < y
    }
    compare = operators.get((ineq, eq))
    return int(compare(n, m)) if compare else 0