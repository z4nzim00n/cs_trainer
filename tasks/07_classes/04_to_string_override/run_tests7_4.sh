#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "1 2" $'Point(1, 2)\n'
run_case "-3 7" $'Point(-3, 7)\n'
run_case "0 0" $'Point(0, 0)\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
