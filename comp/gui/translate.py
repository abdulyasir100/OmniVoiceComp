"""English -> Japanese translation via the Claude CLI.

Used by app.pyw when the "Translate to Japanese" toggle is on: the English the
user typed is translated to natural spoken Japanese, then that Japanese is what
gets sent to the OmniVoice TTS server.

No API key needed — shells out to the installed `claude` CLI in one-shot mode.
"""

from __future__ import annotations

import subprocess
import sys

_CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0

_PROMPT = (
    "Translate the following English into natural, casual spoken Japanese suitable "
    "for text-to-speech. Output ONLY the Japanese — no romaji, no quotes, no "
    "explanation, no notes. Keep any [bracketed] tags unchanged.\n\n"
)


def to_japanese(text: str, claude_exe: str = "claude", timeout: float = 90.0) -> str:
    """Translate English text to Japanese. Raises RuntimeError on failure/empty output."""
    text = text.strip()
    if not text:
        raise RuntimeError("Nothing to translate.")
    try:
        proc = subprocess.run(
            [claude_exe, "-p", _PROMPT + text],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            creationflags=_CREATE_NO_WINDOW,
        )
    except FileNotFoundError:
        raise RuntimeError(
            f"Claude CLI not found ('{claude_exe}'). Install it or check PATH."
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"Translation timed out after {timeout:.0f}s.")

    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or proc.stdout or "").strip().splitlines()[-8:])
        raise RuntimeError(f"Claude CLI failed:\n{tail}")

    out = (proc.stdout or "").strip()
    if not out:
        raise RuntimeError("Claude CLI returned empty output.")
    return out
