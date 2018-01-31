#!/usr/bin/python

import re, os, sys

_invalid_chars = {
    'Non-Breaking Space (Mac)': r'[\xc2\xa0]',
    'Tabulator \\t':            r'\t',
}

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.chdir(root)
errors = 0

for subdir, dirs, files in os.walk('doc/'):
    for file in files:
        if not re.search('\.md$', file):
            continue

        content = None
        fn = os.path.join(subdir, file)
        with open(fn) as f:
            content = f.read()
            f.close()

        for i, line in enumerate(re.split('\n', content)):
            for explanation, pattern in _invalid_chars.iteritems():
                m = re.search(r'^.*' + pattern, line)
                if not m:
                    continue

                sys.stderr.write('%s:%d:%d Invalid character: %s\n' % (fn, i+1, len(m.group(0))-1, explanation))
                print '>> %s' % line
                errors += 1

if errors > 0:
    sys.stderr.write('Found %d errors\n' % errors)
    sys.exit(1)
