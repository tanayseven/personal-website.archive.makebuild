import pytest
from hamcrest import *

from markdown_proc import MarkdownProc

class TestWordFormatting(object):

    def test_input_word_with_asterisk_is_marked_as_italic(self):
        input_word = '*a_single*word*with_no_spaces*'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a_single*word*with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_asterisk_is_marked_as_italic(self):
        input_word = '*a set of words with spaces*'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_asterisks_is_marked_as_italic(self):
        input_word = 'multiple *italic* markings *throughout the line*'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'multiple <span class="italic-text">italic</span> markings <span class="italic-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_underscore_is_marked_as_italic(self):
        input_word = '_a_single_word_with_no_spaces_'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a_single_word_with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_underscore_is_marked_as_italic(self):
        input_word = '_a set of words with spaces_'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_underscores_is_marked_as_italic(self):
        input_word = 'multiple _italic_ markings _throughout the line_'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'multiple <span class="italic-text">italic</span> markings <span class="italic-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_asterisk_is_marked_as_bold(self):
        input_word = '**a_single**word**with_no_spaces**'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="bold-text">a_single**word**with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_asterisk_is_marked_as_bold(self):
        input_word = '**a set of words with spaces**'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="bold-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_asterisk_is_marked_as_bold(self):
        input_word = 'multiple **bold** markings **throughout the line**'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'multiple <span class="bold-text">bold</span> markings <span class="bold-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_tilde_is_marked_as_strike(self):
        input_word = '~~a_single~~word~~with_no_spaces~~'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="striked-text">a_single~~word~~with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_tilde_is_marked_as_strikethrough(self):
        input_word = '~~a set of words with spaces~~'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = '<span class="striked-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_tilde_is_marked_as_strikethrough(self):
        input_word = 'multiple ~~bold~~ markings ~~throughout the line~~'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'multiple <span class="striked-text">bold</span> markings <span class="striked-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_grave_is_marked_as_code(self):
        input_word = 'some `code` in a line'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'some <code>code</code> in a line'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_grave_is_marked_as_code(self):
        input_word = 'a set of words `that are code` with spaces'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'a set of words <code>that are code</code> with spaces'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_grave_tilde_is_marked_as_code(self):
        input_word = 'multiple `code` markings `throughout the line`'
        output_html = MarkdownProc.parse_line(input_word)
        expected_html = 'multiple <code>code</code> markings <code>throughout the line</code>'
        assert_that(output_html, is_(expected_html))