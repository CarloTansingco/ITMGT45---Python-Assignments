#Code 1
def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    if letter == ' ':
        return ' '
    
    letter = letter.upper()

    letter_code = ord(letter)

    if 'A' <= letter <= 'Z':
        shifted_code = (letter_code - ord('A') + shift) % 26 + ord('A')
        return chr(shifted_code)
    else:
        return letter
shifted_letter = shift_letter("A", 5)
print (shifted_letter)
#Example


#Code 2
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26  
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            else:
                encrypted_char = char
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message
cc_encrypted_message = caesar_cipher("HELLO WORLD", 3)
print("The deciphered message is ", encrypted_message)
#Example


#Code 3
def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    
    shift_value = ord(letter_shift) - ord('A')
    
    shifted_letter = chr(((ord(letter) - ord('A') + shift_value) % 26) + ord('A'))

    return shifted_letter
shifted_letter = shift_by_letter("B", "E")
print (shifted_letter)
#Example


#Code 4
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    result = ""
    
    message = message.upper()
    key = key.upper()

    for i in range(len(message)):
        if message[i] == ' ':  
            result += ' '
        else:
            key_char = key[i % len(key)]  
            shift = ord(key_char) - ord('A')
            
            shifted_char = chr(((ord(message[i]) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char

    return result   
vc_encrypted_message = vigenere_cipher("HELLO WORLD", "KEY")
print("The deciphered message is ", vc_encrypted_message)
#Example