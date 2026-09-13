# OmniVoice Studio (`comp/`)

A local voice-cloning workstation built on OmniVoice: a FastAPI synthesis
server, a Tkinter studio (reference-clip maker, clip merger, generator) and a
thin Windows installer. Everything runs from this folder's own `.venv`; no
model weights, reference clips or generated audio are tracked in git.

```
comp/
  server/app.py        POST /synthesize {text, ref_audio?, instruct?, language?, guidance_scale?, asmr?}
                       GET  /audio/<file>.wav   GET /health
  server/asmr_fx.py    ASMR post-processing presets (close | room | drift) used by `asmr`
  server/asmr_ref.py   analyze normal-vs-whisper clip pairs; derive a whisper reference (LPC / TTS)
  gui/studio.pyw       the studio: Ref maker | Merge | Generate | Server tabs
  gui/refmaker*.py     ffmpeg extract -> optional demucs vocals -> silence-split candidates -> clean ref
  installer/           PyInstaller launcher + Inno Setup script (the exe only remembers this folder)
  tests/               listening-set generator, ref-maker unit tests
  ref/                 the server's startup default voice: put default_ref.wav here (ignored)
  ref-input/           long, dirty source rips for the ref maker (ignored)
  ref-output/          clean reference clips the studio produces (ignored)
```

## Setup (Windows, NVIDIA)

```powershell
cd comp
py -3.12 -m venv .venv
.venv\Scripts\pip install torch==2.8.0+cu128 torchaudio==2.8.0+cu128 --extra-index-url https://download.pytorch.org/whl/cu128
.venv\Scripts\pip install omnivoice httpx soundfile scipy librosa demucs
copy <your 5-15 s clean clip> ref\default_ref.wav
```

Run the server (first start downloads the model):

```powershell
.venv\Scripts\python.exe server\app.py --host 0.0.0.0 --port 9192 --ref-audio ref\default_ref.wav
```

Run the studio: `gui\studio.bat` (or `gui\launch.bat` for the generator alone).

Build the installer: `installer\build.bat` (needs PyInstaller in the venv and Inno Setup 6).
The installed "OmniVoice Studio" asks for this folder once and launches the studio from its venv.

## Notes

- `ref_audio` in a request must live under `ref/`, `ref-output/` or `ref-input/`; anything else is
  refused, because the endpoint has no auth and would otherwise be a filesystem oracle.
- `instruct` (e.g. `female, young adult`) only applies to voice *design*. With a cloning reference
  present OmniVoice ignores it, so a whispered voice needs a whispered reference clip
  (see `server/asmr_ref.py analyze` for what actually differs, measured on paired recordings).
- `asmr` = `close | room | drift` post-processes the result and returns stereo.
- Short-text degeneration guard: the server enforces a duration floor and retries a
  degenerate output once (see the top of `server/app.py`).
