---
title: "Customer Support Looks Easy. That's Why AI Can't Crack It."
layout: post
date: 2026-02-28 09:00
description: "We tried to automate customer support first. It turned out to be the hardest job of all."
language: en
tags:
- AI
categories:
- Startup
toc: true
widgets:
   - type: toc
     position: left
   - type: categories
     position: left
   - type: recent_posts
     position: left
---

At softly, we tried to automate customer support for clinics. The AI part worked — FAQs, multi-step lookups, even reasoning about clinic policies. The support part didn't.

People don't message a clinic to ask what's on the website. They want someone who knows the things the website doesn't say — can this procedure fix *my* specific case, will it hurt more than last time, if I'm combining two procedures which order matters — and who can solve their problem right now.

Each question is an edge case. Getting one wrong isn't just bad service — a hallucinated answer about a procedure is dangerous. Generalization and hallucination come from the same place.

But even accurate answers weren't enough. The job was conversion — turning that anxious inquiry into a patient who actually walks through the door. Every rule we wrote implied ten more we hadn't thought to write. The gap never closed.

<!--more-->

Coding agents already ship features[^1]. Design tools generate layouts from prompts. Customer support looks like the obvious next step — text-based work, recognizable patterns[^2]. In 2011, Gartner predicted that by 2020, customers would manage 85% of their relationship with an enterprise without interacting with a human[^3]. Fifteen years later, the job still exists.

## The easy jobs are hard

In 1988, Hans Moravec noticed something strange: the tasks easiest for humans — perception, social judgment, reading people's motivations — are hardest for machines[^4]. A billion years of evolution encoded these skills deep in the brain. Reasoning is the thin veneer on top — which is why machines learned it first. Our bot could reason through multi-step insurance lookups. It couldn't tell when a patient was too scared to ask what they actually wanted.

Behind every message was context the bot never saw — when they messaged, what marketing brought them in, their nationality, whether they were planning travel for the procedure. A human agent reads all of this without thinking — and knows what to say to get the patient through the door. Not the answer to the question they asked. The thing that was actually stopping them from booking. The bot sees text.

## Who closes the loop

Moravec tells you what's hard, but difficulty doesn't determine the order of automation[^5]. What matters is who judges the output.

**Closed** problems fall first — coding, math — where the answer checks itself. Code compiles or it doesn't. The proof holds or it doesn't.

**Semi-closed** problems follow — design, research, marketing. Human-in-the-loop works because one person controls the whole cycle: produce the work, review it, ship it.

Customer support is **open**. The worker doesn't close the loop — the customer does. They start it. They judge it. We couldn't tell if our bot's response was right until the patient didn't book.

Every workflow where the user and the judge are the same person can be solved incrementally: first assist the human, then automate.

But the core of customer support — conversion, trust, reading the patient — is judged by the customer, not the worker. Different people, different incentives. The customer has no reason to give feedback — so the loop never closes, and the copilot never improves on the work that matters.

## Why training can't close the gap

### No one wrote it down

In other jobs, knowledge is documented and managed by the worker — code has docs, designs have style guides, research has published methods. The knowledge is explicit, so it transfers to machines.

In customer support, the critical knowledge was never written down. The clinic staff who converted the most patients couldn't explain how they did it. "Experience." "Intuition." "I just read people." That's Polanyi's Paradox: we know more than we can tell[^6].

LLMs have cracked much of what can be articulated — abstract reasoning, procedural know-how. But embodied social knowledge — the kind built from reading people, not reading about them — doesn't make it into a text corpus. A smile, a pause, the instinct to follow up differently based on tone: none of it was ever written down[^7].

### The reward model optimizes for the wrong thing

RLHF trains a reward model from annotator preferences — a proxy for "good." This proxy is subject to Goodhart's Law: optimize hard enough against it, and it diverges from the real objective. For coding, the divergence self-corrects — bad code fails visibly, so annotator judgments track reality.

For customer support, "helpful" can't be annotated in isolation. Whether a response is good depends on the product, the service, the clinic's positioning — context no annotator has. So they judge what *sounds* helpful. Both humans and preference models systematically prefer agreeable responses over correct ones[^8] — and RLHF amplifies this bias as a first-order effect, not a side effect[^9]. More training makes it worse, not better.

Customer support succeeds when a patient books — or comes back. The reward model can't measure retention. It optimizes for pleasant. This isn't a bug — it's what the math guarantees.

## Wrong question

CS won't be automated away. It'll be shipped away.

Building is getting cheaper. Coding agents already ship features — a recurring CS ticket is now a prompt away from becoming a product fix. At some point, fixing the thing beats routing around it.

Products are already doing this. Onboarding that anticipates confusion prevents tickets from being filed. In-product assistants answer the FAQ before anyone reaches a human. Every feature that fixes a recurring problem removes a class of questions permanently.

Stripe is a clean example. "Why did my charge fail?" used to generate support tickets. Now the dashboard surfaces the reason directly — card declined, fraud flag, expired card — before anyone reaches a human. The ticket class disappeared. Not because a bot handled it. Because the product made the answer obvious.

As building gets cheaper, more ticket classes disappear the same way. The queue doesn't shrink because CS gets more efficient. It shrinks because there's less to handle.

[^1]: ["Anthropic acquires computer-use AI startup Vercept."](https://techcrunch.com/2026/02/25/anthropic-acquires-vercept-ai-startup-agents-computer-use-founders-investors/) TechCrunch, February 2026.
[^2]: ["Measuring AI Agent Autonomy."](https://www.anthropic.com/research/measuring-agent-autonomy) Anthropic, 2026.
[^3]: Gartner. ["Gartner Customer 360 Summit 2011: CRM Strategies and Technologies to Understand, Grow and Manage Customer Experiences."](https://www.gartner.com/imagesrv/summits/docs/na/customer-360/C360_2011_brochure_FINAL.pdf) Gartner, 2011.
[^4]: Moravec, H. [*Mind Children: The Future of Robot and Human Intelligence*](https://doi.org/10.2307/j.ctvbj7j1x). Harvard University Press, 1988.
[^5]: Schaal (2025) quantified Moravec's Paradox across 19,000 O*NET tasks: [arXiv:2510.13369](https://arxiv.org/abs/2510.13369). See also OpenAI, ["GDPval"](https://arxiv.org/abs/2510.04374) (arXiv:2510.04374, 2025) and ["Anthropic Economic Index, January 2026 Report."](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
[^6]: Autor. ["Polanyi's Paradox and the Shape of Employment Growth."](https://www.nber.org/papers/w20485) NBER Working Paper 20485, 2014.
[^7]: Lu (2025) found LLMs capture abstract and procedural tacit knowledge but not embodied knowledge. [Review of Austrian Economics](https://link.springer.com/article/10.1007/s11138-025-00710-5). Xu et al. (2025) tested 4,442 human concepts and found LLMs barely register sensory and motor features. [Nature Human Behaviour](https://www.nature.com/articles/s41562-025-02203-8).
[^8]: Perez et al. ["Towards Understanding Sycophancy in Language Models."](https://arxiv.org/abs/2310.13548) ICLR 2024.
[^9]: Shapira et al. ["How RLHF Amplifies Sycophancy."](https://arxiv.org/abs/2602.01002) arXiv:2602.01002, 2026. See also Casper et al. ["Open Problems and Fundamental Limitations of RLHF."](https://arxiv.org/abs/2307.15217) 2023.
