#! /usr/bin/env dash

# ==============================================================================
# test01.sh
# Test the pushy-add command.
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

pushy-init
echo "line 1" > a

# test if file exist

cat > "$expected_output" <<EOF
pushy-add: error: can not open '$filename'
EOF

pushy-add a > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# test if filename not start with "-" "." "_"


echo "Hello Julian" > "-csqw.txt"

cat > "$expected_output" <<EOF
pushy-add: error: filename should start with an alphanumeric character ([a-zA-Z0-9]) and will only contain alpha-numeric characters, plus ., - and _ characters.
EOF

pushy-add "-csqw.txt" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# test if the filename is [a-zA-Z0-9]

echo " line 1" > "%^^"

cat > "$expected_output" <<EOF
pushy-add: error: filename should start with an alphanumeric character ([a-zA-Z0-9]) and will only contain alpha-numeric characters, plus ., - and _ characters.
EOF

pushy-add "%^^" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


echo "Passed test"
exit 0