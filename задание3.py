def truth_table(n):
    return [tuple(int(bit) for bit in bin(i)[2:].zfill(n)) for i in range(2**n)]

def are_equivalent(f, g, n):
    for table_row in truth_table(n):
        if f(*table_row) != g(*table_row):
            return False
    return True

def de_morgan_left(a, b): return not (a and b)
def de_morgan_right(a, b): return (not a) or (not b)
def wrong(a, b): return (not a) and (not b)

print(are_equivalent(de_morgan_left, de_morgan_right, 2))  
print(are_equivalent(de_morgan_left, wrong, 2))             
