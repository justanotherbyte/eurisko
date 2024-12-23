from exercises import (
    check_if_symmetric,
    count_characters,
    convert_to_letters,
    convert_to_numbers,
    is_prime,
    get_intersection,
    get_union,
)

tests = [
    {"function": check_if_symmetric, "input": ("racecar",), "output": True},
    {"function": check_if_symmetric, "input": ("hello",), "output": False},
]

for test in tests:
    func = test["function"]
    args = test["input"]
    expected_output = test["output"]
    actual_output = func(*args)
    if actual_output == expected_output:
        print("Test passed...")
    else:
        print(f"Test failed. Expected {expected_output}, got {actual_output}")
