#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\nwater 500\ncoffee 30\ncup\ncup\ncup' $'Coffee ready\nCoffee ready\nNot enough resources\nWater: 100\nCoffee: 10\n'
run_case $'3\nwater 200\ncoffee 10\ncup' $'Coffee ready\nWater: 0\nCoffee: 0\n'
run_case $'4\nwater 199\ncoffee 10\ncup\ncup' $'Not enough resources\nNot enough resources\nWater: 199\nCoffee: 10\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
