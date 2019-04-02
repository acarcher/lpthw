from ex48 import parser
import unittest


class TestParser(unittest.TestCase):

    def test_sentence(self):
        sentence = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'cake'))
        self.assertEqual(sentence.subject, 'bear')
        self.assertEqual(sentence.verb, 'eat')
        self.assertEqual(sentence.object, 'cake')

    def test_peek(self):
        self.assertEqual(parser.peek([]), None)
        self.assertEqual(parser.peek([('verb', 'hit'), ('noun', 'log')]), 'verb')

    def test_match(self):
        self.assertEqual(parser.match([], 'noun'), None)
        self.assertEqual(parser.match([('verb', 'dash'), ('noun', 'door')], 'noun'), None)
        self.assertEqual(parser.match([('verb', 'watch'), ('noun', 'bird')], 'verb'),
                         ('verb', 'watch'))

    def test_skip(self):
        word_list = [('stop', 'the'), ('noun', 'floor')]
        parser.skip(word_list, 'stop')
        self.assertEqual(word_list, [('noun', 'floor')])

    # SUBJECT VERB OBJECT

    def test_parse_verb(self):
        self.assertRaises(parser.ParserError, parser.parse_verb, [('noun', 'phone')])
        self.assertEqual(parser.parse_verb([('verb', 'drink')]), ('verb', 'drink'))

    def test_parse_object(self):
        self.assertRaises(parser.ParserError, parser.parse_object, [('verb', 'flies')])
        self.assertEqual(parser.parse_object([('noun', 'paper')]), ('noun', 'paper'))
        self.assertEqual(parser.parse_object([('direction', 'north')]), ('direction', 'north'))

    def test_parse_subject(self):
        self.assertRaises(parser.ParserError, parser.parse_subject, [('stop', 'it')])
        self.assertEqual(parser.parse_subject([('noun', 'tree')]), ('noun', 'tree'))
        self.assertEqual(parser.parse_subject([('verb', 'think')]), ('noun', 'player'))

    def test_parse_sentence(self):
        self.addTypeEqualityFunc(parser.Sentence, sentence_eq)
        self.assertEqual(parser.parse_sentence([('noun', 'ratman'),
                                                ('verb', 'eats'),
                                                ('noun', 'cake')]),
                         parser.Sentence(('noun', 'ratman'),
                                         ('verb', 'eats'),
                                         ('noun', 'cake')))


def sentence_eq(expected_sentence, actual_sentence, msg=None):
    if (expected_sentence.subject != actual_sentence.subject or
            expected_sentence.verb != actual_sentence.verb or
            expected_sentence.object != actual_sentence.object):

        msg = '{} != {}. {}'.format(expected_sentence, actual_sentence, msg or '')
        raise AssertionError(msg)
