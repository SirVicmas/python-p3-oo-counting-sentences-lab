#!/usr/bin/env python3

class MyString:
  class MyString:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        if self._value and self._value.endswith('.'):
            return True
        return False

    def is_question(self):
        if self._value and self._value.endswith('?'):
            return True
        return False

    def is_exclamation(self):
        if self._value and self._value.endswith('!'):
            return True
        return False

    def count_sentences(self):
        if not self._value:
            return 0
        sentences = self._value.split('.')
        sentences = [s.strip() for s in sentences if s]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())  # True
print(string.is_question())  # False
print(string.is_exclamation())  # True
print(string.count_sentences())  # 3

