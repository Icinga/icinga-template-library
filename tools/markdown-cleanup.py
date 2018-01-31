#!/usr/bin/env python

import sys, os.path
# try to load the submodule
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/mistune')

import mistune
from markdown_renderer import MarkdownRenderer

if len(sys.argv) < 2:
    raise StandardError('Please specify at least one file to fix!')

files = sys.argv
files.pop(0)

for file in files:
    print "Working on file: %s" % file
    source_text = None

    with open(file, 'r') as f:
        source_text = f.read()
        f.close()

    md = mistune.Markdown(MarkdownRenderer())
    markdown = md(source_text)
    markdown = markdown.rstrip('\n') + '\n'

    with open(file, 'w') as f:
        f.write(markdown)
        f.close()
