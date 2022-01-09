text = input()
Word = input()

def search(text,Word):
 if text in Word:
    print("Word found")
 else:
    print("Word not found")
search(text,Word)