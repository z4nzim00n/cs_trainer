#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\nabc xyz' $'def abc\n'
run_case $'1\nHello, World!' $'Ifmmp, Xpsme!\n'
run_case $'0\nNo change' $'No change\n'
run_case $'25\nab' $'za\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
