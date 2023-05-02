import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.logo)


play_again = True

#ask_again = input('Do you want to play again? type yes or not').lower()

def caesar(text, shift, direction):
  plain_text = ''
  forward = False
  shift = shift % 26
  for letter in text:
    if letter in alphabet:
      if direction.lower() == 'encode':
          new_position = alphabet.index(letter) + shift
      elif direction.lower() == 'decode':
        new_position = alphabet.index(letter) - shift
        forward = False
      new_char = alphabet[new_position]
      plain_text += new_char
    
    else:
      plain_text += letter
      
  if forward:
    print(f'Crypted message is {plain_text}')
  else:
    print(f'The decoded text is {plain_text}')

while play_again:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)

  game_again = input('Do you want to play again? Type "yes" or "no"')
  
  if game_again == 'no':
    play_again = False
    print('Goodbye')



