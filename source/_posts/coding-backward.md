---
title: "Coding Backward"
layout: post
date: 2026-03-24 10:00
description: "AI didn't replace each step of development. It changed where humans review."
tags:
- AI
- Engineering
categories:
- Tech
- Engineering
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

I'd never built an app before. Claude Code made me think I could.

Backend is my world — I've done it for years. API design, data modeling, infrastructure. But the app side? I didn't know React Native from Expo, let alone how navigation stacks or state management worked on the client side.

The usual approach: read the docs, understand the framework, design the architecture, then write code. I did the opposite. I opened Claude Code, described what I wanted, and started building. When something broke, I fixed it. When something worked, I moved on. I learned why things worked by watching them work — or fail.

I coded backward.

<!--more-->

## Backward from where I can review

For the backend, I read the AI's code and judged it immediately. Data modeling, error handling, API structure — I knew what correct looked like. When Claude Code made a decision I disagreed with, I caught it in the code, before running anything. The review happened early because I had the frame of reference to question the choices.

For the frontend, I couldn't do that. I didn't know enough to read a React Native component and tell good from bad. So I reviewed later — when I ran the app, tapped through screens, and something felt wrong or broke. The review point moved from the code to the result.

Early on, I started the way a human team would: build the frontend with mock data, connect the real API later. But with AI, I quickly started building frontend and backend at the same time. The mock data became dead code the moment real endpoints went live. I missed it — I was reviewing the features, not the scaffolding. By the time I found it, mock data was scattered across the codebase. My review didn't catch it because I didn't know to look there.

I didn't stop studying, designing, and coding — those steps collapsed into one. My job became review. Where I reviewed depended on what I already knew.

## What made backward possible

The old way of building software — design carefully, get each step right before moving on — wasn't arbitrary. It was rational. Because fixing was expensive.

### The economics

Changing architecture meant rewriting modules. If you wanted to refactor a component tree, you had to trace every dependency. Going back cost days or weeks. A wrong early decision compounded through every layer built on top of it. So you invested heavily upfront: anticipate future needs, get the data model right, think three steps ahead. The cost of prevention was lower than the cost of repair.

Then the economics flipped.

The cost of AI-assisted refactoring had been dropping for a while — Copilot, Cursor, earlier Claude versions all made it faster. But when Anthropic dropped the 2x surcharge on long context[^1] and 1M tokens hit standard pricing, the shift stopped feeling theoretical.

Claude could hold my entire codebase in one pass. Its output was better aligned with the existing code and cheaper than before. When I asked it to rewrite a module, it traced imports across files I'd forgotten existed. I stopped thinking about whether a refactor was "worth it." The technical cost of fixing collapsed.

### The social cost

In the old world, asking someone to redo their work had friction. You'd soften the feedback, batch your requests, sometimes accept "good enough" to avoid the conversation. Asking a question you felt you should already know the answer to was embarrassing. Every interaction carried emotional overhead.

AI doesn't complain. You can ask a basic question without feeling stupid. You can hand it the most tedious scaffolding task without guilt. You can say "redo this completely" ten times and it doesn't push back, get tired, or lose motivation. I became bolder — not because I got smarter, but because the friction disappeared.

Everyone talks about the economics — AI is faster, cheaper. But I think the social cost was the bigger barrier. You can push through a slow refactor if you have to. It's harder to push through the discomfort of asking someone to redo their work for the third time.

## The bet

I'm still testing whether "build fast and fix" actually beats "think deeply and build once." The app will tell me. If it ships and holds up — if the architecture doesn't collapse under its own weight, if the decisions I couldn't judge turn out to be sound — then coding backward works. If it doesn't, I'll know exactly where my review failed.

The code AI writes on its first pass is still not great. But show it the whole picture and ask it to refactor, and it improves. It can't reason about the full picture in a single shot. So it compensates with repetition: build, see the result, refactor, review, repeat. What it lacks in depth it makes up in cycles.

But the reviewer has blind spots too. AI can't fill gaps I don't know I have. The problems are probably already in the codebase — they just haven't surfaced yet. That's what makes this uncomfortable. Not that the process is new, but that I won't know if it failed until later.

Trusting a process built on "fix it later" doesn't sit right — not after years of training myself to get it right the first time. But I'm learning backward. Understanding why things work by watching them work.

I'm coding backward. It's faster. It's cheaper. And the thing I'm betting on is that I can learn backward fast enough.

[^1]: [1M context now generally available](https://claude.com/blog/1m-context-ga)
