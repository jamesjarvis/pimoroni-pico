import json
import random

text_file = "quotes.txt"
TEXT_WIDTH = 50

# Open the book file
quotes = open(text_file, "r")

# read ahead to quote at number n
n = random.randint(0, 2042)
for i in range(n):
  quotes.readline()

current_quote_json = json.loads(quotes.readline())
# Read a full line and split it into words.
words = current_quote_json["content"].split(" ")

lines = []
latest_line = ""
for word in words:
    latest_line_length = len(latest_line)
    if latest_line_length >= TEXT_WIDTH:
        lines.append(latest_line)
        latest_line = ""
    latest_line += word
    latest_line += " "

lines.append(latest_line)

lines.append(current_quote_json["author"])

for line in lines:
  print(line)