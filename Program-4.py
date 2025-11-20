# Program-4.py

def multiples_count(lst):
    output = {}
    for i in range(1, 10):
        output[i] = sum(1 for num in lst if num % i == 0)
    print(output)

# Example usage:
# multiples_count([1,2,8,9,12,46,76,82,15,20,30])
# Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
