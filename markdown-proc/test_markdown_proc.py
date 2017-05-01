import pytest
from hamcrest import *

from markdown_proc import MarkdownLineProc, MarkdownDocumentProc

tag = {
    "single-asterisk": ('<span class="single-asterisk">', '</span>'),
    "single-under": ('<span class="single-under">', '</span>'),
    "single-grave": ('<code class="single-grave">', '</code>'),
    "double-asterisk": ('<span class="double-asterisk">', '</span>'),
    "double-tilde": ('<span class="double-tilde">', '</span>'),
}


class TestLineFormatting(object):

    def test_input_sentence_which_has_no_formatting_should_be_returned_as_it_is(self) -> None:
        input_word = 'some sentence with no formatting'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = input_word
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_asterisk_is_marked_as_italic(self) -> None:
        input_word = '*a_single*word*with_no_spaces*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['single-asterisk'][0] + 'a_single*word*with_no_spaces'+tag['single-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_asterisk_is_marked_as_italic(self) -> None:
        input_word = '*a set of words with spaces*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['single-asterisk'][0] + 'a set of words with spaces' + tag['single-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_asterisks_is_marked_as_italic(self) -> None:
        input_word = 'multiple *italic* markings *throughout the line*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple ' + tag['single-asterisk'][0] +'italic'+ tag['single-asterisk'][1] +\
                        ' markings ' + tag['single-asterisk'][0] +'throughout the line' + tag['single-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_underscore_is_marked_as_italic(self) -> None:
        input_word = '_a_single_word_with_no_spaces_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['single-under'][0] + 'a_single_word_with_no_spaces' + tag['single-under'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_underscore_is_marked_as_italic(self) -> None:
        input_word = '_a set of words with spaces_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['single-under'][0] + 'a set of words with spaces' + tag['single-under'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_underscores_is_marked_as_italic(self) -> None:
        input_word = 'multiple _italic_ markings _throughout the line_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple ' + tag['single-under'][0] + 'italic' + tag['single-under'][1] +\
                        ' markings ' + tag['single-under'][0] + 'throughout the line' + tag['single-under'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = '**a_single**word**with_no_spaces**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['double-asterisk'][0] + 'a_single**word**with_no_spaces' + tag['double-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = '**a set of words with spaces**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['double-asterisk'][0] + 'a set of words with spaces' + tag['double-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = 'multiple **bold** markings **throughout the line**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple ' + tag['double-asterisk'][0] + 'bold'+ tag['double-asterisk'][1] +\
                        ' markings '+ tag['double-asterisk'][0] +'throughout the line' + tag['double-asterisk'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_tilde_is_marked_as_strike(self) -> None:
        input_word = '~~a_single~~word~~with_no_spaces~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['double-tilde'][0] + 'a_single~~word~~with_no_spaces' + tag['double-tilde'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_tilde_is_marked_as_strikethrough(self) -> None:
        input_word = '~~a set of words with spaces~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = tag['double-tilde'][0] + 'a set of words with spaces' + tag['double-tilde'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_tilde_is_marked_as_strikethrough(self) -> None:
        input_word = 'multiple ~~bold~~ markings ~~throughout the line~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple ' + tag['double-tilde'][0] + 'bold' + tag['double-tilde'][1] + \
                        ' markings ' + tag['double-tilde'][0] + 'throughout the line' + tag['double-tilde'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_grave_is_marked_as_code(self) -> None:
        input_word = 'some `code` in a line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'some ' + tag['single-grave'][0] + 'code' + tag['single-grave'][1] + ' in a line'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_grave_is_marked_as_code(self) -> None:
        input_word = 'a set of words `that are code` with spaces'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'a set of words ' + tag['single-grave'][0] + 'that are code' + tag['single-grave'][1] + \
                        ' with spaces'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_grave_is_marked_as_code(self) -> None:
        input_word = 'multiple `code` markings `throughout the line`'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple ' + tag['single-grave'][0] + 'code' + tag['single-grave'][1] + ' markings ' \
                        + tag['single-grave'][0] + 'throughout the line' + tag['single-grave'][1]
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_nested_grave_and_tilde(self) -> None:
        input_word = 'this set of words `have grave ~~and tilde~~ in` one line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'this set of words ' + tag['single-grave'][0] + 'have grave ' + tag['double-tilde'][0] + \
                        'and tilde' + tag['double-tilde'][1] + ' in' + tag['single-grave'][1] + ' one line'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_nested_underscore_and_bold(self) -> None:
        input_word = 'this set of words _have bold **and italic** in_ one line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'this set of words ' + tag['single-under'][0] + 'have bold ' + tag['double-asterisk'][0] + \
                        'and italic' + tag['double-asterisk'][1] + ' in' + tag['single-under'][1] + ' one line'
        assert_that(output_html, is_(expected_html))


line_tag = MarkdownDocumentProc.LINE_FORMAT


class TestDocumentFormatting(object):
    def test_input_document_with_single_hash_for_heading_text(self) -> None:
        input_document = """
        # This is an h1 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h1 heading{1}""".format(line_tag['#'][0], line_tag['#'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_two_hash_for_heading_text(self) -> None:
        input_document = """
        ## This is an h2 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h2 heading{1}""".format(line_tag['##'][0], line_tag['##'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_three_hash_for_heading_text(self) -> None:
        input_document = """
        ### This is an h3 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h3 heading{1}""".format(line_tag['###'][0], line_tag['###'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_four_hash_for_heading_text(self) -> None:
        input_document = """
        #### This is an h4 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h4 heading{1}""".format(line_tag['####'][0], line_tag['####'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_five_hash_for_heading_text(self) -> None:
        input_document = """
        ##### This is an h5 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h5 heading{1}""".format(line_tag['#####'][0], line_tag['#####'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_six_hash_for_heading_text(self) -> None:
        input_document = """
        ###### This is an h6 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h6 heading{1}""".format(line_tag['######'][0], line_tag['######'][1])
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_multiple_heading_lines(self) -> None:
        input_document = """
        ###### This is an h6 heading
        ## This is a h2 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """{0}This is an h6 heading{1}\n{2}This is a h2 heading{3}""".format(
            line_tag['######'][0],
            line_tag['######'][1],
            line_tag['##'][0],
            line_tag['##'][1],
        )
        assert_that(output_html, is_(expected_html))

    @pytest.mark.skip(reason="This implementation is currently in progress")
    def test_input_document_with_equals_symbol_for_heading_line(self) -> None:
        input_document = """
        This is h1 heading
        ==================
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """<h1>This is h1 heading</h1>"""
        assert_that(output_html, is_(expected_html))
