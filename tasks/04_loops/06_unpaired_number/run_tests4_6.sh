#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n2 3 2 1 3' $'Unique: 1\n'
run_case $'3\n7 7 9' $'Unique: 9\n'
run_case $'1\n42' $'Unique: 42\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
