import unittest

from buzz import generator

def test_sample_single_word():
    t = ('foo', 'bar', 'foobar')
    word = generator.sample(t)
    assert word in t

def test_sample_multiple_words():
    t = ('foo', 'bar', 'foobar')
    words = generator.sample(t, 2)
    assert len(words) == 2
    assert words[0] in t
    assert words[1] in t
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 8