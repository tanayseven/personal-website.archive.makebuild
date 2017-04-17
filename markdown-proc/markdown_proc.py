#!/usr/bin/env python3

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
    @classmethod
    def parse_doc(cls, document: str) -> str:
        pass


def output_html_for_input_file() -> str:
    return ''


if __name__ == '__main__':
    print(output_html_for_input_file())
