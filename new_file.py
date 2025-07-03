input = "test.txt"
output = "output.txt"
paragraph = ""
i = 1
with open(input) as f:
    for line in f:

        if "Dushyant" in line:
            print(f"\n\n My Name is in line {i} \n\n")
        paragraph += f"{line.strip()} \n"

        i += 1


print(paragraph)
with open(output, "w") as f:
    f.write(paragraph)

