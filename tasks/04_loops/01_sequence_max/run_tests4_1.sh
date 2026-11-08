#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 9 2 7 1' $'Max: 9\n'
run_case $'3\n-5 -2 -8' $'Max: -2\n'
run_case $'1\n42' $'Max: 42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
