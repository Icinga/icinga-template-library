# Notes for Development

## Markdown Updates

There are some tools to process and update the markdown docs.

### Cleanup

Does re-render markdown files and takes care of:

* Cleaning up whitespace
* Re-formatting tables
* (optional) sorting all 2nd level headers

Usage:

```
./tools/markdown-cleanup.py doc/*.md
./tools/markdown-cleanup.py --sort-headers doc/{1{1,2,3,4},2,3}*.md
```
