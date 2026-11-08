#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f numbers.txt' EXIT
printf '1 2 3\n4 5\n' > numbers.txt
run_case "numbers.txt" $'Sum: 15\n'
printf -- '-1 10' > numbers.txt
run_case "numbers.txt" $'Sum: 9\n'
printf '42' > numbers.txt
run_case "numbers.txt" $'Sum: 42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
