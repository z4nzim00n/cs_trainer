#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "7" $'True\n'
run_case "9" $'False\n'
run_case "1" $'False\n'
run_case "2" $'True\n'
run_case "13" $'True\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
