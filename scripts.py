import time
import os
from collections import Counter
import socket

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words), Counter(words)

# Function to handle contractions
def handle_contractions(text):
    contractions = {"I'm": "I am", "can't": "cannot", "don't": "do not"}  # Extend this list
    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    return text

# Define the paths to the text files
file1_path = '/home/data/IF.txt'
file2_path = '/home/data/AlwaysRememberUsThisWay.txt'

# Count words in IF.txt
word_count1, counter1 = count_words_in_file(file1_path)
# Top 3 frequent words in IF.txt
top3_if = counter1.most_common(3)

# Handle contractions and count words in AlwaysRememberUsThisWay.txt
with open(file2_path, 'r') as file2:
    text = file2.read()
processed_text = handle_contractions(text)
word_count2, counter2 = count_words_in_file(file2_path)
top3_ar = counter2.most_common(3)

# Calculate total words across both files
total_words = word_count1 + word_count2

# Get the IP address of the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write the results to /home/data/output/result.txt
output_path = '/home/data/output/result.txt'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as output_file:
    output_file.write(f"Total words in IF.txt: {word_count1}\n")
    output_file.write(f"Total words in AlwaysRememberUsThisWay.txt: {word_count2}\n")
    output_file.write(f"Grand total of words: {total_words}\n")
    output_file.write(f"Top 3 words in IF.txt: {top3_if}\n")
    output_file.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top3_ar}\n")
    output_file.write(f"IP address of container: {ip_address}\n")

# Print the results to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())

time.sleep(3600)
