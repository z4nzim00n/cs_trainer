#!/usr/bin/env bash
# scripts/lib.sh — общие функции для run_tests.sh в заданиях C#-тренажёра.
#
# Источник решения задаётся переменной SOURCE_FILE (по умолчанию Program.cs):
#   SOURCE_FILE=Solution.cs bash run_tests1_1.sh
#
# Ожидаемый вывод в run_case — точные байты. Для переносов строк используй
# ANSI-C кавычки: run_case "2 2" $'4\n'  (WriteLine)  или  run_case "2 2" "4"  (Write).
# Вывод программы нормализуется: \r\n -> \n.

_LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$_LIB_DIR/.." && pwd)"

SOURCE_FILE="${SOURCE_FILE:-Program.cs}"
BUILD_DIR=".build"
APP="$BUILD_DIR/app.exe"

# Ищем компилятор C#: переменная CSC, затем csc в PATH, затем Roslyn
# из Visual Studio / Build Tools.
CSC_BIN="${CSC:-}"
if [ -z "$CSC_BIN" ] && command -v csc >/dev/null 2>&1; then
  CSC_BIN="$(command -v csc)"
fi
if [ -z "$CSC_BIN" ]; then
  for _base in "/c/Program Files/Microsoft Visual Studio" \
               "/c/Program Files (x86)/Microsoft Visual Studio"; do
    for _f in "$_base"/*/*/MSBuild/Current/Bin/Roslyn/csc.exe; do
      if [ -f "$_f" ]; then
        CSC_BIN="$_f"
        break 2
      fi
    done
  done
  unset _base _f
fi

compile() {
  mkdir -p "$BUILD_DIR"

  if [ -z "$CSC_BIN" ]; then
    echo "Компилятор C# (csc) не найден." >&2
    echo "Установите .NET Framework / Visual Studio Build Tools либо задайте CSC." >&2
    return 1
  fi

  "$CSC_BIN" -nologo -langversion:latest -warn:4 -optimize+ \
    -out:"$APP" "$SOURCE_FILE" "$@"
}

_compare_and_report() {
  local label="$1" expected="$2"
  printf '%s' "$expected" > /tmp/expected.out
  if cmp -s /tmp/actual.out /tmp/expected.out; then
    echo "OK:   $label -> '$expected'"
  else
    echo "FAIL: $label -> получили '$(cat -A /tmp/actual.out)', ждали '$(cat -A /tmp/expected.out)'"
    FAILED=1
  fi
}

# run_case "вход" "ожидаемый_вывод" — вход через printf (добавляет \n)
run_case() {
  local input="$1" expected="$2"
  printf '%s\n' "$input" | "$APP" | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input'" "$expected"
}

# run_case_noeol "вход" "ожидаемый_вывод" — вход БЕЗ завершающего \n
run_case_noeol() {
  local input="$1" expected="$2"
  printf '%s' "$input" | "$APP" | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input' (без \\n)" "$expected"
}

# run_case_devnull "ожидаемый_вывод" — вход полностью пуст (EOF до первого символа)
run_case_devnull() {
  local expected="$1"
  "$APP" < /dev/null | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "(/dev/null)" "$expected"
}

# run_case_args "аргументы" "вход" "ожидаемый_вывод"
run_case_args() {
  local args="$1" input="$2" expected="$3"
  printf '%s\n' "$input" | "$APP" $args | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "args='$args' input='$input'" "$expected"
}

# check_file "путь" "ожидаемое_содержимое" — проверяет файл, созданный программой.
check_file() {
  local file="$1" expected="$2"
  printf '%s' "$expected" > /tmp/expected_file.out
  if [ ! -f "$file" ]; then
    echo "FAIL: файл '$file' не создан"
    FAILED=1
    return
  fi
  tr -d '\r' < "$file" > /tmp/actual_file.out || true
  if cmp -s /tmp/actual_file.out /tmp/expected_file.out; then
    echo "OK:   файл '$file' -> '$expected'"
  else
    echo "FAIL: файл '$file' -> получили '$(cat -A /tmp/actual_file.out)', ждали '$(cat -A /tmp/expected_file.out)'"
    FAILED=1
  fi
}
