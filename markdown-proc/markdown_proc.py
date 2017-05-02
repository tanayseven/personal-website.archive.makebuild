#!/usr/bin/env python3
import re
from typing import List


class MarkdownLineProc(object):

    LINE_FORMATTING = {
        ' *': ' <span class="single-asterisk">',
        ' _': ' <span class="single-under">',
        ' `': ' <code class="single-grave">',
        ' **': ' <span class="double-asterisk">',
        ' ~~': ' <span class="double-tilde">',

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

    ONE_LINE_FORMAT = {
        '#': ('<h1>', '</h1>'),
        '##': ('<h2>', '</h2>'),
        '###': ('<h3>', '</h3>'),
        '####': ('<h4>', '</h4>'),
        '#####': ('<h5>', '</h5>'),
        '######': ('<h6>', '</h6>'),
    }

    TWO_LINE_FORMAT = {
        '--': ('REGEXP', '<h1>', '</h1>'),
        '==': ('REGEXP', '<h2>', '</h2>'),
    }

    current_multiline_formatter = None
    document_lines = []
    resultant_lines = []
    previous_indent = 0
    formatter_symbol = ''
    current_indent = 0
    previous_paragraph = ''
    formatted_line = ''
    current_block = []

    @classmethod
    def _initialize_fields(cls, document):
        cls.document_lines = document.split('\n')
        cls.resultant_lines = []
        cls.previous_indent = 0
        cls.previous_paragraph = ''
        cls.current_indent = 0
        cls.current_block = []

    @classmethod
    def _extract_formatter_symbol(cls, line: str) -> (str, int):
        return line.strip().split(' ')[0], len(line) - len(line.lstrip(' '))

    @classmethod
    def _extract_line_to_be_formatted(cls, line: str) -> str:
        return ' '.join(line.strip().split(' ')[1:])

    @classmethod
    def _apply_one_line_formatting(cls, formatter_symbol: str, line_to_be_formatted: str):
        formatted_line = cls.ONE_LINE_FORMAT[formatter_symbol][0] + \
                         MarkdownLineProc.parse_line(line_to_be_formatted) + \
                         cls.ONE_LINE_FORMAT[formatter_symbol][1]
        return formatted_line

    @classmethod
    def _apply_multi_line_formatting(cls, formatter_symbol: str, line_to_be_formatted: str):
        formatted_line = cls.ONE_LINE_FORMAT[formatter_symbol][0] + \
                         MarkdownLineProc.parse_line(line_to_be_formatted) + \
                         cls.ONE_LINE_FORMAT[formatter_symbol][1]
        return formatted_line

    @classmethod
    def _apply_paragraph_to_be_formatted(cls, line: str) -> str:
        return '<p>' + line + '</p>' if len(line) > 0 else ''

    @classmethod
    def _apply_one_line_format(cls, line: str):
        cls.line_to_be_formatted = cls._extract_line_to_be_formatted(line)
        cls.formatted_line = cls._apply_one_line_formatting(cls.formatter_symbol, cls.line_to_be_formatted)
        cls.previous_paragraph = cls._apply_paragraph_to_be_formatted(' '.join(cls.current_block))
        cls._append_to_result()

    @classmethod
    def _append_to_result(cls):
        cls.resultant_lines.append(MarkdownLineProc.parse_line(cls.previous_paragraph))
        cls.resultant_lines.append(cls.formatted_line)
        cls.current_block = []
        cls.previous_paragraph = ''

    @classmethod
    def parse_doc(cls, document: str) -> str:
        cls._initialize_fields(document)
        for line in cls.document_lines:
            cls.formatter_symbol, cls.current_indent = cls._extract_formatter_symbol(line)
            if cls.formatter_symbol in cls.ONE_LINE_FORMAT:
                cls._apply_one_line_format(line)
            else:
                cls.current_block.append(MarkdownLineProc.parse_line(line))
        resultant_lines = [line for line in cls.resultant_lines if line != '']
        return '\n'.join(resultant_lines)


def output_html_for_input_file() -> str:
    return ''


if __name__ == '__main__':
    print(output_html_for_input_file())
