# Space Moon Blog

Personal blog by Jihyung Moon. Hexo static site with Icarus theme.

## Project

- **Platform**: Hexo 7
- **Theme**: Icarus (in `themes/icarus`)
- **Posts**: `source/_posts/` — markdown with YAML frontmatter
- **Deploy**: GitHub Pages via `hexo deploy`
- **URL**: https://www.thespacemoon.com

## Commands

- `npx hexo server` — local dev server
- `npx hexo generate` — build static files to `public/`
- `npx hexo deploy` — deploy to GitHub Pages
- `npx hexo clean` — clear cache and generated files
- Requires **pandoc** installed locally (used by `hexo-renderer-pandoc`)

## Post conventions

- File names: English, kebab-case (e.g., `the-shrinking-moat.md`)
- Frontmatter: title, layout (post), date, tags, categories, toc, widgets
- `<!--more-->` marks the excerpt break
- `post_asset_folder: true` — images go in a folder matching the post name
- New posts target international audience — write in English
- `softly.ai` is dead — do not link to it
- Permalink format: `/:year/:month/:day/:title/` — dates matter for URL structure

## Review workflow

- Use `.claude/agents/post-reviewer.md` to review posts against writing style rules
- Run reviewer after writing or major edits, iterate on critical issues
- Reviewer scores: Directness, Concreteness, Honesty, Rhythm, Corporate Speak, Arc & Structure

## Writing style

Inspired by Paul Graham and Sam Altman. Follow these principles when writing or editing blog posts:

### Core philosophy

Writing that sounds good is more likely to be right. Rhythm reflects clear thinking — if a sentence reads awkwardly, the idea behind it is probably muddled. Use how writing sounds as a tool for checking whether the ideas are actually right.

### Rules

1. **Short sentences. Simple words.** If a shorter word works, use it. Never use jargon to sound smart.
2. **Be direct.** Say what you mean in the fewest words possible. Cut every sentence that doesn't earn its place.
3. **Ideas first, self second.** Lead with observations and insights, not personal announcements. Personal experience is evidence, not the point.
4. **Concrete over abstract.** Specific examples beat general claims. "We tested davinci on platform.openai.com" beats "we explored the latest AI models."
5. **Honest > polished.** Admit what didn't work. Bluntness builds trust.
6. **No corporate speak.** Never write "thrilled to announce", "incredibly grateful", "excited to share", or any LinkedIn filler.
7. **Constraint breeds clarity.** If something feels too long, the fix is usually a better idea, not just fewer words.
8. **Clumsiness signals problems.** When a passage feels awkward, don't just rephrase — rethink the underlying idea.
9. **Reread ruthlessly.** Good writers are first good readers of their own work.
