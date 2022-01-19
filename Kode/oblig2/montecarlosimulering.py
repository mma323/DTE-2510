#Programmet benytter Monte Carlo simulering til å estimere pi

import random

#Antar at sentrum i kvadratet er origo
def generate_random_points_in_square(amount_of_points, length):
    x = [0] * amount_of_points
    y = [0] * amount_of_points

    for point in range(amount_of_points):
        x[point] = (length/2) * random.uniform(-1, 1)
        y[point] = (length/2) * random.uniform(-1, 1)

    points = [x, y]

    return points

def check_if_point_inside_circle(radius, centre_x, centre_y, point_x, point_y):
    if (point_x - centre_x)**2 + (point_y - centre_y)**2 < radius**2:
        return True
    else:
        return False


def main():
    SIDE_LENGTH_SQUARE = 2
    RADIUS_CIRCLE = 1
    AMOUNT_OF_POINTS = 1000000

    points_in_square = (
     generate_random_points_in_square(AMOUNT_OF_POINTS, SIDE_LENGTH_SQUARE) )
     
    number_of_hits = 0
    for i in range(AMOUNT_OF_POINTS):
        if check_if_point_inside_circle(
            RADIUS_CIRCLE, 0, 0, points_in_square[0][i], points_in_square[1][i]
            ) == True:
            number_of_hits+=1

    approximation_of_pi = (4 * number_of_hits) / AMOUNT_OF_POINTS

    print(approximation_of_pi)

main()