#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=None):
    self._value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value,str) and 1 <= len(value) <=25:
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    '''Returns True if value ends with a period and False otherwise.'''
    return self.value.endswith(".")
  
  def is_question(self):
    '''Returns True if value ends with a period and False otherwise.'''
    return self.value.endswith("?")
  
  def is_exclamation(self):
    '''Returns True if value ends with a period and False otherwise.'''
    return self.value.endswith("!")
  
  def count_sentences(self):
    '''Returns  the number of sentences in the value.'''
    if self.value is None:
      return 0
    else:
        sentences = re.split(r'[.!?]+', self.value)
        non_empty_sentences = [sentence for sentence in sentences if len(sentence.strip()) > 0]
        return len(non_empty_sentences)