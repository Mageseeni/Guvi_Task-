#1. Calculate the total number of vowels and count of each individual vowel

def count_vowels(string):
    vowels = "AEIOUaeiou"
    count = {v: 0 for v in vowels}
    total = 0
    for char in string:
        if char in vowels:
            count[char] += 1
            total += 1
    return total, count

string = "Guvi Geeks Network Private Limited"
total_vowels, vowel_counts = count_vowels(string)
print("Total vowels:", total_vowels)
print("Vowel counts:", vowel_counts)

#2. Create a pyramid of numbers from 1 to 20 using a for loop

def number_pyramid():
    for i in range(1, 21):
        print(" ".join(str(j) for j in range(1, i + 1)))

number_pyramid()

#3. Return a new string with all vowels removed

def remove_vowels(string):
    vowels = "AEIOUaeiou"
    return "".join(char for char in string if char not in vowels)

string = "Guvi Geeks Network Private Limited"
result = remove_vowels(string)
print("String without vowels:", result)


#4. Return the number of unique characters in a string

def unique_characters_count(string):
    return len(set(string))

string = "Guvi Geeks Network Private Limited"
unique_count = unique_characters_count(string)
print("Number of unique characters:", unique_count)

#5. Check if a string is a palindrome

def is_palindrome(string):
    cleaned = "".join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]

string = "A man a plan a canal Panama"
result = is_palindrome(string)
print("Is palindrome:", result)

#6. Find the longest common substring between two strings

def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    longest = 0
    ending_index = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    ending_index = i

    return s1[ending_index - longest: ending_index]

s1 = "Guvi Geeks"
s2 = "Network Geeks"
result = longest_common_substring(s1, s2)
print("Longest common substring:", result)


#7.Find the most frequent character in a string

from collections import Counter

def most_frequent_character(string):
    counts = Counter(string)
    return counts.most_common(1)[0]

string = "Guvi Geeks Network Private Limited"
most_frequent = most_frequent_character(string)
print("Most frequent character:", most_frequent)


#8. Check if a string is an anagram of another

def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

s1 = "listen"
s2 = "silent"
result = is_anagram(s1, s2)
print("Is anagram:", result)


#9. Return the number of words in a string

def word_count(string):
    return len(string.split())

string = "Guvi Geeks Network Private Limited"
num_words = word_count(string)
print("Number of words:", num_words)



