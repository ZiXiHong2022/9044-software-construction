#! /usr/bin/env dash

# ==============================================================================
# test06.sh
# Test the pushy-rm command.
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

# check if file not in .pushy/index directory
mkdir -p .pushy/index
touch checkfile1
cat > "$expected_output" <<EOF
pushy-rm: error: 'checkfile1' is not in the pushy repository
EOF

pushy-rm checkfile1 > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# check if the file not in current directory and index directory
mkdir -p .pushy/index

cat > "$expected_output" <<EOF
pushy-rm: error: 'checkfile2' not found in index and working directory
EOF

pushy-rm checkfile2 > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


echo "Passed test"
exit 0