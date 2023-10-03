import csv

# Define the input and output file paths
input_file = 'de_50k.txt'
output_file = 'de_50k.csv'

with open(input_file, 'r') as f:
    lines = f.readlines()

# Create a list to store the word-frequency pairs
word_freq_pairs = []

# Iterate through the lines and split each line into word and frequency
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        word = parts[0]
        frequency = parts[1]
        word_freq_pairs.append((word, frequency))

# Write the word-frequency pairs to the CSV file
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header row
    csv_writer.writerow(['Word', 'Frequency'])
    # Write the word-frequency pairs
    csv_writer.writerows(word_freq_pairs)

print(f"CSV file '{output_file}' has been created.")
