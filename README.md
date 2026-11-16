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

For Vercel, import this repository, choose Other as the framework, leave the build command empty, and set the output directory to `dist`. [Vercel static build settings](https://vercel.com/docs/builds/configure-a-build).

## Content

The study material is based on course documents or a supplied textbook. Original third-party material retains its respective ownership; this repository does not grant a license to that material.

The reader covers 60 HSK Standard Course 2 dialogues across 15 lessons. Hover over dialogue characters for pinyin. Dialogue exercises stay Hanzi-only; matching and paper tests have their own pinyin prompts. The night theme preserves the original orange accents.

## Matching and whole-word writing

**Match characters** keeps the existing character-to-pinyin exercise. **Write words** is the paper-writing activity, replacing Listen & write.

Each chapter includes its listed new vocabulary and the words used in its four dialogues, with duplicate written forms removed. For example, Chapter 1 has 58 practice words (12 numbered new entries) and Chapter 6 has 63 (13 numbered new entries). See `authoring/vocabulary-coverage.csv` for all totals and `authoring/Vocabulary-Audit.md` for scope. Standalone supplementary appendix vocabulary outside the chapter dialogues is not silently assigned to chapters.

The chapter page shows one total, progress and a single next-round button. **View all words** reveals the full list; **Choose another round** and settings are collapsed. Rounds contain up to ten words and the final short round uses its actual size. It does not add familiar words to disguise the smaller total.

Timing uses each word’s total stroke count from Unicode Unihan: up to 20 strokes gets 1 minute, 21–35 gets 2 minutes and more than 35 gets 3 minutes. Hanzi hides halfway through while pinyin remains, then the next word starts automatically. Missed items receive targeted review without an automatic three-minute penalty.

After practice, a ten-second countdown starts the spoken/pinyin test. Each prompt advances after fifteen seconds, beginning when its audio starts. Hanzi stays hidden until the test ends. Learners self-mark correct or wrong, then can practise and retest only missed words or phrases. Playback failure pauses the test. Leaving the tab pauses practice.

The writing screen contains the word, pinyin, optional meaning, one countdown, Listen and Pause. Extra controls are under Word options. Old rounds, test positions, marks, timers and return-to-learning sessions are preserved when the expanded vocabulary loads.

Progress uses the existing IndexedDB store with a localStorage recovery copy. Word sets, copy/recall/check stage, timer, test order, written marks and results survive refresh and are included in full-progress backups. Former isolated-character writing sessions and scores are retained in backup history, without claiming the learner has practised whole words. Normal clones include all voice recordings; no runtime speech server or key is needed.

## Learning layout

The main navigation separates Read, Match characters, Write words, and Review. Reading follows three visible stages: Read the dialogue → Check meaning → Read again. The next action stays visible while reading. The Lessons button opens the book library; reading tools and backup controls are grouped separately. The original orange accent remains in both themes. A compact subset of Noto Serif CJK SC is bundled, with its OFL license in `dist/fonts/`.

## Portable Mandarin voice

The site includes finished MP3 recordings generated with **Kokoro v1.1-zh, voice zf_001**, at a slightly slower reading pace. Word recordings use the vocabulary bank’s specified pinyin, including contextual reading variants. The bank also includes spoken example sentences and recordings for all 60 dialogues. Model: https://huggingface.co/hexgrad/Kokoro-82M-v1.1-zh . Model attribution and Apache-2.0 license are included under `dist/licenses/`. These are synthetic recordings.

All playable recordings are ordinary files in `dist/audio/kokoro/` and `dist/audio/paper/`. Paper character and phrase recordings use the specified book pinyin, with a separate manifest in `authoring/paper-voice-manifest.json`. They should be committed to Git alongside the website, without Git LFS or an external audio bucket. A normal complete clone or source ZIP therefore includes the same voice. No API key, speech server, browser-installed Mandarin voice, or connection to the original author’s PC is required. The model itself is a generation tool and is not needed to run the site.

For Vercel, deploying `dist/` deploys these audio files with the pages. For local use, the Python command above serves both the pages and recordings. Regenerating audio is optional and requires the separate tools described in `authoring/README.md`.

## Exercise checks

Optional, with Node.js: `node authoring/test-paper.cjs` checks chapter coverage, learning gates, safe cumulative tests, timer state, answer reveal, self-check persistence and bundled recordings.  `node authoring/test-core.cjs` checks exercise state rules and migration; `node authoring/test-dialogues.cjs` checks all 180 dialogue activities. These do not require browser libraries or change learner progress. The core flow was also checked in the browser through a complete 10-word dictation round, delayed answer reveal, paper marking, saved speed, activity switching and refresh recovery.


Use the clickable **Learn the words** step or **Back to Learn words** from a test, answer check or result. The current test is parked with its remaining time and answers intact. Relearning runs as a separate saved practice view; **Return to saved activity** restores the parked question or result. Completed sets also offer **Learn words again** in the chapter list.
