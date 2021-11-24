1 2 3
1 3 2
Cat B
Mouse C

Cat B will catch the mouse first, so we print Cat B on a new line.
Query 1: In this query, cats A and B reach mouse at the exact same
Because the mouse escapes, we print Mouse C on a new line.

def catAndMouse(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
    
    return "Cat A" if a<b else "Cat B" if b<a else "Mouse C" 
