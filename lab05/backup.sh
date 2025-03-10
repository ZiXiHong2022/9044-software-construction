#!/bin/dash


if [ $# -ne 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

filename="$1"


backup_base=".${filename}"
backup_suffix=0


while [ -e "${backup_base}.${backup_suffix}" ]; do
    backup_suffix=$((backup_suffix + 1))
done


backup_file="${backup_base}.${backup_suffix}"


cp "$filename" "$backup_file"

echo "Backup of '$filename' saved as '$backup_file'"
