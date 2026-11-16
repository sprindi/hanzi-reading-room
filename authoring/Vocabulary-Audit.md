# Writing vocabulary audit

The chapter bank now includes each numbered New Words entry, the printed component subentries 出, 粉 and 红, and every distinct written vocabulary form in the existing 60-dialogue transcription. Chapter lists are deduplicated by written form; original textbook entries and their readings are retained. The numbered lists were cross-checked with the supplied PDF vocabulary appendix (PDF pages 139–145). The standalone supplementary vocabulary appendix (PDF page 146), grammar-only examples and warm-ups are outside these chapter pools unless their vocabulary also occurs in the dialogues.

`vocabulary-coverage.csv` records chapter totals. Coverage checks compare each chapter against every word in the prior dialogue vocabulary bank, every numbered entry and the component subentries. Tests also check local audio and stroke counts.

Stroke totals come from Unicode Unihan kTotalStrokes (first listed value, summed across the word). The practical timing policy is 1 minute up to 20 strokes, 2 minutes for 21–35, 3 minutes above 35. The policy is a pacing preference rather than a validated teaching threshold. Wrong items are targeted for repetition without automatically forcing three minutes.

English glosses for additional dialogue vocabulary use the CC-CEDICT subset. Meanings already supplied with the textbook vocabulary or dialogue focus words take precedence. Dictionary glosses are matched to the reading when possible. Source and license information is in dist/licenses.

All original word identifiers remain available. Existing rounds migrate to a separate saved-round namespace so expanding the chapter pool neither drops old attempts nor hides newly added words behind completed old batches.
