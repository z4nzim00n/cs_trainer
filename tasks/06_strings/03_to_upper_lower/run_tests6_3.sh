#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Hello World" $'UPPER: HELLO WORLD\nlower: hello world\n'
run_case "C#" $'UPPER: C#\nlower: c#\n'
run_case "abc" $'UPPER: ABC\nlower: abc\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
