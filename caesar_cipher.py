MAX_KEY_SIZE = 26
def getMessage():
    print('Enter your message:')
    sen = input()
    return sen

def translate(sen, mode, key):
    if mode in 'decrypt':
        key = -key
    ret = ''
    for i in sen:
        if i.isalpha():
            trans = ord(i)+key
            if i.isupper():
                if trans>90:
                    trans -= MAX_KEY_SIZE
                elif trans<65:
                    trans += MAX_KEY_SIZE
            elif i.islower():
                if trans>122:
                    trans -= MAX_KEY_SIZE
                elif trans<97:
                    trans += MAX_KEY_SIZE
        else:
            trans = ord(i)
        ret = ret+chr(trans)
        
    print(ret)
    

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        ans = input()
        if ans.lower() in 'encrypt e'.split():
            return 'encrypt'
        elif ans.lower() in 'decrypt d'.split():
            return 'decrypt'
        elif ans.lower() in 'brute b'.split():
            return 'brute'
        else:
            print('Type "encrypt" or "decrypt" or "brute" or "d" or "e" or "b"!')

def getKey():
    print('Enter your key number (1-%s):'%MAX_KEY_SIZE)
    key = int(input())
    while key not in list(range(1,MAX_KEY_SIZE+1)):
        print('Please enter your key number again (1-%s):'%MAX_KEY_SIZE)
    return key

def again():
    print('Do you want to play again?')
    return input().lower().startswith('y')

playAgain = True
while (playAgain):
    sen = getMessage()
    mode = getMode()
    if mode != 'brute':
        key = getKey()
        translate(sen, mode, key)
    else:
        for key in range(1, MAX_KEY_SIZE+1):
            translate(sen, 'decrypt', key)
    playAgain = again()
