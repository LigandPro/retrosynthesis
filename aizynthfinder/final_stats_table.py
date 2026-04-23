"""A simple script to report statistics about the retrosynthesis results."""

import json

def report_stats(data: list):
    solved_times = []
    solved = 0
    report = []
    for d in data:
        solved_times.append(float(d["search_time"]))
        if d["is_solved"]:
            solved += 1
        report.append((d["index"], d["target"], 1 if d["is_solved"] else 0))

    print(f"Average time: {sum(solved_times) / len(solved_times):.1f} s")
    print(f"Solved: {solved}, {100 * solved / len(data):.2f}%")

    return report


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--routes_json_path", "-r", type=str)
    parser.add_argument("--output_path", "-o", type=str, default="stats.csv")
    args = parser.parse_args()

    with open(args.routes_json_path, "r") as f:
        data = json.load(f)["data"]

    report = report_stats(data)
    with open(args.output_path, "w") as f:
        f.write("index,SMILES,solved\n")
        for s in report:
            f.write(f"{s[0]},{s[1]},{s[2]}\n")
