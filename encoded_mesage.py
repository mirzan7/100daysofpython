def encrypt_message(plain_text,shift_amount,alphabet):
    encrypted_text = ""
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position + shift_amount
        if(new_position > 26):
            new_position = new_position % 26
        new_letter = alphabet[new_position]
        encrypted_text += new_letter
    print(encrypted_text)

def decrypt_message(plain_text,shift_amount,alphabet):
    decrpted_text  = ""
    for letters in plain_text:
        posittion = alphabet.index(letters)
        new_position = posittion - shift_amount
        if(new_position < 1):
            new_position = 26 - abs(new_position)
        new_letter = alphabet[new_position]
        decrpted_text += new_letter
    print(decrpted_text)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input("Enter the message you want to encrypt   :")
shift = int(input("shift   :"))
encrypt_message(message,shift,alphabet)
message1 = input("Enter the text you want to decrypt  :")
shift1 = int(input("shift value   :"))
decrypt_message(message1,shift1,alphabet)