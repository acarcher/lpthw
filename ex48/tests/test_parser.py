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
        self.assertEqual(parser.match([('verb', 'dash'), ('noun', 'door')], 'verb'), ('verb', 'dash'))

    def test_skip(self):
        word_list = [('stop', 'the'), ('noun', 'door')]
        parser.skip(word_list, 'stop')
        self.assertEqual(word_list, [('noun', 'door')])

    # SUBJECT VERB OBJECT

    def test_parse_verb(self):
        self.assertRaises(parser.ParserError, parser.parse_verb, [('noun', 'phone')])
        self.assertEqual()

    def test_parse_object(self):
        self.assertRaises(parser.ParserError, parser.parse_object, [('verb', 'flies')])

    def test_parse_subject(self):
        self.assertRaises(parser.ParserError, parser.parse_subject, [('stop', 'it')])

    def test_parse_sentence(self):
        pass
