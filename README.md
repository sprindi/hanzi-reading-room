# Hanzi Reading Room

A self-contained study website with reading material, practice exercises, and a remembered light/dark theme. Progress stays in your browser.

## Run locally

Requires Python 3. From this folder, run:

```sh
python3 -m http.server 18769 --bind 127.0.0.1 --directory dist
```

Then open http://127.0.0.1:18769/ . On Windows, use `py` instead of `python3`.

## Files and deployment

`dist/` contains the complete website: editable HTML, CSS, JavaScript, and study content. No dependency installation or build is required. Serve `dist/` with any static website host.

For Vercel, import this repository, choose Other as the framework, leave the build command empty, and set the output directory to `dist`.

## Content

The study material is based on course documents or a supplied textbook. Original third-party material retains its respective ownership; this repository does not grant a license to that material.

The reader covers 60 HSK Standard Course 2 dialogues across 15 lessons. Hover over dialogue characters for pinyin; exercises stay Hanzi-only. The night theme preserves the original orange accents.
