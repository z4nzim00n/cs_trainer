#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "circle 2" $'Area: 12.57\n'
run_case "rect 3 4" $'Area: 12.00\n'
run_case "circle 1" $'Area: 3.14\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
