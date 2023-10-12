from enigma import enigma

en = enigma()
en.position = [0, 0, 0]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

end = False

while not end:
    print('enter letters')
    letters = input().upper()

    output_str = ""

    for letter in letters:
        if letter in alphabet:
            number = alphabet.index(letter)
            index = en.forward(number)
            en.rotation()
            output_str += alphabet[index]
        else:
            output_str += letter
    print(en.position)
    print(output_str)
    