#!/bin/bash

log_dir=$(realpath log_dir)
echo $log_dir

python run_evaluation.py \
    --predictions_path predictions/swe_bench_lite_oracle__test.jsonl \
    --log_dir $log_dir \
    --swe_bench_tasks princeton-nlp/SWE-bench_Lite_oracle \
    --skip_existing

python get_report.py \
    --agent cheating_agent \
    --predictions_path predictions/swe_bench_lite_oracle__test.jsonl \
    --dataset_file princeton-nlp/SWE-bench_Lite_oracle \
    --log_dir $log_dir \
    > out/out_test.json