# C5 - Star-Delta (Y-Delta) Transformation
# Function star_to_delta() converts the three resistors of a Star (Y) network
# into the equivalent Delta network, rounded to two decimal places.


def star_to_delta(ra, rb, rc):
    # Numerator factor is calculated once to avoid repeating it
    r_numerator = ra * rb + rb * rc + rc * ra

    r_ab = r_numerator / rc
    r_bc = r_numerator / ra
    r_ca = r_numerator / rb

    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)


print("star_to_delta(10, 20, 30) ->", star_to_delta(10, 20, 30))

# Extra test with my own values (equal resistors: Delta should be 3 times Star)
print("star_to_delta(5, 5, 5) ->", star_to_delta(5, 5, 5))
