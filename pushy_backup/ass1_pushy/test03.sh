#! /usr/bin/env dash

# ==============================================================================
# test03.sh
# Test the pushy-log command.
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

./pushy-init
rm .pushy
cat > "$expected_output" <<EOF
create a initial .pushy files first
EOF

pushy-log > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

./pushy-init

echo "information" > a

./pushy-add a

./pushy-commit -m "first commit"

rm .pushy/commits

cat > "$expected_output" <<EOF
pushy-log : commit directory not found
EOF

pushy-log > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0