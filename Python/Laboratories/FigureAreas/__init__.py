import tria, square, rect, romb, trapec

type = None

while type != 'q':
    type = input("What type of figure (tri, sq, rec, romb, trap) \n")

    if type == "tri":
        tria.Area()
    elif type == 'sq':
        square.Area()
    elif type == 'rec':
        rect.Area()
    elif type == 'romb':
        romb.Area()
    elif type == 'trap':
        trapec.Area()