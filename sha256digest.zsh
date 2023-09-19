#!/bin/zsh

# check if the file is provided
if [[ $# -eq 0 ]]; then
  echo "Usage: $0 <path/to/file.txt>"
  exit 1
fi

# Check if the file exists
if [[ ! -f $1 ]]; then
  echo "File not found: $1"
  exit 1
fi

# Compute the SHA-256 hash
computed_hash=$(shasum -a 256 $1 | awk '{ print $1 }')
echo "Computed hash: $computed_hash"

# check if an exptected hash is provided
if [[ $# -eq 2 ]]; then
  exptected_hash=$2

  if [[ "$computed_hash" == "$exptected_hash" ]]; then
    echo "Hash match: Verified"
  else
    echo "Hash mismatch: Not Verified"
  fi
fi
