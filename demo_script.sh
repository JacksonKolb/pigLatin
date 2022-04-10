#!/bin/bash

curl -X 'POST' \
  'http://127.0.0.1/piglatin-converter/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sentence": "Hello, my name is Alice."
}'






