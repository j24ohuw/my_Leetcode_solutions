MORSE_CODE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
ENGLISH_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
CHAR_TO_MORSE_LOOKUP = {char: MORSE_CODE[i] for i, char in enumerate(ENGLISH_LETTERS)}


class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        unique_transformation_set = set()
        for word in words:
            unique_transformation_set.add(self.translate_word_to_morse_code(word))
        return len(unique_transformation_set)

    def translate_word_to_morse_code(self, word):
        morse_message = ''
        for char in word:
            morse_message += CHAR_TO_MORSE_LOOKUP[char]
        return morse_message