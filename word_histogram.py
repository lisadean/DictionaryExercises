################################################################################
# Functions
def strip_period(text):
    stripped_text = ""
    for c in text:
        if c != ".":
            stripped_text += c
    return stripped_text


def create_histogram(text):
    text = strip_period(text)

    word_list = text.split()

    histogram = {}
    for word in word_list:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] = histogram[word] + 1
    return histogram


def find_top_word(histogram):
    new_dict = {}
    max = 0
    for key, value in histogram.items():
        if len(new_dict) == 0:
            new_dict[key] = value
            max = value
        elif value > max:
            new_dict = {key : value}
            max = value
    return new_dict


def remove_pair(dict1, pair_to_remove):
    for key in pair_to_remove.keys():
        del dict1[key]
    return dict1


def find_top_words(histogram, num):
    new_histogram = {}
    for i in range(num):
        top_histogram = find_top_word(histogram)
        new_histogram.update(top_histogram)
        histogram = remove_pair(histogram, top_histogram)
    return new_histogram


def print_dictionary(histogram):
    for key, value in histogram.items():
        print("%s: %d" % (key, value))


################################################################################
# Variables
# text = input("Please enter a sentence: ")
# text = "This is a sentence with a duplicate word, this is."
# text = "To be or not to be."
text = "repeat word repeat repeat dog cat cat cat cat word"

################################################################################
# Script

# text = text.lower()

histogram = create_histogram(text)

print_dictionary(histogram)
print()

qty = 3
print("Top %d words:" % qty)
print_dictionary(find_top_words(histogram, qty))