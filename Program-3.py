# Program-3.py

def odd_conditional_series(a):
    result = []
    if a < 3:
        result = [1]
    elif a in [3, 4]:
        result = [1, 3, 5]
    else:
        count = (a + 1) // 2
        for i in range(count):
            result.append(2 * i + 1)
    print(", ".join(str(x) for x in result))

# Example usage:
# odd_conditional_series(5)  # Output: 1, 3, 5, 7, 9
