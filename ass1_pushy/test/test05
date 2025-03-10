#! /usr/bin/env dash

# ==============================================================================
# test05.sh
# Test the pushy-show command.
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

#Check if trackrd commit number is exist
mkdir -p .pushy/commits

cat > "$expected_output" <<EOF
pushy-show: error: unknown commit '3'
EOF

pushy-show 3:A > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


# check if there is file in .pushy/commits/$commit_next_number
mkdir -p .pushy/commits/1

cat > "$expected_output" <<EOF
pushy-show: error: 'Acsss' not found in commit 1
EOF

pushy-show 1:Acsss > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0