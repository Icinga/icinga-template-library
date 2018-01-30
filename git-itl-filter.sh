#!/bin/bash

set -ex

# Filtering commits, only including ITL and its docs
git filter-branch --force --prune-empty --index-filter '
    set -e
    # Delete files which are NOT needed
    git ls-files -z | grep -zvP "^(itl/|doc/.*template-library)" | xargs -0 -r git rm --cached -q
    # Move files to root directory
    git ls-files -s |
        GIT_INDEX_FILE=$GIT_INDEX_FILE.new \
        git update-index --index-info &&
        ( test ! -f "$GIT_INDEX_FILE.new" \
            || mv -f "$GIT_INDEX_FILE.new" "$GIT_INDEX_FILE" )
' HEAD

TF=`mktemp`

# Helper script to clean branch
cat >"$TF" <<EOF
#!/usr/bin/env ruby
old_parents = gets.chomp.gsub('-p ', ' ')

if old_parents.empty? then
  new_parents = []
else
  new_parents = \`git show-branch --independent #{old_parents}\`.split
end

puts new_parents.map{|p| '-p ' + p}.join(' ')
EOF
chmod +x "$TF"

git filter-branch --force --prune-empty --parent-filter "$TF" HEAD

rm -f "$TF"
