def pasture_area(wire, w):
    l = wire / 2 - w
    if l < 0:
        return 0.0
    return l * w
def best_pasture(wire):
    w = wire / 4
    l = wire / 2 - w
    area = l * w
    return (w, l, area)

print(pasture_area(100, 25))    
print(best_pasture(100))       
