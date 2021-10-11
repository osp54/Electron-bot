def resolve_variable(variable):
    if hasattr(variable, "__iter__"):
        var_length = len(list(variable))
        if (var_length > 100) and (not isinstance(variable, str)):
            return f"<a {type(variable).__name__} iterable with more than 100 values ({var_length})>"
        elif (not var_length):
            return f"<an empty {type(variable).__name__} iterable>"
    if (not variable) and (not isinstance(variable, bool)):
        return f"<an empty {type(variable).__name__} object>"
    return (variable if (len(f"{variable}") <= 1000) else f"<a long {type(variable).__name__} object with the length of {len(f'{variable}'):,}>")
def prepare(string):
    arr = string.strip("```").replace("py\n", "").replace("python\n", "").split("\n")
    if not arr[::-1][0].replace(" ", "").startswith("return"):
        arr[len(arr) - 1] = "return " + arr[::-1][0]
    return "".join(f"\n\t{i}" for i in arr)
