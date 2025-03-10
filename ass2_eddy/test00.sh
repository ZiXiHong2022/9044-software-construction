#! /usr/bin/env dash

# ==============================================================================
# test00.sh
# Test the '-n' defalut command.
# Written by: ZiXi Hong <z5521365@ad.unsw.edu.au>
# Date: 2024-04-18
# For COMP2041/9044 Assignment 2
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

# test1
echo -e "line 1\nline 2\nline 3" > test_input.txt


echo -e "line 1\nline 2" > "$expected_output"


cat test_input.txt | python3 eddy.py '2d' > "$actual_output"


if diff "$expected_output" "$actual_output"; then
    echo "Passed test"
    exit 0
else
    echo "Failed test"
    exit 1
fi



# test2

echo -e "line 1\nline 2\nline 3" > test_input.txt


echo -e "" > "$expected_output"


cat test_input.txt | python3 eddy.py -n '2d' > "$actual_output"


if diff "$expected_output" "$actual_output"; then
    echo "Passed test"
    exit 0
else
    echo "Failed test"
    exit 1
fi

