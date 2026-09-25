# .github

Org-level defaults for [The AI Merge](https://github.com/the-ai-merge).

The landing page you see on the organization profile lives in
[`profile/README.md`](profile/README.md) — GitHub renders that file, not this one.

## Assets

Everything visual is self-hosted under `profile/assets/`, so the profile does not
depend on a third-party badge or image service staying up:

| File | What it is |
| --- | --- |
| `header.svg` | Animated banner — a grid of squares sweeping left to right, styled after a contribution graph |
| `footer.svg` | Matching closing strip |
| `stack-covered.svg` | Tile grid of the technologies these repos cover |
| `pill-*.svg` | Header link buttons |
| `logo.svg` | The AI Merge mark |

Regenerate the grid and pills after editing the lists inside them:

```bash
python3 profile/assets/gen_stack.py
python3 profile/assets/gen_pills.py
```

Bump the `?v=` query on any changed image in `profile/README.md` afterwards —
`raw.githubusercontent.com` caches for five minutes and GitHub will otherwise
keep serving the old file.
