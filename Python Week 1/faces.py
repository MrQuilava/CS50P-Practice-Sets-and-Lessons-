

def main():
    sentences = input("Input a Sentence: ")
    sentences = convert(sentences)
    print(sentences)

def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

main()
