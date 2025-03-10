#!/bin/dash

# Function to set ID3 tags based on the file path
set_id3_tags() {
    local file_path="$1"
    local artist album title track year

    
    album=$(basename "$(dirname "$file_path")")
    year=$(echo "$album" | grep -oE '[0-9]{4}')

    filename=$(basename "$file_path")
    track=$(echo "$filename" | sed -E 's/^([0-9]+).*/\1/')
    title=$(echo "$filename" | sed -E 's/[0-9]+ - (.*?) - .*/\1/')
    artist=$(echo "$filename" | sed -E 's/.* - (.*)\.mp3/\1/')

    
    id3 -t "$title" -T "$track" -a "$artist" -A "$album" -y "$year" "$file_path"
}


for dir in "$@"; do
    find "$dir" -type f -iname "*.mp3" | while read -r file; do
        set_id3_tags "$file"
    done
done
