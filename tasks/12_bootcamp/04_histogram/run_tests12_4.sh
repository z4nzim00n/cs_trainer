#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n2 5 2 2 5' $'2: ***\n5: **\n'
run_case $'3\n0 9 0' $'0: **\n9: *\n'
run_case $'1\n7' $'7: *\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
