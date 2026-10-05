def truth_table(n):
    if n == 0:
        return [()]   
    res = []
    for i in range(2**n):
        row = tuple(int(bit) for bit in bin(i)[2:].zfill(n))
        res.append(row)
    return res
print(truth_table(1))  
print(truth_table(2))  
