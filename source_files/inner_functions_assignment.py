"""
Morgan Christensen

Module6 - inner functions
program accepts a list of measurements for a rectangle
and calculates the perimeter and the area using a main and inner function

10/06/20
"""


def measurements(rect_measure):
    a_value = 0.0
    p_value = 0.0

    def area(a_measure):
        if len(a_measure) == 1:
            return a_measure[0] * a_measure[0]
        elif len(a_measure) == 2:
            return a_measure[0] * a_measure[1]
        else:
            raise IndexError

    def perimeter(p_measure):
        if len(p_measure)==1:
            return p_measure[0] * 4
        elif len(p_measure)==2:
            return (p_measure[0] * 2) + (p_measure[1] * 2)
        else:
            raise IndexError
    try:
        a_value = area(rect_measure)
        p_value = perimeter(rect_measure)
    except IndexError:
        raise IndexError
    return "Perimeter = {} Area = {}".format(p_value, a_value)


if __name__ == '__main__':
    try:
        print(measurements([2, 3]))
    except IndexError:
        print("Invalid set of measurements!")