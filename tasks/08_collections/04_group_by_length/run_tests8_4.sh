#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "dog elephant cat sun" $'3: cat dog sun\n8: elephant\n'
run_case "aa b ccc" $'1: b\n2: aa\n3: ccc\n'
run_case "one two" $'3: one two\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
