import random

words = ["bad","good","happy","sad","year","day"]   #قائمة الكلمات العشوائية
word = random.choice(words)#الكلمة الي الكومبيوتر مختارها

chance = 6
guessed_list = []

hidden_word = list(len(word)*"_") #list تضم _____

#طالما في أل hidden _ اذا نفذ الكود بلوك
while "_" in hidden_word and chance != 0: 
	guessed = input("Enter your guess: ").lower()

	
	for pos in range(len(word)):
		if word[pos] == guessed: #if guessed correct
			hidden_word[pos] = guessed 
			if guessed in guessed_list:
				print("\nYou entered same charcter before!")
	if guessed not in word.lower():
		chance = chance - 1
	str_hidden_word = " ".join(hidden_word)
	print(f"you have [{chance}] more chances\n")
	print(str_hidden_word)		
	guessed_list.append(guessed)

if chance == 0:
	print("\nlose!\n"+
	"""=========
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")
else:
	print("\n************\nwin\n*************")
