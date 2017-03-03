"""
Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle
is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one
thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
"""
def point_in_triangle(a, b, c, p=(0, 0)):
    # Solve using barycentric coordinates
    denom = ((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1]))
    bary_a = ((b[1] - c[1]) * (p[0] - c[0]) + (c[0] - b[0]) * (p[1] - c[1])) / denom
    bary_b = ((c[1] - a[1]) * (p[0] - c[0]) + (a[0] - c[0]) * (p[1] - c[1])) / denom
    bary_c = 1 - bary_a - bary_b
    return 0 <= bary_a <= 1 and 0 <= bary_b <= 1 and 0 <= bary_c <= 1


assert point_in_triangle((-340, 495), (-153, -910), (835, -947))
assert not point_in_triangle((-175, 41), (-421, -714), (574, -645))


def points(line):
    x1, y1, x2, y2, x3, y3 = map(int, line.rstrip().split(','))
    return (x1, y1), (x2, y2), (x3, y3)


if __name__ == '__main__':
    print('Answer:', len([line for line in open('p102_triangles.txt') if point_in_triangle(*points(line))]))
