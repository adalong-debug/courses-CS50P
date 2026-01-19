def convert(user_input):
    user_input_convert = user_input.replace(":)", "🙂").replace(":(", "🙁")
    return user_input_convert

def main():
    prompt = '''input some words with a emoticon from the following 2 choices.
    :) was a happy face and text like :( was a sad face.
    now your words: '''

    user_input = input(prompt)
    print(convert(user_input))

main()
