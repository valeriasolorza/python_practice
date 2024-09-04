def max_num(a, b, c):
    return max(a, b, c)

# Example usage:
print(max_num(3, 5, 1))  # Output: 5

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage:
print(mult_list([2, 3, 5]))  # Output: 30

def rev_string(s):
    return s[::-1]

# Example usage:
print(rev_string("hello"))  # Output: "olleh"

def num_within(num, start, end):
    return start <= num <= end

# Example usage:
print(num_within(3, 2, 4))  # Output: True
print(num_within(10, 2, 5))  # Output: False

def pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    for row in triangle:
        print(row)

# Example usage:
pascal(5)
