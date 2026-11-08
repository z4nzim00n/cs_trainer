#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Bob 5" $'Student: Bob, Grade: 5\n'
run_case "Alice 4" $'Student: Alice, Grade: 4\n'
run_case "Eve 3" $'Student: Eve, Grade: 3\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
