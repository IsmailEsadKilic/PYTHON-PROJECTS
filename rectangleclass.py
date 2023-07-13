class point():
    '''
    this be a point
    '''

class rectangle():
    '''
    this represents a rectangle
    attributes are width height and lower left corner
    '''

box = rectangle()
box.width = 400
box.lenght = 200
box.corner = point()
box.corner.x = 100
box.corner.y = 100

def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.lenght / 2.0
    return p

print(f"center point of the box is {find_center(box).x},{find_center(box).y}")


