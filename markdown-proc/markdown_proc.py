#!/usr/bin/env python3

from typing import List, Tuple


class MarkdownProc(object):

    LINE_FORMATTING = {
        ' *': ' <span class="italic-text">',
        ' _': ' <span class="italic-text">',
        ' **': ' <span class="bold-text">',
        ' ~~': ' <span class="striked-text">',

        '* ': '</span> ',
        '_ ': '</span> ',
        '** ': '</span> ',
        '~~ ': '</span> ',
    }

    @staticmethod
    def parse_line(line: str) -> str:
        symbol_stack = ['bottom']
        resultant_line = ''
        char_index = 0
        line = ' ' + line + '  '
        while char_index < len(line)-1:
            if line[char_index] + line[char_index+1] + line[char_index+2] in MarkdownProc.LINE_FORMATTING:
                if symbol_stack[-1] == (line[char_index] + line[char_index+1] + line[char_index+2]).strip():
                    symbol_stack.pop(-1)
                    resultant_line += MarkdownProc.LINE_FORMATTING[line[char_index] + line[char_index+1] + line[char_index+2]]
                else:
                    symbol_stack.append((line[char_index] + line[char_index+1] + line[char_index+2]).strip())
                    resultant_line += MarkdownProc.LINE_FORMATTING[line[char_index] + line[char_index+1] + line[char_index+2]]
                char_index += 3
            elif line[char_index] + line[char_index+1]  in MarkdownProc.LINE_FORMATTING:
                if symbol_stack[-1] == (line[char_index] + line[char_index+1]).strip():
                    symbol_stack.pop(-1)
                    resultant_line += MarkdownProc.LINE_FORMATTING[line[char_index] + line[char_index+1]]
                else:
                    symbol_stack.append((line[char_index] + line[char_index+1]).strip())
                    resultant_line += MarkdownProc.LINE_FORMATTING[line[char_index] + line[char_index+1]]
                char_index += 2
            else:
                resultant_line += line[char_index]
                char_index += 1
        return resultant_line.strip()


def ouput_html_for_input_file() -> str:
    return ''


if __name__ == '__main__':
    print(ouput_html_for_input_file())