#! /usr/bin/env dash

# ==============================================================================
# test02.sh
# Test the pushy-commit command.
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
echo "line 2" > c
./pushy-add c

#check if commit message is ASCII

cat > "$expected_output" <<EOF
Commit message cannot start with '-'
EOF

pushy-commit -m "不是ascii" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


#check commit message not start with "-"


cat > "$expected_output" <<EOF
Commit message cannot start with '-'
EOF

pushy-commit -m "-first mesaage" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi


#check if [-a] is working

cat > "$expected_output" <<EOF
Committed as commit 0
EOF

pushy-commit -m "-second mesaage" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi



#check if .pushy/index doesn't change
touch d
./pushy-add d

cat > "$expected_output" <<EOF
Nothing to commit.
EOF

pushy-commit -m "third message" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi



# test if -m function can work

cat > "$expected_output" <<EOF
Committed as commit 1
EOF

pushy-commit -m "fifth message" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

#only type commit message without -m
cat > "$expected_output" <<EOF
Usage: pushy-commit [-a] -m <commit_message>
EOF

pushy-commit "first message" > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0