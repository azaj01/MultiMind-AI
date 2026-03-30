# MultiMind AI — Benchmark Report

**Generated:** 2026-03-30T12:35:34.426463+00:00

**Total runtime:** 310.1s

**Models:** llama3.2:3b

**Council advisors:** qwen3.5:4b, ministral-3:3b, qwen3-4b-instruct, llama3.2:3b

---

## gsm8k_mini

### Accuracy

| Model | Mode | Accuracy | Correct | Total | Median Time |
|-------|------|----------|---------|-------|-------------|
| llama3.2:3b | hard | 20.0% | 1 | 5 | 34.8s |
| llama3.2:3b | medium | 60.0% | 3 | 5 | 19.9s |
| llama3.2:3b | off | 80.0% | 4 | 5 | 2.6s |

### Reasoning Effort Delta

| Model | off | medium | hard | Δ(medium-off) | Δ(hard-off) |
|-------|-----|--------|------|---------------|-------------|
| llama3.2:3b | 80.0% | 60.0% | 20.0% | -20.0% | -60.0% |

### Self-Correction (Hard Mode)

| Model | Self-Correction Rate |
|-------|---------------------|
| llama3.2:3b | 100.0% |

### Overhead vs Off Mode

| Model | Mode | Time Ratio | Char Ratio |
|-------|------|------------|------------|
| llama3.2:3b | medium | 7.5× | 9.4× |
| llama3.2:3b | hard | 13.1× | 15.9× |

---

## Cross-Suite Summary

| Suite | Best Model | Best Mode | Best Accuracy |
|-------|------------|-----------|---------------|
| gsm8k_mini | llama3.2:3b | off | 80.0% |
