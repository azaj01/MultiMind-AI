#!/usr/bin/env bash
# =============================================================================
# Standard Benchmarks via lm-evaluation-harness
#
# Runs GSM8K, HumanEval, MMLU-Pro (500 subset), TruthfulQA, and IFEval
# against Ollama for raw model baseline performance.
#
# Prerequisites:
#   1. Ollama running: ollama serve
#   2. Models pulled: ollama pull qwen3.5:0.8b qwen3.5:4b qwen3.5:9b
#   3. lm-evaluation-harness installed: pip install lm_eval[api]
#
# Usage:
#   chmod +x benchmarks/run_standard_benchmarks.sh
#   ./benchmarks/run_standard_benchmarks.sh
# =============================================================================

set -euo pipefail

OLLAMA_URL="http://127.0.0.1:11434/v1"
OUTPUT_DIR="benchmarks/results/standard"
MODELS=("qwen3.5:0.8b" "qwen3.5:4b" "qwen3.5:9b")

# Tasks to run (these are lm-evaluation-harness task names)
# NOTE: Some tasks may not work with chat-completion APIs (loglikelihood-based).
#       gsm8k_cot and truthfulqa_mc2 are the safest bets.
TASKS=(
    "gsm8k_cot"          # GSM8K with Chain-of-Thought (generative)
    "truthfulqa_mc2"     # TruthfulQA multiple choice v2
    "ifeval"             # Instruction Following Evaluation
)

mkdir -p "$OUTPUT_DIR"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║     Standard Benchmarks via lm-evaluation-harness       ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Ollama URL: $OLLAMA_URL"
echo "Models:     ${MODELS[*]}"
echo "Tasks:      ${TASKS[*]}"
echo "Output:     $OUTPUT_DIR"
echo ""

# Check if lm_eval is installed
if ! command -v lm_eval &> /dev/null; then
    echo "ERROR: lm_eval not found. Install with:"
    echo "  pip install lm_eval[api]"
    exit 1
fi

# Check if Ollama is running
if ! curl -s "$OLLAMA_URL/../api/tags" > /dev/null 2>&1; then
    echo "WARNING: Ollama may not be running at $OLLAMA_URL"
    echo "Start it with: ollama serve"
fi

for model in "${MODELS[@]}"; do
    echo ""
    echo "═══════════════════════════════════════════════════════"
    echo "Model: $model"
    echo "═══════════════════════════════════════════════════════"

    for task in "${TASKS[@]}"; do
        echo ""
        echo "▶ Running: $task"

        # Create safe filename from model name
        safe_model=$(echo "$model" | tr ':/' '_')
        result_file="$OUTPUT_DIR/${safe_model}__${task}"

        lm_eval \
            --model local-chat-completions \
            --model_args "model=${model},base_url=${OLLAMA_URL},num_concurrent=1,max_retries=3,tokenized_requests=False" \
            --tasks "$task" \
            --output_path "$result_file" \
            --log_samples \
            --batch_size 1 \
            2>&1 | tee "${result_file}.log"

        echo "  ✔ Results saved to: $result_file"
    done
done

echo ""
echo "═══════════════════════════════════════════════════════"
echo "All standard benchmarks complete!"
echo "Results: $OUTPUT_DIR"
echo "═══════════════════════════════════════════════════════"
