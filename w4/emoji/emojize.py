import emoji

#prompts the user
user = input("Input: ").strip()

#check  aliases
#outputs the “emojized” version
try:
    print(emoji.emojize(user, language='alias'))
except:
    pass

