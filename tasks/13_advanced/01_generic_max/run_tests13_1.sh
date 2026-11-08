#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3 7\napple banana' $'Max int: 7\nMax string: banana\n'
run_case $'-1 -9\ncat dog' $'Max int: -1\nMax string: dog\n'
run_case $'5 5\na a' $'Max int: 5\nMax string: a\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
