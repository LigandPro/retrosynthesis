#!/bin/bash

# Full path to the input CSV file with SMILES
INPUT_FILE="/<...>/retrosynthesis/data/example.smi"

# Full path to the output JSON file
OUTPUT_FILE="/<...>/retrosynthesis/results/example.json"

# Full path to the config file
CONFIG_FILE="/<...>/retrosynthesis/aizynthfinder/public/config.yml"

# Number of processes to use
PROCESSES=1

# Run the command
aizynthcli --config $CONFIG_FILE \
            --smiles $INPUT_FILE \
            --output $OUTPUT_FILE \
            --log_to_file \
            --nproc $PROCESSES