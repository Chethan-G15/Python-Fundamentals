"""# 7)find the power using loops and functions
ex(2,5) = 32"""
def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

print(power(2, 5))