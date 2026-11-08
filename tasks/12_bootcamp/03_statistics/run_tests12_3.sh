#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n1 2 3 4 5' $'Min: 1\nMax: 5\nSum: 15\nAverage: 3.00\n'
run_case $'3\n2 4 9' $'Min: 2\nMax: 9\nSum: 15\nAverage: 5.00\n'
run_case $'1\n-5' $'Min: -5\nMax: -5\nSum: -5\nAverage: -5.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
