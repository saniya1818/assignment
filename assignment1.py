def lower_triangular(size):
    for i in range(size):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def upper_triangular(size):
    for i in range(size):
        for j in range(size):
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print()

def pyramid(size):
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

size = 5

print("Lower Triangular Pattern:")
lower_triangular(size)

print("\nUpper Triangular Pattern:")
upper_triangular(size)

print("\nPyramid Pattern:")
pyramid(size)
