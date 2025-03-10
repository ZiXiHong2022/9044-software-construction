#! /usr/bin/env dash

# ==============================================================================
# test08.sh
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


# check if .pushy/commits is empty and .pushy/index exist
mkdir -p .pushy/index
rm -rf .pushy/commits

cat > "$expected_output" <<EOF
pushy-status: error: haven't staged for commits
EOF

pushy-status > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#current directory and index and lastest commits directory which not stage yet

mkdir -p .pushy/index .pushy/commits/commit1

cat > "$expected_output" <<EOF
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


#Untracked files in the current directory
mkdir -p .pushy/index
echo "Hello World" > untracked_file.txt


cat > "$expected_output" <<EOF
untracked_file.txt - untracked
EOF

pushy-status  > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0