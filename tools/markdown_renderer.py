import re

# based on mistune.Renderer
class MarkdownRenderer(object):
    """A markdown renderer for mistune
    """

    def __init__(self, **kwargs):
        self.options = kwargs

    def placeholder(self):
        """Returns the default, empty output value for the renderer.
        """
        return ''

    def block_code(self, code, lang=None):
        """Rendering block level code. ``pre > code``.
        :param code: text content of the code block.
        :param lang: language of the given code.
        """
        code = code.rstrip('\n')
        if not lang:
            return '```\n%s\n```\n\n' % code
        return '```%s\n%s\n```\n\n' % (lang, code)

    def block_quote(self, text):
        """Rendering blockquote with the given text.
        :param text: text content of the blockquote.
        """
        text = re.sub('^', '> ', text.rstrip('\n'), 0, re.MULTILINE)
        text = re.sub('\s+$', '', text, 0, re.MULTILINE)
        return text + '\n\n'

    def block_html(self, html):
        """Rendering block level pure html content.
        :param html: text content of the html snippet.
        """
        return '\n' + html + '\n'

    def header(self, text, level, raw=None):
        """Rendering header/heading tags like ``<h1>`` ``<h2>``.
        :param text: rendered text content for the header.
        :param level: a number for the header level, for example: 1.
        :param raw: raw text content of the header.
        """
        return '%s %s\n\n' % ('#' * level, text)

    def hrule(self):
        """Rendering method for horizontal ruler."""
        return '\n---\n'

    def list(self, body, ordered=True):
        """Rendering list tags like ``<ul>`` and ``<ol>``.
        :param body: body contents of the list.
        :param ordered: whether this list is ordered or not.
        """
        if ordered:
            items = re.split('\n', body)
            for i, v in enumerate(items):
                prefix = '%d. ' % (i+1)
                items[i] = re.sub('^\* ', prefix, v)

            body = '\n'.join(items)
        return body + '\n'

    def list_item(self, text):
        """Rendering list item snippet. Like ``<li>``."""
        return '* %s\n' % text

    def paragraph(self, text):
        """Rendering paragraph tags. Like ``<p>``."""
        return text.strip() + '\n\n'

    def _align_table(self, text):
        header_cols = []
        cols = []
        lines = re.split('\n', text)

        # calculate columns sizes
        for i in range(len(lines)):
            cells = re.split(r'(?<!\\)\|', lines[i])
            for j in range(len(cells)):
                l = len(cells[j])
                if len(cols) < j+1:
                    cols.append(l)
                elif l > cols[j]:
                    cols[j] = l

            # save the header sizes
            if i == 0:
                header_cols = cols[:]

        # resize all cells
        for i in range(len(lines)):
            cells = re.split(r'(?<!\\)\|', lines[i])
            col_no = len(cells)
            for j in range(col_no):
                content = cells[j]
                if re.search('^\s*\-+\s*$', content):
                    if self.options.get('table_borders'):
                        cells[j] = ' %s ' % ('-' * (cols[j]-2))
                    elif j == col_no - 1:
                        cells[j] = '-' * header_cols[j]
                    else:
                        cells[j] = '-' * cols[j]
                else:
                    pad = cols[j] - len(content)
                    if pad < 0:
                        pad = 0
                    cells[j] = ' %s%s ' % (cells[j].strip(), ' ' * pad)

            lines[i] = '|'.join(cells).strip()

        return '\n'.join(lines)

    def table(self, header, body):
        """Rendering table element. Wrap header and body in it.
        :param header: header part of the table.
        :param body: body part of the table.
        """
        # count columns with the
        cols = re.split(r'(?<!\\)\|', header.strip().strip('|').strip())
        count = len(cols)

        if self.options.get('table_borders'):
            header_sep = '|' + (' --- |' * count)
        else:
            header_sep = ('---|' * count).rstrip('|')
        text = '%s%s\n%s\n' % (header, header_sep, body)
        return self._align_table(text)

    def table_row(self, content):
        """Rendering a table row. Like ``<tr>``.
        :param content: content of current table row.
        """
        if self.options.get('table_borders'):
            return content + '|\n'
        return re.sub(r'\s*\|\s*$', '', content) + '\n'

    def table_cell(self, content, **flags):
        """Rendering a table cell. Like ``<th>`` ``<td>``.
        :param content: content of current table cell.
        :param header: whether this is header or not.
        :param align: align of current table cell.
        """
        # TODO: align
        #align = flags['align']
        if self.options.get('table_borders'):
            return '| %s ' % (content)
        return '%s | ' % (content)

    def double_emphasis(self, text):
        """Rendering **strong** text.
        :param text: text content for emphasis.
        """
        return '**%s**' % text

    def emphasis(self, text):
        """Rendering *emphasis* text.
        :param text: text content for emphasis.
        """
        return '*%s*' % text

    def codespan(self, text):
        """Rendering inline `code` text.
        :param text: text content for inline code.
        """
        return '`%s`' % text

    def linebreak(self):
        """Rendering line break like ``<br>``."""
        return '\n'

    def strikethrough(self, text):
        """Rendering ~~strikethrough~~ text.
        :param text: text content for strikethrough.
        """
        return '~~%s~~' % text

    def text(self, text):
        """Rendering unformatted text.
        :param text: text content.
        """
        return text

    def escape(self, text):
        """Rendering escape sequence.
        :param text: text content.
        """
        return '\\' + text

    def autolink(self, link, is_email=False):
        """Rendering a given link or email address.
        :param link: link content or email address.
        :param is_email: whether this is an email or not.
        """
        return link

    def link(self, link, title, text):
        """Rendering a given link with content and title.
        :param link: href link for ``<a>`` tag.
        :param title: title content for `title` attribute.
        :param text: text content for description.
        """
        if not title:
            return '[%s](%s)' % (text, link)
        return '[%s](%s "%s")' % (text, link, title)

    def image(self, src, title, text):
        """Rendering a image with title and text.
        :param src: source link of the image.
        :param title: title text of the image.
        :param text: alt text of the image.
        """
        if not title:
            return '![%s](%s)' % (text, src)
        return '![%s](%s "%s")' % (text, src, title)

    def inline_html(self, html):
        """Rendering span level pure html content.
        :param html: text content of the html snippet.
        """
        return html

    def newline(self):
        """Rendering newline element."""
        return '\n'

    def footnote_ref(self, key, index):
        """Rendering the ref anchor of a footnote.
        :param key: identity key for the footnote.
        :param index: the index count of current footnote.
        """
        return ''

    def footnote_item(self, key, text):
        """Rendering a footnote item.
        :param key: identity key for the footnote.
        :param text: text content of the footnote.
        """
        return ''

    def footnotes(self, text):
        """Wrapper for all footnotes.
        :param text: contents of all footnotes.
        """
        return ''
