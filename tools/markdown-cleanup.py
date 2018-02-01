#!/usr/bin/env python

import sys, os.path
import argparse
# try to load the submodule
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/mistune')

from markdown_processor import MarkdownProcessor

parser = argparse.ArgumentParser(description='Markdown cleanup and re-formatting')
parser.add_argument('files', metavar='file', nargs='+',
                    help='List of files to work with')
parser.add_argument('--sort-headers', action='store_true',
                    help='Sort all 2nd level headers in the file')
args = parser.parse_args()

if len(args.files) == 0:
    raise StandardError('Please specify at least one file to work on!')

options = {}
if args.sort_headers:
    options['sort_headers'] = True
md = MarkdownProcessor(**options)

for file in args.files:
    print "Working on file: %s" % file
    source_text = None

    with open(file, 'r') as f:
        source_text = f.read()
        f.close()

    markdown = md(source_text)
    markdown = markdown.rstrip('\n') + '\n'

    with open(file, 'w') as f:
        f.write(markdown)
        f.close()
