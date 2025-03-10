#!/bin/dash

for i in "$@"; do
    if [ -e "$i" ]; then
        display "$i" || echo "Cannot display $i - skipping"
        
        echo "Address to e-mail this image to?"
        read add_name

        if [ -n "$add_name" ]; then
            echo "Message to accompany image?"
            read acc_text 

            echo "$acc_text" | mutt -s "$i!" -e 'set copy=no' -a "$i" -- "$add_name"
            echo "$i sent to $add_name"
        else
            echo "No email sent "
        fi
    else
        echo "File $i does not exist - skipping"
    fi
done
