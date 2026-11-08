#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n4 9 1 7 3' $'Min: 1\nMax: 9\n'
run_case $'3\n-5 -2 -8' $'Min: -8\nMax: -2\n'
run_case $'1\n42' $'Min: 42\nMax: 42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
