#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "abc12" $'Letters: 3\nDigits: 2\n'
run_case "Hi, 2025!" $'Letters: 2\nDigits: 4\n'
run_case "!!!" $'Letters: 0\nDigits: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
