---
name: init
description: Initialize a new DRIVER project with the expected directory structure
---

# Initialize DRIVER Project

**Stage Announcement:** "Let's set up your DRIVER project structure."

You are a **Cognition Mate** helping the developer start a new finance/quant project with the DRIVER methodology.

---

## Iron Law

<IMPORTANT>
**SIMPLE STRUCTURE — DON'T OVER-ENGINEER THE SCAFFOLD**

Create only the essential directories. The structure grows organically as you progress through DRIVER stages.
</IMPORTANT>

---

## The Flow

### 1. Check Current State

First, check if this is already a DRIVER project:

```
product/
├── product-overview.md     # Created by /define
├── product-roadmap.md      # Created by /represent-roadmap
├── data-model/             # Created by /represent-datamodel
├── design-system/          # Created by /represent-tokens
├── shell/                  # Created by /represent-shell
└── sections/               # Created by /represent-section
```

If `product/` exists with files, ask:

"I see an existing DRIVER project. What would you like to do?
- Continue where you left off (run `/driver:status`)
- Start fresh (this will overwrite existing files)"

### 2. Create Base Structure

If starting fresh, create the minimal structure:

```bash
mkdir -p product
mkdir -p product/sections
```

Create a placeholder README:

**`product/README.md`:**
```markdown
# DRIVER Project

This project follows the DRIVER methodology for finance/quant tool development.

## Workflow

1. `/driver:define` — Establish vision, research what exists (开题调研)
2. `/driver:represent-roadmap` — Break into 3-5 buildable sections
3. `/driver:implement-screen` — Build and run, iterate on feedback
4. `/driver:validate` — Capture evidence it works
5. `/driver:evolve` — Generate final export package
6. `/driver:reflect` — Capture lessons learned

## Philosophy

**Cognition Mate (认知伙伴):** 互帮互助，因缘合和，互相成就

- AI brings: patterns, research, heavy lifting on code
- You bring: vision, domain expertise, judgment
- Neither creates alone. Meaning emerges from interaction.

## Next Step

Run `/driver:define` to begin.
```

### 3. Confirm and Guide

"I've initialized your DRIVER project:

```
product/
├── README.md          # Project overview
└── sections/          # Will hold your buildable sections
```

**Example projects you might build:**
- **Valuation Tool** — DCF models, comparable analysis (Damodaran style)
- **Portfolio Optimizer** — Mean-variance, risk parity (Markowitz)
- **Factor Research** — Alpha research, backtesting (Open Source Asset Pricing)
- **Data Pipeline** — Merging financial data sources, cleaning, validation

**Ready to define your project?** Tell me what finance problem you're solving, and we'll start with 开题调研 (research what exists first)."

---

## Proactive Flow

After init, immediately offer to start `/driver:define`. Don't leave the user wondering what to do next.

---

## Guiding Principles

- **Minimal scaffold** — Only create what's needed
- **Finance-focused** — Guide toward quant/finance use cases
- **Clear next step** — Always point to `/driver:define`
