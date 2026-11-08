#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'4\nbbb a cc ab' $'a ab cc bbb\n'
run_case $'3\nbb aa c' $'c aa bb\n'
run_case $'2\nsame same' $'same same\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
