#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program calculates the volume of a triangular prism


def volume_calculator(base_length, altitude, height):
    # This function calculates the volume of a triangular prism
    volume = round(base_length * altitude / 2 * height, 3)

    return volume


def main():
    # This function is the main function
    print("This calculates the volume of a triangular prism.")

    while True:
        try:
            # input & process
            user_base_length = input("Enter the base length (cm): ")
            user_base_length = float(user_base_length)

            user_altitude = input("Enter the altitude (height of the triangle) (cm): ")
            user_altitude = float(user_altitude)

            user_height = input("Enter the height of the prism (cm): ")
            user_height = float(user_height)

            # call function & output
            print(
                "\nThe volume of the triangular prism is {0} cm³.".format(
                    volume_calculator(user_base_length, user_altitude, user_height)
                )
            )
            break
        except (Exception):
            print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
