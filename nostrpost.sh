#!/bin/bash

# This script publishes a message to Nostr.

# Get the message from the Python script.
# replace the path with your own
b=$(python3 /home/nostrbot/nostrbot.py)

# Check if the message has content.
if [[ ! -z "$b" ]]; then
  # Echo the message to the console.
  echo $b

  # Publish the message to Nostr.
  # replace the path with your own
  /home/nostrbot/go/bin/noscl publish "$b"
else
  echo "end of the file"
fi
