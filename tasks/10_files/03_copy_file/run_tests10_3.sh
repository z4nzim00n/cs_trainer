#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f input.txt copy.txt' EXIT
printf 'abc\n' > input.txt
run_case $'input.txt\ncopy.txt' $'Copied: copy.txt\n'
check_file "copy.txt" $'abc\n'
printf 'old\n' > copy.txt
run_case $'input.txt\ncopy.txt' $'Copied: copy.txt\n'
check_file "copy.txt" $'abc\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
