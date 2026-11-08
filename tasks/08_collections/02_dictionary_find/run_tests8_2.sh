#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\napple 5\nbanana 7\nkiwi 3\nbanana' $'Found: 7\n'
run_case $'2\na 1\nb 2\nz' $'Not found\n'
run_case $'0\nkey' $'Not found\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
