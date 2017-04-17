#!/usr/bin/env python3
from typing import List


class MarkdownLineProc(object):

    LINE_FORMATTING = {
        ' *': ' <span class="italic-text">',
        ' _': ' <span class="italic-text">',
        ' `': ' <code>',
        ' **': ' <span class="bold-text">',
        ' ~~': ' <span class="striked-text">',

        '* ': '</span> ',
        '_ ': '</span> ',
        '` ': '</code> ',
        '** ': '</span> ',
        '~~ ': '</span> ',
    }

    symbol_stack = ['bottom']
    resultant_line = ''
    char_index = 0
    line = ''

    @classmethod
    def _process_markdown_token(cls) -> None:
        token_length_2 = cls.line[cls.char_index] + cls.line[cls.char_index + 1]
        token_length_3 = token_length_2 + cls.line[cls.char_index + 2]
        if token_length_3 in cls.LINE_FORMATTING:
            cls._process_markdown_token_length_3()
        elif token_length_2 in cls.LINE_FORMATTING:
            cls._process_markdown_token_length_2()
        else:
            cls._process_markdown_token_length_1()

    @classmethod
    def _process_markdown_token_length_3(cls) -> None:
        i = cls.char_index
        token = cls.line[i] + cls.line[i + 1] + cls.line[i + 2]
        if cls.symbol_stack[-1] == token.strip():
            cls.symbol_stack.pop(-1)
            cls.resultant_line += cls.LINE_FORMATTING[token]
        else:
            cls.symbol_stack.append(token.strip())
            cls.resultant_line += cls.LINE_FORMATTING[token]
        cls.char_index += 3

    @classmethod
    def _process_markdown_token_length_2(cls) -> None:
        i = cls.char_index
        token = cls.line[i] + cls.line[i + 1]
        if cls.symbol_stack[-1] == token.strip():
            cls.symbol_stack.pop(-1)
            cls.resultant_line += cls.LINE_FORMATTING[token]
        else:
            cls.symbol_stack.append(token.strip())
            cls.resultant_line += cls.LINE_FORMATTING[token]
        cls.char_index += 2

    @classmethod
    def _process_markdown_token_length_1(cls) -> None:
        cls.resultant_line += cls.line[cls.char_index]
        cls.char_index += 1

    @classmethod
    def parse_line(cls, line: str) -> str:
        cls.symbol_stack = ['bottom']
        cls.resultant_line = ''
        cls.char_index = 0
        cls.line = ' ' + line + '  '
        while cls.char_index < len(cls.line)-2:
            cls._process_markdown_token()
        return cls.resultant_line.strip()


class MarkdownDocumentProc(object):

    LINE_FORMAT = {
        '#': ('<h1>', '</h1>'),
        '##': ('<h2>', '</h2>'),
        '###': ('<h3>', '</h3>'),
        '####': ('<h4>', '</h4>'),
        '#####': ('<h5>', '</h5>'),
        '######': ('<h6>', '</h6>'),
    }

    @classmethod
    def _extract_formatter_symbol(cls, line: str) -> str:
        return line.strip().split(' ')[0]

    @classmethod
    def _extract_line_to_be_formatted(cls, line: str) -> str:
        return ' '.join(line.strip().split(' ')[1:])

    @classmethod
    def _apply_line_formatting(cls, formatter_symbol, line_to_be_formatted):
        formatted_line = cls.LINE_FORMAT[formatter_symbol][0] + \
                         MarkdownLineProc.parse_line(line_to_be_formatted) + \
                         cls.LINE_FORMAT[formatter_symbol][1]
        return formatted_line

    @classmethod
    def parse_doc(cls, document: str) -> str:
        document_lines = document.split('\n')
        lines = []
        for line in document_lines:
            formatter_symbol = cls._extract_formatter_symbol(line)
            if formatter_symbol in cls.LINE_FORMAT:
                line_to_be_formatted = cls._extract_line_to_be_formatted(line)
                formatted_line = cls._apply_line_formatting(formatter_symbol, line_to_be_formatted)
                lines.append(formatted_line)
        return '\n' + '\n'.join(lines) + '\n'


def output_html_for_input_file() -> str:
    return ''


if __name__ == '__main__':
    print(output_html_for_input_file())
