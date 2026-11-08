#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f text.txt' EXIT
printf 'hello world\nfoo\n' > text.txt
run_case "text.txt" $'Words: 3\n'
printf '  one   two  ' > text.txt
run_case "text.txt" $'Words: 2\n'
: > text.txt
run_case "text.txt" $'Words: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
