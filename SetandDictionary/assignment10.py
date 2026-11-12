"""12)write a program to create a dictionary of  words with synonyms,provide
user with an option to search for a word in the dictionary

synonyms = {
     "happy": "joyful",
     "sad": "unhappy",
     "angry": "mad",
     "excited": "enthusiastic"
}
"""
synonyms = {
     "happy": "joyful",
     "sad": "unhappy",
     "angry": "mad",
     "excited": "enthusiastic"
}
world = input("Enter the synonyms word ")
print("The Synonyms for the",world,"is",synonyms[world])