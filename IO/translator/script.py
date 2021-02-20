from translate import Translator

translator = Translator(to_lang="ja")

try: 
    with open('./data/test.txt',mode='r') as myFile:
        text = myFile.read()
        translation = translator.translate(text)
        with open('./data/test-ja.txt',mode='w') as myFile2:
            myFile2.write(translation)

except FileNotFoundError as err:
    print('check your file path!')