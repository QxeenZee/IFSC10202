def main():

    # Open the file and read all lines into a list
    file = open("constitution.txt", "r")

    lines = []
    for line in file:
        line = line.rstrip("\n")   # remove newline character
        lines.append(line)

    file.close()

    # Keep asking for search terms
    while True:

        search = input("Enter search term: ")

        # Exit if user presses Enter
        if search == "":
            break

        i = 0

        while i < len(lines):

            # Check if search term appears in the line (case insensitive)
            if search.lower() in lines[i].lower():

                # Find start of section (look backward for blank line)
                start = i
                while start > 0 and lines[start] != "":
                    start = start - 1

                # Find end of section (look forward for blank line)
                end = i
                while end < len(lines) - 1 and lines[end] != "":
                    end = end + 1

                # Print the section with line numbers
                j = start
                while j <= end:
                    print("Line", j + 1, ":", lines[j])
                    j = j + 1

                print()

                # Skip to the end of the section
                i = end + 1

            else:
                i = i + 1


# Run the program
main()