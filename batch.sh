#!/bin/bash

# List of arguments
args=("pg_cnn2" "a3c_gcn_seq2seq" "pg_cnn_qos" "pg_seq2seq" "gae_clustering" "pg_mlp" "hopfield_network" "pg_cnn" "mcts" "**_**" "ga" "ts" "pso" "aco" "sa" "pl_rank" "nrm_rank" "grc_rank" "rw_rank" "rw_rank_bfs" "mip" "r_rounding")

# Create a directory for log files
log_dir="logs"
mkdir -p "$log_dir"

# Loop through each argument and run the Python script
for arg in "${args[@]}"; do
    log_file="$log_dir/$arg.log"
    echo "Running with argument: $arg"
    python min.py "$arg" > "$log_file" 2>&1  # Redirect stdout and stderr to log file
    echo "----------------------------------"
done
