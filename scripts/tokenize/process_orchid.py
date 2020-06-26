"""
Parses the xml conversion of orchid

https://github.com/korakot/thainlp/blob/master/xmlchid.xml
"""

import sys
import xml.etree.ElementTree as ET

# line "122819" has some error in the tokenization of the musical notation
# line "209380" is also messed up
# line "227768"

skipped_lines = {
    "122819",
    "209380",
    "227769",
    "245992",
    "347163",
    "409708",
    "431227",
}

escape_sequences = {
    '<space>': ' ',
    '<left_parenthesis>': '(',
    '<right_parenthesis>': ')',
    '<circumflex_accent>': '^',
    '<full_stop>': '.',
    '<minus>': '-',
    '<asterisk>': '*',
    '<quotation>': '"',
    '<slash>': '/',
    '<colon>': ':',
    '<equal>': '=',
    '<comma>': ',',
    '<semi_colon>': ';',
    '<less_than>': '<',
    '<greater_than>': '>',
    '<ampersand>': '&',
    '<left_curly_bracket>': '{',
    '<right_curly_bracket>': '}',
    '<apostrophe>': "'",
    '<plus>': '+',
    '<number>': '#',
    '<dollar>': '$',
    '<at_mark>': '@',
    '<question_mark>': '?',
    '<exclamation>': '!',
    'app<LI>ances': 'appliances',
    'intel<LI>gence': 'intelligence',
    "<slash>'": "/'",
    '<100>': '100',
}

allowed_sequences = {
    '<a>',
    '<b>',
    '<c>',
    '<e>',
    '<f>',
    '<LI>',
    '<---vp',
    '<---',
    '<----',
}

filename = sys.argv[1]
tree = ET.parse(filename)

# we will put each paragraph in a separate block in the output file
# we won't pay any attention to the document boundaries unless we
# later find out it was necessary
# a paragraph will be a list of sentences
# a sentence is a list of words, where each word is a string
paragraphs = []

root = tree.getroot()
for document in root:
    # these should all be documents
    if document.tag != 'document':
        raise ValueError("Unexpected orchid xml layout: {}".format(document.tag))
    for paragraph in document:
        if paragraph.tag != 'paragraph':
            raise ValueError("Unexpected orchid xml layout: {} under {}".format(paragraph.tag, document.tag))
        sentences = []
        for sentence in paragraph:
            if sentence.tag != 'sentence':
                raise ValueError("Unexpected orchid xml layout: {} under {}".format(sentence.tag, document.tag))
            if sentence.attrib['line_num'] in skipped_lines:
                continue
            words = []
            for word in sentence:
                if word.tag != 'word':
                    raise ValueError("Unexpected orchid xml layout: {} under {}".format(word.tag, sentence.tag))
                word = word.attrib['surface']
                word = escape_sequences.get(word, word)
                if len(word) > 1 and word[0] == '<' and word not in allowed_sequences:
                    raise ValueError("Unknown escape sequence {}".format(word))
                words.append(word)
            sentences.append(words)
        paragraphs.append(sentences)

print(paragraphs[0])

