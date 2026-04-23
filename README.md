# Retrosynthesis

Repository for retrosynthesis workflows.

This repository uses AiZynthFinder to build retrosynthetic routes.
The code in the `aizynthfinder` directory was downloaded from `https://github.com/MolecularAI/aizynthfinder` at commit `adf53342049cbb6508410c35d52748ac6461d10e`.

## Environment Setup

1. Install `uv` if it is not already installed. It is a faster alternative to `pip` and `poetry`.
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
More detailed instructions are available in the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/).

2. Install dependencies.
```bash
cd aizynthfinder
uv sync
```

## Running Commands

Activate the environment:
```bash
source .venv/bin/activate
```
Then run commands as usual. Alternatively, skip activation and run every command through `uv run`.

## Retrosynthesis Files

Download the configuration and base retrosynthesis model with:
```bash
mkdir public
uv run download_public_data ./public
```

## Running Retrosynthesis

Run `run_aizynthfinder.sh` after setting the correct input and output paths in the script.
AiZynthFinder writes logs to the directory it is launched from, so create a separate run directory for each experiment.
```bash
mkdir logs_exp_example
cd logs_exp_example
uv run bash ../run_aizynthfinder.sh
```

## Results Table

Retrosynthesis results are written to a detailed JSON file.
To quickly generate a table with binary retrosynthesis outcomes, where each molecule is marked as solved or unsolved, run `final_stats_table.py` from `retrosynthesis/aizynthfinder`:
```bash
RESULT_JSON=../results/example.json
OUTPUT_CSV=../results/example.csv
uv run final_stats_table.py -r $RESULT_JSON -o $OUTPUT_CSV
```
