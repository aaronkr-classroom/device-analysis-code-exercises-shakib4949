# BINARY
a = 132
b = 45

fmt0 = '{:<10}'
fmt1 = '0b{:08b}  0x{:02x}  {:3}'
n = 30

print("bitwise AND")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-' * n)
print(fmt0.format('a & b'), fmt1.format(a & b, a & b, a & b))

# OR

print("bitwise OR")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-' * n)
print(fmt0.format('a | b'), fmt1.format(a | b, a | b, a | b))


# EXCLUSIVE OR (XOR)

print("bitwise XOR")
print(fmt0.format('a'), fmt1.format(a, a, a))
print(fmt0.format('b'), fmt1.format(b, b, b))
print('-' * n)
print(fmt0.format('a ^ b'), fmt1.format(a ^ b, a ^ b, a ^ b))


# NOT

print("bitwise NOT")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-' * n)
print(fmt0.format('~a'), fmt1.format(~a & 0xFF, ~a & 0xFF, ~a))


# LEFT SHIFT

print("left shift a << 2")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-' * n)
print(fmt0.format('a << 2'), fmt1.format(a << 2, a << 2, a << 2))

# RIGHT SHIFT

print("right shift a >> 2")
print(fmt0.format('a'), fmt1.format(a, a, a))
print('-' * n)
print(fmt0.format('a >> 2'), fmt1.format(a >> 2, a >> 2, a >> 2))

