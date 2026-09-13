"""Shared temp-workdir management for the refmaker / merge pipelines.

Both refmaker_tab and merge_tab decode a full-length WAV (+ demucs vocals) into a
throwaway workdir under %TEMP%. Historically these dirs were created with
`tempfile.mkdtemp(...)` and never removed, so every Analyze / Cut&Merge run left a
1-3 GB folder behind forever (28 GB observed across 15 runs).

This module is the single source of truth for creating and reaping those dirs:

    sweep_stale("refmaker_")            # at startup: delete leftovers from past runs
    wd = new_workdir("refmaker_")       # per run: fresh dir, remembering the previous
    ...                                 # (source_path may point INSIDE wd, so we only
                                        #  delete the PREVIOUS one, not this one)
    remove_workdir(wd)                  # on window close: final cleanup

Kept Tk-free so it stays unit-testable.
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

TEMP_ROOT = Path(tempfile.gettempdir())


def new_workdir(prefix: str) -> Path:
    """Create and return a fresh throwaway workdir under %TEMP%."""
    return Path(tempfile.mkdtemp(prefix=prefix, dir=TEMP_ROOT))


def remove_workdir(path: str | Path | None) -> None:
    """Best-effort recursive delete of a single workdir. Never raises."""
    if not path:
        return
    shutil.rmtree(path, ignore_errors=True)


def sweep_stale(prefix: str, keep: str | Path | None = None) -> int:
    """Delete every `<TEMP>/<prefix>*` dir except `keep`. Returns count removed.

    Called at tab startup so orphans from crashed / force-quit past sessions
    (which no live workdir still references) don't accumulate.
    """
    keep_path = Path(keep).resolve() if keep else None
    removed = 0
    for entry in TEMP_ROOT.glob(f"{prefix}*"):
        if not entry.is_dir():
            continue
        if keep_path is not None and entry.resolve() == keep_path:
            continue
        shutil.rmtree(entry, ignore_errors=True)
        removed += 1
    return removed
