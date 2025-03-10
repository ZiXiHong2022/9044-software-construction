#! /usr/bin/env dash

# ==============================================================================
# test04.sh
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


rm -rf .pushy  # make sure .pushy is not exist

cat > "$expected_output" <<EOF
pushy-show: error: pushy repository directory .pushy not found
EOF

pushy-show 1:a > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


#arguments number error


cat > "$expected_output" <<EOF
usage:pushy-show [commit]:filename
EOF

pushy-show 1:a:12 > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# check if there is a tracked file
mkdir -p .pushy/index
cat > "$expected_output" <<EOF
pushy-show: error: 'A' not found in index
EOF

pushy-show : A > "actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi





echo "Passed test"
exit 0





