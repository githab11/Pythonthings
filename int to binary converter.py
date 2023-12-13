from bitstring import BitArray
# Function to convert number to Binary
def Binary(num):
    if num >= 1:
        Binary(num // 2)
    print(num % 2, end='')

dec_val = 764
Binary(dec_val)


