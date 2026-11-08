#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "20 1" $'Allowed: True\n'
run_case "17 1" $'Allowed: False\n'
run_case "20 0" $'Allowed: False\n'
run_case "18 1" $'Allowed: True\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
