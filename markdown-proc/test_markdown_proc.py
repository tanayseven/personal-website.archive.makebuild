from hamcrest import *

from markdown_proc import MarkdownLineProc, MarkdownDocumentProc

class TestLineFormatting(object):

    def test_input_sentence_which_has_no_formatting_should_be_returned_as_it_is(self) -> None:
        input_word = 'some sentence with no formatting'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = input_word
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_asterisk_is_marked_as_italic(self) -> None:
        input_word = '*a_single*word*with_no_spaces*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a_single*word*with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_asterisk_is_marked_as_italic(self) -> None:
        input_word = '*a set of words with spaces*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_asterisks_is_marked_as_italic(self) -> None:
        input_word = 'multiple *italic* markings *throughout the line*'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple <span class="italic-text">italic</span> markings <span class="italic-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_underscore_is_marked_as_italic(self) -> None:
        input_word = '_a_single_word_with_no_spaces_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a_single_word_with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_underscore_is_marked_as_italic(self) -> None:
        input_word = '_a set of words with spaces_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="italic-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_underscores_is_marked_as_italic(self) -> None:
        input_word = 'multiple _italic_ markings _throughout the line_'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple <span class="italic-text">italic</span> markings <span class="italic-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = '**a_single**word**with_no_spaces**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="bold-text">a_single**word**with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = '**a set of words with spaces**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="bold-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_asterisk_is_marked_as_bold(self) -> None:
        input_word = 'multiple **bold** markings **throughout the line**'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple <span class="bold-text">bold</span> markings <span class="bold-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_double_tilde_is_marked_as_strike(self) -> None:
        input_word = '~~a_single~~word~~with_no_spaces~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="striked-text">a_single~~word~~with_no_spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_double_tilde_is_marked_as_strikethrough(self) -> None:
        input_word = '~~a set of words with spaces~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = '<span class="striked-text">a set of words with spaces</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_double_tilde_is_marked_as_strikethrough(self) -> None:
        input_word = 'multiple ~~bold~~ markings ~~throughout the line~~'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple <span class="striked-text">bold</span> markings <span class="striked-text">throughout the line</span>'
        assert_that(output_html, is_(expected_html))

    def test_input_word_with_grave_is_marked_as_code(self) -> None:
        input_word = 'some `code` in a line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'some <code>code</code> in a line'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_grave_is_marked_as_code(self) -> None:
        input_word = 'a set of words `that are code` with spaces'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'a set of words <code>that are code</code> with spaces'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_multiple_grave_is_marked_as_code(self) -> None:
        input_word = 'multiple `code` markings `throughout the line`'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'multiple <code>code</code> markings <code>throughout the line</code>'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_nested_grave_and_tilde(self) -> None:
        input_word = 'this set of words `have grave ~~and tilde~~ in` one line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'this set of words <code>have grave <span class="striked-text">and tilde</span> in</code> one line'
        assert_that(output_html, is_(expected_html))

    def test_input_a_set_of_words_with_nested_underscore_and_bold(self) -> None:
        input_word = 'this set of words _have bold **and italic** in_ one line'
        output_html = MarkdownLineProc.parse_line(input_word)
        expected_html = 'this set of words <span class="italic-text">have bold <span class="bold-text">and italic</span> in</span> one line'
        assert_that(output_html, is_(expected_html))

class TestDocumentFormatting(object):
    def test_input_document_with_single_hash_for_heading_text(self) -> None:
        input_document = """
        # This is an h1 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h1>This is an h1 heading</h1>\n"""
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_two_hash_for_heading_text(self) -> None:
        input_document = """
        ## This is an h2 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h2>This is an h2 heading</h2>\n"""
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_three_hash_for_heading_text(self) -> None:
        input_document = """
        ### This is an h3 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h3>This is an h3 heading</h3>\n"""
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_four_hash_for_heading_text(self) -> None:
        input_document = """
        #### This is an h4 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h4>This is an h4 heading</h4>\n"""
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_five_hash_for_heading_text(self) -> None:
        input_document = """
        ##### This is an h5 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h5>This is an h5 heading</h5>\n"""
        assert_that(output_html, is_(expected_html))

    def test_input_document_with_six_hash_for_heading_text(self) -> None:
        input_document = """
        ###### This is an h6 heading
        """
        output_html = MarkdownDocumentProc.parse_doc(input_document)
        expected_html = """\n<h6>This is an h6 heading</h6>\n"""
        assert_that(output_html, is_(expected_html))