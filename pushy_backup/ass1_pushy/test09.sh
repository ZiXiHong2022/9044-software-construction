#! /usr/bin/env dash

# ==============================================================================
# test09.sh
# Test the pushy-status command.
#
# Written by: Zixi Hong <z5521365@ad.unsw.edu.au>
# Date: 2024-03-21
# For COMP2041/9044 Assignment 1
# ==============================================================================

# add the current directory to the PATH so scripts
# can still be executed from it after we cd

PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1

# Create some files to hold output.

expected_output="$(mktemp)"
actual_output="$(mktemp)"

# Remove the temporary directory when the test is done.

trap 'rm "$expected_output" "$actual_output" -rf "$test_dir"' INT HUP QUIT TERM EXIT


#The file is only in the index, not with the current directory
mkdir -p .pushy/index

echo "Index version" > .pushy/index/changed_file.txt
echo "Workdir version" > changed_file.txt

cat > "$expected_output" <<EOF
changed_file.txt - file changed, changes not staged for commit
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#The file is in the index and in the latest commit, but the content is different

mkdir -p .pushy/index .pushy/commits/commit1


echo "Index version" > .pushy/index/staged_file.txt
echo "Commit version" > .pushy/commits/commit1/staged_file.txt


cat > "$expected_output" <<EOF
staged_file.txt - file changed, changes staged for commit
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# File is in the index but not in the latest commit

mkdir -p .pushy/index
echo "New file" > .pushy/index/test_file.txt

cat > "$expected_output" <<EOF
new_file.txt - added to index
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


#File in latest commit but deleted from current directory

mkdir -p .pushy/commits/commit1


echo "Deleted file" > .pushy/commits/commit1/deleted_file.txt
rm -f deleted_file.txt


cat > "$expected_output" <<EOF
deleted_file.txt - file deleted
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#The files are in the working directory, the index, and the latest submission, with the same contents

mkdir -p .pushy/index .pushy/commits/commit1

echo "Same content" > same_file.txt
cp same_file.txt .pushy/index/
cp same_file.txt .pushy/commits/commit1/


cat > "$expected_output" <<EOF
identical_file.txt - same as repo
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


echo "Passed test"
exit 0