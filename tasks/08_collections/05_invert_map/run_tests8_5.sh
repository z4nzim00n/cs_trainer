#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\na 1\nb 2\nc 3' $'1: a\n2: b\n3: c\n'
run_case $'2\nx 10\ny 5' $'5: y\n10: x\n'
run_case $'1\nonly 42' $'42: only\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
