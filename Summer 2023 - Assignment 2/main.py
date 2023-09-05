import shapedb

shapes_database = []
our_set = []

def load(file_name):
    global shapes_database
    processed_row = 0
    shapes_added = 0
    errors = 0

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("Processing", file_name)

            for line in lines:
                shape_data = line.strip().split()
                shape_type = shape_data[0].strip().lower()

                if shape_type == "shape":
                    processed_row += 1
                    shapes_added += 1
                    shape = shapedb.Shape()
                    shapes_database.append(shape)
                    if len(shape_data) > 1:
                        print("Error. Invalid Shape on line", processed_row, ": ", line)

                elif shape_type == "circle":
                    processed_row += 1
                    if len(shape_data) != 2 or not shape_data[1].strip().isdigit():
                        print("Error. Invalid Circle on line", processed_row, ": ", line)
                    else:
                        shapes_added += 1
                        radius = float(shape_data[1].strip())
                        circle = shapedb.Circle(radius)
                        shapes_database.append(circle)

                elif shape_type == "ellipse":
                    processed_row += 1
                    if len(shape_data) != 3 or not shape_data[1].strip().isdigit() or not shape_data[
                        2].strip().isdigit():
                        print("Error. Invalid Ellipse on line", processed_row, ": ", line)
                        errors += 1
                    else:
                        shapes_added += 1
                        a = float(shape_data[1].strip())
                        b = float(shape_data[2].strip())
                        ellipse = shapedb.Ellipse(a, b)
                        shapes_database.append(ellipse)

                elif shape_type == "rhombus":
                    processed_row += 1
                    if len(shape_data) != 3 or not shape_data[1].strip().isdigit() or not shape_data[
                        2].strip().isdigit():
                        print("Error. Invalid Rhombus on line", processed_row, ": ", line)
                        errors += 1
                    else:
                        shapes_added += 1
                        x = float(shape_data[1].strip())
                        y = float(shape_data[2].strip())
                        rhombus = shapedb.Rhombus(x, y)
                        shapes_database.append(rhombus)

                else:
                    print("Invalid shape type: {}".format(shape_type))
        print("Processed {} row(s), {} shapes added, {} error(s)".format(processed_row,shapes_added, errors))
        print("File '{}' loaded successfully.".format(file_name))

    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))

    return shapes_database


def toset():
    global our_set
    index = 0
    while index < len(shapes_database):

        shape = shapes_database[index]
        name = shape.__class__.__name__

        if name == 'Circle':
            temp = f"circle {shape.radius}"
        elif name == 'Ellipse':
            temp = f"ellipse {shape.semi_minor} {shape.semi_major}"
        elif name == 'Rhombus':
            temp = f"rhombus {shape.x} {shape.y}"
        elif name == 'Shape':
            temp = "shape"

        if temp in our_set:
            del shapes_database[index]
        else:
            our_set.append(temp)
            index += 1
            shape.id = index


def save(file_name):
    try:
        with open(file_name, 'w') as file:
            for shape in our_set:
                file.write(shape.__str__() + "\n")
        print("Data saved to file '{}'.\n".format(file_name))
    except IOError:
        print("Error saving data to file '{}'.".format(file_name))
    return None


def summary():
    shape_counts = {}
    shapes_count = 0

    for shape in shapes_database:
        shape_type = shape.__class__.__name__
        if shape_type not in shape_counts:
            shape_counts[shape_type] = 1
            shapes_count += 1
        else:
            shape_counts[shape_type] += 1
            shapes_count += 1
    shape_counts["Shape"] = shapes_count
    for shape_type, count in sorted(shape_counts.items()):
        print("{}(s): {}".format(shape_type, count))

    return None


def details():

    if our_set:
        shapes = our_set
    else:
        shapes = shapes_database

    for shape in shapes:
        print(shape.__str__())
    return None


if __name__ == '__main__':

    print("Welcome to the database Read and Process Application\n")

    while True:

        print("Select one of the following from the menu system:")
        print("- LOAD <file>")
        print("- TOSET")
        print("- SAVE <file>")
        print("- PRINT")
        print("- SUMMARY")
        print("- DETAILS")
        print("- QUIT")

        user_input = input("Enter your choice: ").strip().split()
        if len(user_input) == 0:
            print("Invalid input. Please try again.")
            continue

        command = user_input[0].upper()

        if command == "LOAD":
            if len(user_input) == 2:
                file_name = user_input[1]
                load(file_name)
                print()
            else:
                print("Invalid command. Please provide a file name.")
        elif command == "TOSET":
            toset()
            print("TOSET operation completed.")
        elif command == "SAVE":
            if len(user_input) == 2:
                file_name = user_input[1]
                save(file_name)
            else:
                print("Invalid command. Please provide a file name.")
        elif command == "PRINT":
            count = 1
            for shape in shapes_database:
                print(count, ": ", end="")
                shape.print()
                count += 1

        elif command == "SUMMARY":
            summary()
            print("Summary generated.")
        elif command == "DETAILS":
            details()
            print("Details generated.")
        elif command == "QUIT":
            print("Exiting the program...")
            break
        else:
            print("Invalid command. Please try again.")
