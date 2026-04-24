# compression_eval

Offline eval harness for `agent/context_compressor.py`. Runs a real
conversation transcript through the compressor, then probes the
compressed state with targeted questions graded on six dimensions.

**Status:** design only. See `DESIGN.md` for the full proposal and
open questions. `run_eval.py` is a placeholder.

## When to run

Before merging changes to:

- `agent/context_compressor.py`
- `agent/auxiliary_client.py` routing for compression tasks
- `agent/prompt_builder.py` compression-note phrasing

## Not for CI

This harness makes real model calls, costs ~$1 per run on a mainstream
model, takes minutes, and is LLM-graded (non-deterministic). It lives
in `scripts/` and is invoked by hand. `tests/` and
`scripts/run_tests.sh` do not touch it.

## Usage (once implemented)

```
python scripts/compression_eval/run_eval.py
python scripts/compression_eval/run_eval.py --fixtures=401-debug
python scripts/compression_eval/run_eval.py --runs=5 --label=my-prompt-v2
python scripts/compression_eval/run_eval.py --compare-to=results/2026-04-24_baseline
```

Results land in `results/<label>/report.md` and are intended to be
pasted verbatim into PR descriptions.

## Fixtures

Small, scrubbed session snapshots checked in under `fixtures/`. See
`DESIGN.md` § "Sourcing fixtures" for the scrubbing checklist — a
fixture should read like public sample code.

## Related

- `agent/context_compressor.py` — the thing under test
- `tests/agent/test_context_compressor.py` — structural unit tests
  that do run in CI
- `scripts/sample_and_compress.py` — the closest existing script in
  shape (offline, credential-requiring, not in CI)
