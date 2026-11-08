#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f text.txt' EXIT
printf 'hello world\nfoo\n' > text.txt
run_case "text.txt" $'Lines: 2\nWords: 3\nChars: 13\n'
printf 'one\n' > text.txt
run_case "text.txt" $'Lines: 1\nWords: 1\nChars: 3\n'
: > text.txt
run_case "text.txt" $'Lines: 0\nWords: 0\nChars: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
