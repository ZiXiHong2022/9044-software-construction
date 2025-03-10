#! /usr/bin/env dash

# ==============================================================================
# test00.sh
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


#The files in the index are different from the files in both the working directory and the repository, and the --force option is not used
mkdir -p .pushy/index .pushy/commits/commit1

echo "Index content" > .pushy/index/checkfile

echo "Working directory content" > checkfile

echo "Repository content" > .pushy/commits/commit1/checkfile

cat > "$expected_output" <<EOF
pushy-rm: error: 'checkfile' not found in index and working directory
EOF

pushy-rm checkfile > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

# The files in the index are different from the files in the working directory, but are the same as the latest version in the repository and are not using the --force option

mkdir -p .pushy/index .pushy/commits/commit1

echo "Same content" > .pushy/index/checkfiles2

cp .pushy/index/checkfiles2 .pushy/commits/commit1/

echo "Modified content" > checkfiles2



cat > "$expected_output" <<EOF
pushy-rm: error: 'checkfiles2' has staged changes in the index
EOF

pushy-rm checkfiles2 > "$actual_output" 2>&1

if ! diff "$expected_output" "$actual_output"; then
    echo "Failed test"
    exit 1
fi

echo "Passed test"
exit 0