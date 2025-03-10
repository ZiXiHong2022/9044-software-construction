#!/bin/dash

snap_num=0


while [ -d ".snapshot.$snap_num" ]; do
    snap_num=$((snap_num + 1))
done

snapshot_dir=".snapshot.$snap_num"
echo "Creating snapshot $snap_num"
mkdir "$snapshot_dir"

for c_files in *; do
   
    if [ "$c_files" != "snapshot-save.sh" ] && [ "$c_files" != "snapshot-load.sh" ]; then
        cp "$c_files" "$snapshot_dir/"
    fi
done





