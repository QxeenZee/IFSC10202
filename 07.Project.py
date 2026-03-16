def ParseDegreeString(ddmmss):
    # Find symbol positions
    deg_pos = ddmmss.find(chr(176))   # degree symbol °
    min_pos = ddmmss.find("'")        # minute symbol '
    sec_pos = ddmmss.find('"')        # second symbol "

    # Extract values
    degrees = ddmmss[0:deg_pos]
    minutes = ddmmss[deg_pos + 1:min_pos]
    seconds = ddmmss[min_pos + 1:sec_pos]

    # Convert to float
    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)

    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees


def main():

    input_file = open("07.Project Angles Input.txt", "r")
    output_file = open("07.Project Angles Output.txt", "w")

    count = 0

    for line in input_file:
        line = line.strip()

        if line != "":
            degrees, minutes, seconds = ParseDegreeString(line)

            decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)

            output_file.write(str(decimal_value) + "\n")

            count = count + 1

    input_file.close()
    output_file.close()

    print(count, "records processed")


main()