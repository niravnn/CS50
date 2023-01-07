from cs50 import get_int

size = get_int('Enter the height: ')

while (size < 1 or size > 8):
    size = get_int('Enter the height: ')

for row in range(1, size + 1):
    hashes = row
    spaces = size - hashes

    print(' ' * spaces, end="")
    print('#' * hashes)
