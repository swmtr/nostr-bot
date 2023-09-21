# pre-pend or append text to a line in a file (for all lines in the file)
# create a file example.txt which will contain your text
# run this script and it will create input.txt file with your modifications
with open("example.txt", "r") as infile, open("input.txt", "w") as outfile:
    for line in infile:
        # Append " something" at the end and add "something else " to the start
        modified_line = "Something else " + line.rstrip('\n') + " something\n"
        outfile.write(modified_line)

