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

    LINE_FORMAT = {
        '#': ('<h1>', '</h1>'),
        '##': ('<h2>', '</h2>'),
        '###': ('<h3>', '</h3>'),
        '####': ('<h4>', '</h4>'),
        '#####': ('<h5>', '</h5>'),
        '######': ('<h6>', '</h6>'),
    }

    MULTI_LINE_FORMAT = {
        re.compile('=+'): ('<h1>', '</h1>'),
    }

    current_multiline_formatter = None

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
    def _apply_multi_line_formatting(cls, formatter_symbol, line_to_be_formatted):
        formatted_line = cls.LINE_FORMAT[formatter_symbol][0] + \
                         MarkdownLineProc.parse_line(line_to_be_formatted) + \
                         cls.LINE_FORMAT[formatter_symbol][1]
        return formatted_line

    @classmethod
    def _apply_paragraph_to_be_formatted(cls, line: str) -> str:
        return '<p>' + line + '</p>' if len(line) > 0 else ''

    @classmethod
    def _is_multiline_formatter_symbol(cls, formatter_symbol: str) -> bool:
        return any(multiline_re.match(formatter_symbol) for multiline_re in cls.MULTI_LINE_FORMAT.keys())

    @classmethod
    def parse_doc(cls, document: str) -> str:
        document_lines = document.split('\n')
        resultant_lines = []
        current_block = []
        for line in document_lines:
            if line == '':
                continue
            formatter_symbol = cls._extract_formatter_symbol(line)
            if cls._is_multiline_formatter_symbol(formatter_symbol):
                print(current_block)
                if len(current_block) >= 1:
                    resultant_lines.append(cls._apply_line_formatting(formatter_symbol, current_block[0]))
                    current_block = []
                # TODO check if it exists in multi-line thihngy
                    # TODO the == should be detected only when the current block size is one
                    # TODO same as the above for ---
                    # TODO Any number of lines can be there for *, -, +
                    # TODO Any number of lines can be there for 1. 2. 3. or i. ii. iii.
                    # TODO Store in stack the indentation levels
            elif formatter_symbol in cls.LINE_FORMAT:
                line_to_be_formatted = cls._extract_line_to_be_formatted(line)
                formatted_line = cls._apply_line_formatting(formatter_symbol, line_to_be_formatted)
                previous_paragraph = cls._apply_paragraph_to_be_formatted(' '.join(current_block))
                resultant_lines.append(MarkdownLineProc.parse_line(previous_paragraph))
                resultant_lines.append(formatted_line)
                current_block = []
            else:
                current_block.append(MarkdownLineProc.parse_line(line))
        resultant_lines = [line for line in resultant_lines if line != '']
        return '\n'.join(resultant_lines)


def output_html_for_input_file() -> str:
    return ''


if __name__ == '__main__':
    print(output_html_for_input_file())
