def merge_files(input_file, merge_file, output_file):
    #Merges the contents of two files into a new file based on specific instructions.

    input_count = 0
    merge_count = 0
    output_count = 0
    insert_merge = "Insert Merge File Here"

    try:
        with open(input_file, 'r') as infile, \
             open(merge_file, 'r') as mergefile, \
             open(output_file, 'w') as outfile:

            for line in infile:
                if insert_merge in line:
                    for merge_line in mergefile:
                        merge_count += 1
                        output_count += 1
                        outfile.write(merge_line)
                else:
                    output_count += 1
                    outfile.write(line)
                    input_count += 1
            # Continue copying remaining lines from input file after the merge
            for line in infile:
                input_count += 1
                output_count += 1
                outfile.write(line)

        print(f"{input_count} input file records")
        print(f"{merge_count} merge file records")
        print(f"{output_count} output file records")

    except FileNotFoundError as e:
        print(f"Error: One or more files not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
input_file = "06.Project Input File.txt"
merge_file = "06.Project Merge File.txt"
output_file = "06.Project Output File.txt"
merge_files(input_file, merge_file, output_file)