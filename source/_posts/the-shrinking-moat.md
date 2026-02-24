---
title: "The Shrinking Moat"
layout: post
date: 2026-02-22 09:00
tags:
- startup
- AI
- LLM
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

In mid-2022, I typed a prompt into platform.openai.com and got back something that didn't feel like a demo.

It was text-davinci-002. Before ChatGPT, before the hype. But it wasn't the output that mattered. It was the feeling: this is going to break everything we know about building AI products.

Building a good AI model meant collecting data, training, and fine-tuning for specific tasks. Hard, slow, expensive work. Davinci-002 could do a rough version of most of it with just a prompt — plain English, no data, no training, no cost.

My co-founders and I were already building softly, an AI startup. A few months later, ChatGPT launched and everyone else felt it too.
<!--more-->

## The arms race

When OpenAI was just an API company, we thought small LLMs plus RAG was our moat. We sold to other startups who wanted to steer models with their own knowledge — something OpenAI's raw API couldn't do out of the box. That lasted about six months. OpenAI launched function calling in June 2023, then the Assistants API with built-in retrieval that November. RAG became a feature, not a product.

So we moved to agents. Multi-step reasoning, tool use, orchestration across systems. Agents felt defensible — they required domain knowledge, custom workflows, real integration work. Then o1 arrived in September 2024. Reasoning became a service. The gap shrank again.

We retreated further into domain-specific agent software. Surely the combination of deep vertical knowledge and agent architecture would hold. But by early 2025, o3 and o4-mini made it clear: every layer we built was getting absorbed into the next release.

Each moat lasted months, not years. And each time we moved, we moved further from what we were actually good at.

## What I got wrong (as an AI startup founder)

We didn't expect OpenAI to move that fast. But speed wasn't the only thing I got wrong.

**I underestimated LLM companies' appetite.** I assumed they'd stay in the infrastructure layer — selling APIs, not building applications. They didn't. LLM companies turned out to be better at building LLM-based software than anyone else, because they control the foundation. Anything an application startup built on top, they could absorb — just by shipping it as a feature.

The application layer wasn't safe ground. It was their roadmap.

**I underestimated domain knowledge.** I thought we could learn how any industry works. We told ourselves we were fast learners. But the real information in any industry is hidden. It lives in relationships, in operational details that nobody writes down, in years of pattern-matching that insiders don't even recognize as knowledge. And we had no way in. No network, no warm introductions. You can't cold-call your way into domain expertise.

**I underestimated our own core strength.** Our team was built to train AI models. That was what we were genuinely good at. But the arms race spooked us. Instead of leaning into model development, we ran from it. We pivoted to AI-powered software — which requires product and go-to-market skills we didn't have. We traded our strongest card for a hand we couldn't play.

**I underestimated market size.** Everyone talks about TAM in pitch decks. I nodded along like I understood. I didn't — not until I felt it. Our last pivot landed us in Korea's aesthetic medicine market — where a single procedure costs thousands of dollars, the industry is growing fast, and Korea is genuinely world-class at it. The difference between a $10 market and a $10,000 market isn't just revenue — it's how much room you have to be wrong.

## Now it's SaaS

I'm watching the same pattern play out again — this time with B2B SaaS.

As LLMs got more capable, the next question became obvious: who would own the connection layer between the model and everything else? OpenAI moved first with GPTs — a closed ecosystem. Anthropic took the opposite approach — open the protocol, let others build on it. That's how MCP was born. MCP won. Even OpenAI adopted it when they launched [Apps in ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/).

The value is migrating from the UI to the chat. I stopped opening Slack, Jira, and Notion in separate tabs — [Claude Code](https://claude.com/code) talks to all of them through [MCP connectors](https://claude.com/connectors). [Claude Cowork](https://claude.com/product/cowork) does the same for non-developers. The LLM is becoming the interface for everything.

Wall Street traders are calling it the "SaaSpocalypse"[^1]. SaaS companies are building their own AI agents, but they're competing against LLM plus MCP — one native interface for everything.

When AI is the user, a beautiful dashboard doesn't matter.

Per-seat subscriptions stop making sense. The companies that survive are the ones sitting on years of accumulated data — the rest become commoditized tools behind an LLM. The models aren't fully autonomous yet[^2] — but as they get closer, this only accelerates.

## B2C is next

B2C is where I am now — and it's not there yet. OpenAI built an [Apps SDK](https://github.com/openai/apps-sdk-ui) to let developers render rich UI inside ChatGPT. [MCP-UI](https://mcpui.dev/) is taking the open protocol approach — GPTs versus MCP, all over again. But neither has gained real traction.

The problem is deeper than interface. A recommendation without rejected alternatives doesn't feel like a decision — it feels like a guess. People choosing a clinic or a hotel need to browse, filter, and compare. They build confidence by ruling out the wrong options, not just finding the right one. Chat alone can't replace that.

The moat keeps shrinking. I don't know what the B2C version of this looks like yet. But if the pattern holds, the last ones standing won't be the ones with the best interface or the smartest model. They'll be the ones holding data that no LLM can generate on its own.

[^1]: https://finance.yahoo.com/news/traders-dump-software-stocks-ai-115502147.html
[^2]: https://www.anthropic.com/research/measuring-agent-autonomy
