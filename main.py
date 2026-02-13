morse_list = {
    "A": ".-", #v,k
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}


def decrypt(msg=""):
    msg_decrypt = ""
    msg = msg.split(" ")
    inverted_list = {v: k for k, v in morse_list.items()}
    for n in msg:
        if n == "":
            continue
        ch = inverted_list[n]
        msg_decrypt += ch
    return msg_decrypt

def encrypt(msg=""):
    msg_encrypted = ""
    for char in msg:
        ch = morse_list[char]        
        msg_encrypted += ch + " "
    return msg_encrypted

while True:
    try:
        message = str(input("Your message: "))
        def ask():
            selection = int(input("[1] encrypt \n[2] decrypt:\nSelection: "))
            if selection < 1 or selection > 2:
                    selection = ask()
            return selection
        selection = ask()
        if selection == 1:
            print(encrypt(message.upper()))
        else:
            print(decrypt(message))
    except KeyboardInterrupt:
        print("\Have a nice day, bye <3")
        exit()
