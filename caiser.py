word = "vwxyz"
print("the Real word :" + word)

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

word_index = []
new_word = []
for i in word :
    word_index.append(alphabet.index(i))
for i in word_index:
    key_word = i+3
    if (key_word > 25):
        key_word = key_word - 26
    if key_word == 26:
        key_word -= 1
    new_word.append(alphabet[key_word])
print ("the cipher :"+''.join(new_word))

cipher_index = []
plain_text = []
for i in new_word:
    cipher_index.append(alphabet.index(i))
for i in cipher_index:
    key_word = i - 3
    if key_word < 0 :
        key_word = key_word +26
    plain_text.append(alphabet[key_word])
print("plain text :"+ ''.join(plain_text))