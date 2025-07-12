def tokenize(code):
    n1s = ""
    op = ""
    n2s = ""
    state = "n1"
    for e in code:
        if e == " ":
            continue
        elif (e >= "0" and e <= "9") or e == ".":
            if state == "n1":
                n1s += e
            elif state == "n2":
                n2s += e
            elif state == "op":
                n2s = e
                state = "n2"
        else:
            state = "op"
            op += e
    return [n1s, op, n2s]


def run(code):
    tokens = tokenize(code)
    n1s, op, n2s = tokens
    n1 = float(n1s)
    n2 = float(n2s)
    if op == "add":
        return n1 + n2
    if op == "sub":
        return n1 - n2
    if op == "x":
        return n1 * n2
    if op == "mod":
        return n1 % n2
    if op == "div":
        return n1 / n2
    if op == "int_div":
        return n1 // n2
    if op == "^":
        return n1**n2
    return f"unknown operation {op}"


code = input("Enter code: ")
print(run(code))
