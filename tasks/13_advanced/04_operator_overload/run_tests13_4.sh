#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "1 2 3 4" $'(4, 6)\n'
run_case "-1 5 1 -5" $'(0, 0)\n'
run_case "0 0 0 0" $'(0, 0)\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
