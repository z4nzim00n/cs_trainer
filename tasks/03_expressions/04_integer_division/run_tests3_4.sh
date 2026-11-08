#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "7 2" $'7 / 2 = 3\n7 % 2 = 1\n'
run_case "-7 2" $'-7 / 2 = -3\n-7 % 2 = -1\n'
run_case "10 5" $'10 / 5 = 2\n10 % 5 = 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
