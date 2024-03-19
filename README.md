# Overview
This script is designed to take a UTF-8 text transcript file and figure out how many filler words are used by each speaker.

Currently detected filler words are:
```
filler_words = ["uh", "um", "you know", "like"]
```
#  Input File Format
The file is depending on a format like:
```
Speaker1FirstName Speaker2LastName: This is where the words Speaker1FirstName spoke would go.
```
# Shortcomings
There are no unit tests on this code. 

# What's Next?
* It would be nice to have a configuration file that can be used as input. 
* It might also be fun to make it run in Azure cloud.
* Lastly, the transcript I get from Descript contians the file name as the first row. Currently, that line has to be deleted. Perhaps improving this to ignore any file rows that don't start with the format "Speaker1FirstName Speaker2LastName:" would be good.
* How could "right" be included, since sometimes it is legitimate. Sometimes it is a filler word. 
