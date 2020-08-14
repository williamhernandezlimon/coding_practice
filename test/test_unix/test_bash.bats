#!/usr/bin/env bats

PROJECT_ROOT_DIR="$PWD/../.."
SRC_FILE="src/unix/bash.sh"


setup() {
  . shellmock

  # create test_table.txt
  {
    echo "---------------------------------------------
|   id  |   user    |   title   |   country |
---------------------------------------------
|   0   |   bob     |   engr    |   usa     |
---------------------------------------------
|   1   |   joe     |   teacher |   mx      |
---------------------------------------------
|   2   |   sam     |   doc     |   china   |
---------------------------------------------
|   3   |   linda   |   nurse   |   eu      |
---------------------------------------------"
  } >> test_table.txt


  # create words.txt
  {
  	echo "a  
 b  c   
   c    b  c"
  } >> words.txt
}

teardown() {
    if [ -z "$TEST_FUNCTION" ]; then
        # echo cleaning tmp mock
        shellmock_clean
    fi

    # remove test files
    rm test_table.txt
    rm words.txt
}

@test "$SRC_FILE - python execution full test with package.json" {
  shellmock_expect shopt --match "-s nullglob globstar"
  shellmock_expect node --type regex --match "--version"
  shellmock_expect npm --type regex --match "--version"
  shellmock_expect yarn --type regex --match "--version"

  shellmock_expect node --type partial --match "-p require('./package.json').version"
  shellmock_expect curl --type regex --match "--request POST.*--url.*--header.*--data.*icon_emoji.*package*"

  # mock all yarn services
  shellmock_expect yarn --type regex --match ".*"

  shellmock_expect tar --type regex --match "-czf.*"
  shellmock_expect aws --type regex --match "s3 cp.*"

  [ ! -d "dockerbuild" ] && mkdir dockerbuild
  shellmock_expect zip --type regex --match "buildspec.zip buildspec.yml"
  shellmock_expect aws --type regex --match "s3 cp.*"
  shellmock_expect rm --type regex --match "-rf buildspec.zip"

  shellmock_expect python3 --type regex --match "/godata/build-gocd-pipeline/pipeline_scripts/message.py.*wavefront.*--metric_type.*metric_value.*epoch_start_time.*source.*"

  run ${PROJECT_SRC_ROOT_DIR}/$SRC_FILE
  [ "$status" = "0" ]
}




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