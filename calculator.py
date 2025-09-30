word1 = "TRUE"
combined_names = "ANGELAYUJACKBAUER"

true_count = 0

for letter in word1:
    for char in combined_names:
        if char in letter:
            true_count += 1

word2 = "LOVE"
combined_names = "ANGELAYUJACKBAUER"

love_count = 0

for letter in word2:
    for char in combined_names:
        if char in letter:
            love_count += 1

print(f"Total Score:{true_count}{love_count}")