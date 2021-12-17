def main():
    course = [l.split(" ") for l in open("./day2/input")]
    horiz, depth = 0, 0
    for direction, distance in course:
        distance = int(distance)
        if direction == "forward":
            horiz += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        else:
            pass  # shouldn't reach here
    print(f"Depth x Horizontal :{depth*horiz}")


if __name__ == "__main__":
    main()
