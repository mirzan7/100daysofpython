with open("./input/letters/starting_names.txt", 'r') as format_file:
    format_for_letter = format_file.read()

with open("./input/names/invited_names.txt", 'r') as names:
    names_to_be_added = names.read().strip()
    replacing_name = names_to_be_added.split()

for word in replacing_name:
    print(word)
    formatted = format_for_letter
    formatted = formatted.replace("[name]", word)
    with open(f"./output/ready to share/letter_for_{word}.docx", 'w') as output:
        output.write(formatted)
