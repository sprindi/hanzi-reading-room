# Optional audio generation

Running the website requires none of these tools: the MP3 files are already included.

The bundled recordings use Kokoro 1.1-zh (`zf_001`, speed 0.92). The generation script makes explicit phonemes from the bank's pinyin for each word, applies adjacent-third-tone changes within a word, and joins an `r` suffix as erhua. Context sentences and full dialogues use Misaki's Mandarin frontend. This is synthetic speech, not a professionally reviewed pronunciation recording corpus.

To regenerate after editing vocabulary:

1. Use a Python environment with `kokoro-onnx==0.6.1`, `misaki-fork[zh]==0.9.6`, `soundfile==0.14.0`, `numpy`, and `onnxruntime`. Install FFmpeg separately.
2. Download `kokoro-v1.1-zh.onnx` and `voices-v1.1-zh.bin` from the [official ONNX model release](https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.1), and `config.json` from the [original Mandarin model](https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh).
3. From the repository root, run `python authoring/generate-voice.py dist /path/to/model-files`. For a smaller batch, set `HANZI_VOICE_BATCH=100` and rerun until it says DONE. Existing complete clips are skipped. The bank switches to the new paths only after every recording is present.
4. Commit the updated `dist/audio/kokoro/`, `dist/practice-data.js`, `dist/voice-data.js`, and generated manifest. Never commit the model directory or a Python environment.

The model is only used during generation. The browser plays standard MP3 files and contacts no model service. Model attribution and license are in `dist/licenses/`; the Chinese font license is in `dist/fonts/`.


## Paper-practice bank

`paper/vocabulary.json` contains the numbered New Words lists checked against the supplied book pages. `paper/data.json` contains word, character and attested-phrase entries. Rebuild the data file from the repository root with `node authoring/paper/build-data.cjs`. It uses the existing dialogue pronunciation alignment and original voice manifest.

Optional recording regeneration, with the same Python dependencies and downloaded model directory as above: `python authoring/paper/generate-audio.py dist /path/to/models`. Models are build tools only. The generated MP3s and `paper-voice-manifest.json` are included, so normal clones need no voice tools.

`node authoring/test-paper.cjs` checks learning gates, all 15 chapter lists, safe cumulative questions, delayed answer reveal, refresh state and complete local audio coverage. The five-minute interval is the learner-requested practice duration.
