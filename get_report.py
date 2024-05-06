import json
import swebench

def gen_report(
    agent_name: str,
    predictions_path: str,
    dataset_file: str,
    log_dir: str,
):
    report = swebench.get_model_report(
        model=agent_name,
        predictions_path=predictions_path,
        swe_bench_tasks=dataset_file,
        log_dir=log_dir,
        verbose=True,
    )
    for k, v in list(report.items()):
        report[k + "_count"] = len(v)
    report["resolved_rate"] = f"{report["resolved_count"] / (report["no_generation_count"] + report["generated_count"]):.1%}"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--agent",
        type=str,
        help="The agent to run.",
        required=True,
    )
    parser.add_argument(
        "--predictions_path",
        type=str,
        help="Path to predictions file (must be .json)",
        required=True,
    )
    parser.add_argument(
        "--dataset_file",
        type=str,
        help="Path to the SWE bench tasks file (must be .json)",
        required=True,
    )
    parser.add_argument(
        "--log_dir", type=str, help="Path to log directory", required=True
    )
    args = parser.parse_args()

    gen_report(
        args.agent,
        args.predictions_path,
        args.dataset_file,
        args.log_dir,
    )
