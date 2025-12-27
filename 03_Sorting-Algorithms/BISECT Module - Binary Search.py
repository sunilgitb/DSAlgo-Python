import bisect

# This sorted list will be used throughout to showcase the functionality
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

print("Original list A:", A)
print()

# bisect_left function - returns the leftmost insertion point
print("bisect_left examples:")
print("bisect_left(A, -10):", bisect.bisect_left(A, -10))  # -10 is at index 1
print("bisect_left(A, 285):", bisect.bisect_left(A, 285))  # First occurrence of 285 at index 6
print("bisect_left(A, 500):", bisect.bisect_left(A, 500))  # Would be inserted at index 10
print()

# bisect_right function - returns the rightmost insertion point
print("bisect_right examples:")
print("bisect_right(A, -10):", bisect.bisect_right(A, -10))  # Index position right of -10 is 2
print("bisect_right(A, 285):", bisect.bisect_right(A, 285))  # Index position after last 285 is 9
print()

# Default bisect function (same as bisect_right)
print("Default bisect examples (same as bisect_right):")
print("bisect(A, -10):", bisect.bisect(A, -10))
print("bisect(A, 285):", bisect.bisect(A, 285))
print()

# insort_left - inserts at the leftmost position
print("insort_left examples:")
B = A.copy()
print("Before insort_left(B, 108):", B)
bisect.insort_left(B, 108)
print("After insort_left(B, 108):", B)
print()

# insort_right - inserts at the rightmost position
print("insort_right examples:")
C = A.copy()
print("Before insort_right(C, 108):", C)
bisect.insort_right(C, 108)
print("After insort_right(C, 108):", C)
print()

# More examples
print("Additional examples:")
print("bisect_left(A, 1):", bisect.bisect_left(A, 1))  # Would be inserted at index 2
print("bisect_right(A, 1):", bisect.bisect_right(A, 1))  # Would be inserted at index 2
print("bisect_left(A, 108):", bisect.bisect_left(A, 108))  # Leftmost 108 at index 3
print("bisect_right(A, 108):", bisect.bisect_right(A, 108))  # Right of 108s at index 5