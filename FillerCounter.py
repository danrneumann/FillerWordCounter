# Import necessary library
import re
import os

# Define a function to count filler words for a given speaker's text
def count_filler_words(text, filler_words):
    count = {word.strip(): text.lower().count(f"{word}") for word in filler_words}
    return count

#For the current dictionary, add the new counts
def update_filler_word_counts(current_counts, new_counts):
    for word, count in new_counts.items():
        if word in current_counts:
            current_counts[word] += count
        else:
            current_counts[word] = count
 
#This function is intended to disregard lines that are at the beginning of the transcript but do not start with the expected format of "SpeakerFirstName SpeakerLastName:"
def find_first_speaker_line(list_of_parts):
    # This pattern looks for strings that start with any word (word1),
    # followed by another word (word2), and ending with a colon.
    pattern = r'^\w+ \w+:'
    # Loop through the list of parts passed in and return the index of the first speaker
    for i in range(0, len(list_of_parts)):
        #if the speaker format is matched, break. If it is not matched, continue.
        if re.match(pattern, list_of_parts[i]):
            return(i)
    # return -1 if no speaker was found
    return -1

# List of filler words you're interested in
filler_words = ["uh", "um", "you know", "like"]
#print (filler_words)

# Initialize a dictionary to hold the count of filler words by speaker
speaker_filler_word_counts = {}

#Get Current Path to terminal
#current_directory = os.getcwd()
#print(current_directory)

# Read the transcript file
# use to be 'transcript.txt' now /Users/dan.neumann/Documents/PythonProjects/FillerCounter/Data/transcript.txt
with open('./SampleTranscript.txt', 'r', encoding='utf-8') as file:
    transcript = file.read()

# Assuming each speaker segment in the transcript starts with "Speaker Name:"
# Split the transcript into segments by speaker
segments = re.split(r'(\w+ \w+):', transcript)  # Adjust regex based on your transcript format

# Process each segment
for i in range(1, len(segments), 2):
    speaker = segments[i].strip()
#    print(speaker)
    speech = segments[i + 1].strip()
#    print(speech)
    new_segment_counts = count_filler_words(speech, filler_words)
    # Assuming speaker_filler_word_counts is your main dictionary holding all counts
    # and new_segment_counts is the count from the latest segment you processed
    if speaker not in speaker_filler_word_counts:
        speaker_filler_word_counts[speaker] = {word: 0 for word in filler_words}

    update_filler_word_counts(speaker_filler_word_counts[speaker], new_segment_counts)
    # speaker_filler_word_counts[speaker] = count_filler_words(speech, filler_words)

# Print the filler word counts for each speaker
for speaker, counts in speaker_filler_word_counts.items():
    print(f"{speaker}: {counts}")
