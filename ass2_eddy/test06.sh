#! /usr/bin/env dash

# ==============================================================================
# test06.sh
# Test the regular expression
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


# test 1
echo -e "hello\nworld 123\nanother line"  > test_input.txt


echo -e "hello\nworld 123\nworld 123\nanother line" > "$expected_output"


cat test_input.txt | python3 eddy.py '/[0-9]+/p' > "$actual_output"

if diff "$expected_output" "$actual_output"; then
    echo "Passed test"
    exit 0
else
    echo "Failed test"
    exit 1
fi



# test 2

echo -e "hello 123\nhello world\nexample 456\njust text"  > test_input.txt


echo -e "hEllo 123\nhEllo world\nExamplE 456\njust text" > "$expected_output"


cat test_input.txt | python3 eddy.py '/[0-9]|world/s/e/E/g' > "$actual_output"

if diff "$expected_output" "$actual_output"; then
    echo "Passed test"
    exit 0
else
    echo "Failed test"
    exit 1
fi



# test 3


echo -e "start\nmiddle 123\nfinish"   > test_input.txt


echo -e "start\nmiddle 123\nfinish" > "$expected_output"


cat test_input.txt | python3 eddy.py '/\d+/s/^/Start: /;s/$/ :End/' > "$actual_output"

if diff "$expected_output" "$actual_output"; then
    echo "Passed test"
    exit 0
else
    echo "Failed test"
    exit 1
fi













