# Hexo 7 + Icarus 6 Upgrade Design

## Goal
Upgrade from Hexo 4.2.1 + Icarus 3.1.0 to Hexo 7.3.0 + Icarus 6.1.1 to fix Node v25 compatibility and resolve 69 npm vulnerabilities.

## Current State
- Hexo 4.2.1, Icarus 3.1.0 (git submodule), hexo-component-inferno 0.4.0
- node-sass / hexo-renderer-sass broken on arm64 / Node 25
- node_modules in mixed broken state
- 10 posts, 2 with KaTeX math (display math `\[...\]` only)
- No removed Hexo 7 tags (youtube/gist/jsfiddle/vimeo) used

## Upgrade Steps

### Phase 1: Research (done)
- Hexo 7.3.0 is latest 7.x, requires Node 14+
- Icarus 6.1.1 targets hexo ^7.1.1, uses Stylus (not Sass)
- No posts use removed Hexo 7 tags
- 2 posts use KaTeX math — need rendering verification

### Phase 2: Package upgrades
Remove:
- hexo-renderer-sass (dead, Icarus 6 uses Stylus)
- node-sass alias (no longer needed)
- hexo-renderer-markdown-it-plus (already removed)
- hexo-inject (deprecated, Icarus 6 doesn't need it)

Upgrade in package.json:
- hexo: ^4.2.1 → ^7.3.0
- hexo-component-inferno: ^0.4.0 → ^3.1.0
- inferno / inferno-create-element: ^7.4.2 → ^8.2.0
- hexo-deployer-git: ^2.1.0 → ^4.0.0
- hexo-generator-archive/category/feed/index/tag: latest compatible
- hexo-renderer-stylus: ^1.1.0 → ^3.0.0
- hexo-renderer-inferno: ^0.1.3 → ^0.1.4
- All other deps to latest compatible versions

### Phase 3: Icarus theme upgrade
- Update submodule to Icarus 6.1.1 tag
- Migrate theme _config.yml:
  - version: 3.0.0 → 5.1.0
  - Remove article.thumbnail (removed in v4)
  - Add plugins.pjax: false (prevent PJAX from breaking KaTeX/Disqus/GA4)
  - Carry over: GA4 ID, social links, Disqus config, widget layout, KaTeX enabled

### Phase 4: Hexo config migration
- _config.yml: use_date_for_updated → updated_option (Hexo 5 change)
- Verify highlight config syntax (Hexo 7 made it explicit)

### Phase 5: Verify
- hexo clean && hexo generate (zero errors)
- hexo server — check home, about, math posts, code blocks, sidebar, RSS, sitemap
- Specifically verify: basics-of-quantum-computings.md and naver-news-Comments-Analysis-3.md for KaTeX
- View source for GA4 gtag.js snippet
- hexo deploy

## Risk Areas
1. KaTeX rendering — 2 posts use display math, renderer must handle `\[...\]`
2. Icarus config migration — widget layout may need adjustment
3. markdown-it vs pandoc — still have both, may conflict (separate concern)

## Safety
- Work in git worktree, merge only after verification
