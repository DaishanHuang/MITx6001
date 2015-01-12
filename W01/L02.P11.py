## L2 P11

# From AutoTesting
varA = "kk"
varB = "jj"

# The code to test
if type(varA) == type('astr') or type(varB) == type('astr'):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")