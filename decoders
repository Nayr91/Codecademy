
def caesar_decoder(message, offset):
  return_string = ""
  for i in message:
    if ord(i) < 96:
      i = ord(i)
    elif ord(i) + offset > 122:
      i = (ord(i) + offset) - 26
    else:
      i = ord(i) + offset
    return_string += chr(i)
  return return_string

def caesar_encoder(message, offset):
  return_string = ""
  for i in message:
    if ord(i) < 96:
      i = ord(i)
    elif ord(i) - offset < 96:
      i = (ord(i) - offset) + 26
    else:
      i = ord(i) - offset    
    return_string += chr(i)
  return return_string

def vigenere_decoder(message, key):
  key_len = len(key)
  count = 0
  return_string = ""
  for i in message:
    offset = ord(key[count]) - 97
    if ord(i) < 97:
      i = ord(i)
    elif ord(i) + offset > 122:
      i = (ord(i) + offset) - 26
      count += 1
    else:
      i = ord(i) + offset
      count += 1 
    return_string += chr(i)
    
    if count >= key_len:
      count = 0
  return return_string


def vigenere_encoder(message, key):
  key_len = len(key)
  count = 0
  return_string = ""
  for i in message:
    offset = ord(key[count]) - 97
    if ord(i) < 97:
      i = ord(i)
    elif ord(i) - offset < 97:
      i = (ord(i) - offset) + 26
      count += 1
    else:
      i = ord(i) - offset
      count += 1 
    return_string += chr(i)
    
    if count >= key_len:
      count = 0
  return return_string
