# ListenPost — legal documents

Public, version-controlled home of the privacy policy for **ListenPost**
(《聽哨》/《听哨》) by **Ashen Knight Games**.

Live: <https://legal.ashenknightgames.com/> (the GitHub Pages address <https://ashen-knight-games.github.io/listening-post-legal/> redirects there)

| File | |
|---|---|
| `privacy-policy.en.md` | **Authoritative version.** All others are translations. |
| `privacy-policy.zh-TW.md` | 繁體中文譯本 |
| `privacy-policy.zh-CN.md` | 简体中文译本 |
| `*.html`, `index.html` | **Generated — do not hand-edit.** Run `build.py`. |

## Why this repository is public

Under Section 11 of the policy, players retain the right to audit all previous revisions alongside their respective modification dates. Fulfilling this commitment strictly requires that this repository remains publicly accessible and its commit log unaltered.

- Force-Pushing is Strictly Prohibited: The commit history serves as audit trail evidence of the exact terms a player agreed to on any given date. Altering this ledger invalidates that proof.
- Maintain Public Availability: This repository must never be commercialized, set to private, or removed while any user data remains under our custody.
- Zero-Tolerance for Player Data Entry: Git logs are fundamentally immutable, which directly conflicts with the policy's right-to-erasure clause. Because these two mechanisms are mutually exclusive, all collected player analytics must reside exclusively on the production endpoint—this repository is designated for documentation only.

## Rebuilding the pages

```
pip install markdown
python3 build.py
```

Edit the `.md` sources, re-run, and commit the `.md` and `.html` together.
`build.py` is the only thing that writes the HTML.

## Hosting

The site deploys directly through GitHub Pages, tracking the `main` branch at the repository root. A `.nojekyll` file is intentionally included to ensure assets bypass the Jekyll compiler and serve exactly as they appear in the tree. The custom domain `legal.ashenknightgames.com` is set by the `CNAME` file in this repository plus a CNAME record in the domain's DNS pointing at `ashen-knight-games.github.io`; the default GitHub Pages address redirects to it.

This live URL must be manually linked within the Steamworks App Admin dashboard under the legal documents section. **Because the demo and the retail version operate on separate App IDs, you must apply this link to both configurations individually**.