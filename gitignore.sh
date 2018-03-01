#!/bin/sh
# Script for managing the XMedicus .gitignore file.
# Add file(s) using:

# gitignore foo bar

# Invoking without files removes duplicates and resorts.

file=".gitignore"
if ! [[ -f "$file" ]]
then
    echo "$file not found."
    return 1
fi

# We want these to appear first in .gitignore, for aesthetic reasons.
# These elements are prepended, so the last element is line 1 of .gitignore.
# Remember to escape everything properly
array=("\\\n"
"\# Everything below should be auto-sorted. Edit gitignore.sh to add lines above."
"\\\n"
)

for item in "${array[@]}"; do
    LC_ALL=C sed -i "/^$item$/d" .gitignore 
done

for item in "$@"; do
    LC_ALL=C echo "$item" >> .gitignore;
done

sed -i "/^\$/d" .gitignore

# Remove duplicates (and sort):
LC_ALL=C sort -u -f .gitignore -o .gitignore

# Add our stuff to the beginning
for item in "${array[@]}"; do
    LC_ALL=C sed -i "1i $item" .gitignore
done

