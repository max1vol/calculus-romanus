from .roman import from_roman, to_roman


def tokenize(code):
    """
    Converts a string of Calculus Romanus code into a list of tokens.
    """
    code = code.replace("maior quam", "maior_quam")
    code = code.replace("minor quam", "minor_quam")
    code = code.replace("non aequus", "non_aequus")
    tokens = code.split()
    return tokens


class State:
    def __init__(self, code):
        self.variables = {}
        self.functions = {}
        self.tokens = tokenize(code)
        self.index = 0


def run_calculus_romanus(code):
    state = State(code)
    while state.index < len(state.tokens):
        execute_statement(state)


def execute_statement(state):
    token = state.tokens[state.index]

    if token == "Scribo":
        handle_print(state)
    elif state.index + 1 < len(state.tokens) and state.tokens[state.index + 1] == "est":
        handle_assignment(state)
    elif token == "si":
        handle_conditional(state)
    elif token == "functio":
        handle_function_definition(state)
    elif token in state.functions:
        execute_function(token, state)
    else:
        state.index += 1  # Ignore unknown tokens


def handle_print(state):
    state.index += 1  # Consume "Scribo"
    value = evaluate_expression(state)
    print(to_roman(value))


def handle_assignment(state):
    variable_name = state.tokens[state.index]
    state.index += 2  # Consume variable name and "est"
    value = evaluate_expression(state)
    state.variables[variable_name] = value


def handle_conditional(state):
    state.index += 1  # Consume "si"
    condition = evaluate_condition(state)

    if state.tokens[state.index] != "ergo":
        raise SyntaxError("Expected 'ergo' after condition")
    state.index += 1  # Consume "ergo"

    if condition:
        execute_statement(state)
    else:
        # Skip to the 'aliter' or end of block
        while state.index < len(state.tokens) and state.tokens[state.index] != "aliter":
            state.index += 1
        if state.index < len(state.tokens) and state.tokens[state.index] == "aliter":
            state.index += 1  # Consume "aliter"
            execute_statement(state)


def handle_function_definition(state):
    state.index += 1  # Consume "functio"
    name = state.tokens[state.index]
    state.index += 1

    params = []
    if state.tokens[state.index] == "(":
        state.index += 1
        while state.tokens[state.index] != ")":
            params.append(state.tokens[state.index])
            state.index += 1
            if state.tokens[state.index] == ",":
                state.index += 1
        state.index += 1  # Consume ")"

    body_start = state.index
    while state.tokens[state.index] != "finio":
        state.index += 1
    body_end = state.index
    state.functions[name] = (params, state.tokens[body_start:body_end])
    state.index += 1  # Consume "finio"


def evaluate_expression(state):
    error_message = "Transgressio! In aetate Romanorum, numeri infra I non existunt. (Violation! In the age of the Romans, numbers below I do not exist.)"
    left = get_value(state)
    if left <= 0:
        raise ValueError(error_message)

    while state.index < len(state.tokens):
        op = state.tokens[state.index]
        if op in ["addit", "minuit", "multiplicat"]:
            state.index += 1
            right = get_value(state)
            if right <= 0:
                raise ValueError(error_message)

            if op == "addit":
                left = left + right
            elif op == "minuit":
                left = left - right
                if left <= 0:
                    raise ValueError(error_message)
            elif op == "multiplicat":
                left = left * right
        else:
            break  # Not an operator, so we're done with the expression.
    return left


def evaluate_condition(state):
    left = get_value(state)
    op = state.tokens[state.index]
    state.index += 1
    right = get_value(state)

    if op == "aequus":
        return left == right
    elif op == "non_aequus":
        return left != right
    elif op == "maior_quam":
        return left > right
    elif op == "minor_quam":
        return left < right
    else:
        raise SyntaxError(f"Unknown comparison operator: {op}")


def get_value(state):
    token = state.tokens[state.index]
    state.index += 1
    if token in state.variables:
        return state.variables[token]
    elif token in state.functions:
        return execute_function(token, state)
    else:
        try:
            return from_roman(token)
        except KeyError:
            raise NameError(f"Unknown variable or invalid Roman numeral: {token}")


def execute_function(name, state):
    params, body = state.functions[name]

    args = []
    if state.tokens[state.index] == "(":
        state.index += 1
        while state.tokens[state.index] != ")":
            args.append(evaluate_expression(state))
            if state.tokens[state.index] == ",":
                state.index += 1
        state.index += 1  # Consume ")"

    # Create a local scope for the function
    local_state = State("")  # Dummy state
    local_state.variables = state.variables.copy()
    local_state.functions = state.functions
    local_state.tokens = body

    for param, arg in zip(params, args):
        local_state.variables[param] = arg

    while local_state.index < len(local_state.tokens):
        if local_state.tokens[local_state.index] == "reddo":
            local_state.index += 1  # Consume "reddo"
            return evaluate_expression(local_state)
        execute_statement(local_state)

    raise SyntaxError("Function did not return a value")
