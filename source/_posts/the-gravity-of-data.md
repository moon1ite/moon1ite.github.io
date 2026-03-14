---
title: "The Gravity of Data"
layout: post
date: 2026-03-12 10:00
description: "Your MCP connections reveal who survives the AI shift — the ones holding data that LLMs can't generate on their own."
tags:
- AI
- Startup
categories:
- Startup
toc: true
language: en
widgets:
   - type: toc
     position: left
   - type: categories
     position: left
   - type: recent_posts
     position: left
---

I looked at my MCP connections and realized which companies survive the AI shift — and which don't.

<!--more-->

## What my MCP setup revealed

I use Claude Code as my primary interface for work. Over the past few weeks, I've connected it to a handful of tools via MCP: Amplitude, Notion, Braze. Claude Code already reads the codebase directly — no GitHub connector needed.

I tried Figma. It didn't stick — not because the connector was bad, but because Claude Code didn't need it. It could already see the code, read user behavior in Amplitude, pull interview notes from Notion, and see the design system in Storybook. What would it learn from a Figma file that the code didn't already say?

That gap is the tell. Some tools hold data that matters. Others hold descriptions of data that matters.

## The Figma lesson

Figma might be the most successful B2B SaaS story of the last decade. Index Ventures led a $3.8 million seed round in 2013. By 2022, Adobe offered $20 billion to acquire it. When the deal fell through on regulatory grounds, Figma IPO'd in July 2025 and hit $68 billion on day one[^1].

Five months later, the stock had fallen 81%. Market cap back to roughly $18 billion — less than Adobe's original offer[^2].

What happened between July 2025 and January 2026 wasn't a management failure. Most companies still work the same way: a designer opens Figma, builds a component, hands it off to engineering. I skip that step. I describe what I want and Claude Code builds it. If it's wrong, I say so and it fixes it. When I need to communicate the design — for a PRD or a handoff — I share the rendered frontend, not a Figma file.

The problem is structural. Figma sits between intent and execution. When an LLM closes that gap, the middle layer has nowhere to go.

Figma was the most efficient way to communicate what code should look like to another human[^3]. When the executor is an LLM, that communication layer becomes overhead. The design doesn't disappear because it's bad. It disappears because the code *is* the design now.

## Primary data vs. coordination data

Look at which tools you'd connect an agent to if it had to actually do your job:

**Primary data — the agent needs this to act:**

- **Amplitude**: the user behavior, what people actually do
- **Notion**: the product specs, the institutional knowledge, the decisions that shaped the system
- **Braze**: the customer segments, the messaging history, the engagement patterns

**Coordination data — the agent can skip this:**

- **Figma**: a description of what the code should look like
- **Jira**: a description of what work should be done
- **Slack**: a description of what's happening

Primary data is what the system *is*. Coordination data is what humans tell each other about the system.

## B2B information, B2C experience

For B2B, the direction is becoming clear. The moat is **information an LLM can't generate**. Ten years of commit history. Migration decisions that shaped your schema. Customer engagement patterns — in our Braze data, users in Seoul convert 3x better from a Kakao message on Thursday evening than an email on Monday morning. An agent can write new code or draft a push notification, but it can't invent your system's past or your customers' behavior. That data is structurally irreplaceable. No one cold-starts a decade of commit history.

B2C is about to start. Google is building MCP into Android[^4] and Chrome[^5] — agents that won't just read apps, but control them. WebMCP turns websites into structured tool servers. When agents can navigate a checkout flow or book a flight without touching the UI, the same pattern from B2B applies: the UI becomes optional, the data underneath doesn't.

If the B2B pattern holds, the B2C moat will be **experience an LLM can't replicate**. A shopping app that learned what you actually buy, not what you say you want. A streaming service whose recommendations get better every night you watch. A character chatbot that remembers six months of conversation. These products survive because the experience improves with every interaction — and that history belongs to the platform. Your watch history, your purchase patterns, your conversation memory — that's not data you export. That's the product itself.

But B2C moats are more nuanced than B2B ones. Good personalization needs two kinds of data: deep knowledge of the user, and deep knowledge of the items. An LLM might cold-start the user side — guess your taste from a single conversation instead of three years of behavior. But the item side is harder to replace. A streaming service's content metadata — mood, pacing, scene-level tags — is proprietary. A shopping app's supplier relationships, pricing dynamics, and inventory patterns are structural. The LLM can guess what you *want*. It can't guess what the platform *has*.

B2B data is structurally irreplaceable. B2C data depends on which side you're looking at.

## Who survives

Figma was a $68 billion company for one day. The market corrected not because the product got worse, but because the category got smaller.

The question for any company is the same one I asked my own MCP setup: when an LLM does the work, does it need your data? Or just your UI?

[^1]: [Figma IPO filing](https://finance.yahoo.com/news/figma-files-ipo-nearly-two-231113109.html)
[^2]: [AI is killing Figma: a capital structure problem](https://davefriedman.substack.com/p/ai-is-killing-figma-a-capital-structure)
[^3]: [Claude Code is re-shaping my design process](https://jlzych.com/2026/02/20/claude-code-is-re-shaping-my-design-process/)
[^4]: [Android Device Management MCP](https://developers.google.com/android/management/reference/mcp)
[^5]: [WebMCP: Chrome's Early Preview](https://developer.chrome.com/blog/webmcp-epp)
