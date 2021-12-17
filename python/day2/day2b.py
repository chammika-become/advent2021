def main():
    course = [l.split(" ") for l in open("./day2/input")]
    horiz, depth, aim = 0, 0, 0
    for direction, distance in course:
        distance = int(distance)
        if direction == "forward":
            horiz += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        else:
            pass  # shouldn't reach here
    print(f"Depth x Horizontal :{depth*horiz}")


if __name__ == "__main__":
    main()
