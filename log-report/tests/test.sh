#!/bin/bash
set -e

mkdir -p /logs/verifier

pytest \
    /tests/test_outputs.py \
    -rA \
    --ctrf=/logs/verifier/ctrf.json

echo 1 > /logs/verifier/reward.txt