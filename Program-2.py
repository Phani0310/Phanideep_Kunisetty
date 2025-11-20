# Program-2.py

def odd_series(a):
    result = []
    num = 1
    for i in range(a):
        result.append(num)
        num += 2
    print(", ".join(str(x) for x in result))

# Example usage:
# odd_series(3)  # Output: 1, 3, 5
