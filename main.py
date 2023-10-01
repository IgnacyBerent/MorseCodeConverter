from tkinter import Tk, Label, Button, Entry, END
import pyperclip

morse_code_dict = {
    'A': '.- ', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ', 'I': '.. ',
    'J': '.--- ', 'K': '-.- ', 'L': '.-.. ', 'M': '-- ', 'N': '-. ', 'O': '--- ', 'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
    'S': '... ', 'T': '- ', 'U': '..- ', 'V': '...- ', 'W': '.-- ', 'X': '-..- ', 'Y': '-.-- ', 'Z': '--.. ', ' ': '  ',

    '1': '.---- ', '2': '..--- ', '3': '...-- ', '4': '....- ', '5': '..... ', '6': '-.... ', '7': '--... ', '8': '---.. ',
    '9': '----. ', '0': '----- '
}

morse_to_alpha = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', ' ': ' ',

    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
}

MODE = 0


def setup_interface():
    """
    Setup or refresh the interface based on the MODE.
    """
    if MODE == 0:
        text_l.config(text="Your message:")
        code_l.config(text="Morse code:")
        convert_b.config(text='Encode')
    else:
        text_l.config(text="Your code:")
        code_l.config(text="Message:")
        convert_b.config(text='Decode')


def translate():
    if MODE == 0:
        message = text_e.get().upper()
        letters = list(message)
        code = [morse_code_dict.get(letter, "") for letter in letters]
        translation = ''.join(code)
        morse_e.delete(0, END)
        morse_e.insert(0, translation)
        pyperclip.copy(translation)
    else:
        morse = text_e.get().strip()
        words = morse.replace('   ', '  ').split('  ')
        decoded_words = []

        for word in words:
            letters = word.split()
            translation = ''.join([morse_to_alpha.get(letter, "") for letter in letters])
            decoded_words.append(translation)

        decoded_message = ' '.join(decoded_words)
        morse_e.delete(0, END)
        morse_e.insert(0, decoded_message)
        pyperclip.copy(decoded_message)


def change_mode():
    global MODE
    MODE = 1 if MODE == 0 else 0
    clear()
    setup_interface()


def clear():
    morse_e.delete(0, END)
    text_e.delete(0, END)


def main():
    global text_l, code_l, text_e, morse_e, convert_b
    window = Tk()
    window.title("Morse Code Conventer")
    window.config(pady=40, padx=40)

    text_l = Label(window)
    text_l.grid(row=1, column=1)
    text_e = Entry(width=72)
    text_e.grid(row=1, column=2, columnspan=2)
    text_e.focus()

    code_l = Label(window)
    code_l.grid(row=2, column=1)
    morse_e = Entry(width=72)
    morse_e.grid(row=2, column=2, columnspan=2)

    clear_b = Button(text="Clear", width=47, command=clear)
    clear_b.grid(row=4, column=2, columnspan=2)

    convert_b = Button(width=47, command=translate)
    convert_b.grid(row=3, column=2, columnspan=2)

    change_mode_b = Button(text='Change Mode', width=47, command=change_mode)
    change_mode_b.grid(row=5, column=2, columnspan=2)

    setup_interface()
    window.mainloop()


if __name__ == '__main__':
    main()
