import re
from mistune import Markdown, BlockLexer
from markdown_renderer import MarkdownRenderer

from operator import itemgetter

HEADER = 'zz_header'
ITEMS = 'zz_items'

class MarkdownBlockProcessor(BlockLexer):
    _sort_headers = False

    def __init__(self, rules=None, **kwargs):
        if kwargs.get('sort_headers'):
            self._sort_headers = True

        super(MarkdownBlockProcessor, self).__init__(rules, **kwargs)

    def build_header_tree(self, tokens):
        tree = None
        parent = None
        level = None
        chain = []

        if not tokens:
            raise StandardError('Token list is empty!')
        elif tokens[0]['type'] != 'heading':
            raise StandardError('First token is not a heading!')

        for token in tokens:
            if tree is None:
                tree = token
                parent = token
                level = token['level']
                token[HEADER] = []
                chain.append(token)
            else:
                if token['type'] == 'heading':
                    l = token['level']

                    if l == level:
                        chain.pop()
                        # jump back to heading above
                        parent = chain[-1]
                        parent[HEADER].append(token)
                        # we are the new parent
                        parent = token
                        chain.append(token)
                    elif l > level:
                        if not HEADER in parent:
                            parent[HEADER] = []
                        parent[HEADER].append(token)
                        chain.append(parent)
                        parent = token
                        level = l
                    else: # l < level
                        if l == 1:
                            parent = chain[0]
                            chain = [ parent ]
                        else:
                            parent = chain.pop()
                        level = l
                        parent[HEADER].append(token)
                else:
                    if not ITEMS in parent:
                        parent[ITEMS] = []
                    parent[ITEMS].append(token)

        return tree

    def flatten_header_tree(self, tree):
        tokens = []

        tokens.append(tree)

        if ITEMS in tree:
            for item in tree[ITEMS]:
                tokens.append(item)
            del(tree[ITEMS])

        if HEADER in tree:
            for sub_header in tree[HEADER]:
                for item in self.flatten_header_tree(sub_header):
                    tokens.append(item)
            del(tree[HEADER])

        return tokens

    def sort_headers(self):
        tree = self.build_header_tree(self.tokens)

        # sort the second level
        if HEADER in tree and tree[HEADER]:
            tree[HEADER] = sorted(tree[HEADER], key=itemgetter('text'))

        self.tokens = self.flatten_header_tree(tree)

    def parse(self, text, rules=None):
        self.tokens = super(MarkdownBlockProcessor, self).parse(text, rules)

        if self._sort_headers:
            self.sort_headers()

        return self.tokens

# based on mistune.Markdown
class MarkdownProcessor(Markdown):
    """A processor for ITL doc markdown based on mistune
    """

    def __init__(self, renderer=None, inline=None, block=None, **kwargs):
        if not renderer:
            renderer = MarkdownRenderer(**kwargs)
        if not block:
            block = MarkdownBlockProcessor(**kwargs)

        Markdown.__init__(self, renderer, inline, block, **kwargs)
