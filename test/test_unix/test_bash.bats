#!/usr/bin/env bats

PROJECT_ROOT_DIR="$PWD/../.."
SRC_FILE="src/unix/bash.sh"


@test "$SRC_FILE - addition" {
  run ${PROJECT_SRC_ROOT_DIR}/$SRC_FILE 2 2
  [ "$result" -eq 4 ]
}



@test "addition using bc" {
  result="$(echo 2+2 | bc)"
  [ "$result" -eq 4 ]
}

@test "addition using dc" {
  result="$(echo 2 2+p | dc)"
  [ "$result" -eq 4 ]
}