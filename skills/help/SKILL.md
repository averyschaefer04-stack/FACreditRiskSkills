---
name: help
description: DRIVER overview, available skills, and philosophy explanation
---

# DRIVER Help

## What is DRIVER?

DRIVER is a methodology for building finance and quantitative analysis tools with AI assistance. It guides you from concept to completion through six stages.

---

## The Philosophy: Cognition Mate (认知伙伴)

**Core principle:** 互帮互助，因缘合和，互相成就

| Chinese | Pinyin | Meaning |
|---------|--------|---------|
| 互帮互助 | hù bāng hù zhù | Mutual help, helping each other |
| 因缘合和 | yīn yuán hé hé | Causes and conditions coming together (interdependent arising) |
| 互相成就 | hù xiāng chéng jiù | Accomplishing together, mutual achievement |

**What this means in practice:**
- AI is not a tool you command — it's a thinking partner
- You bring vision and domain expertise; AI brings patterns and research
- Neither creates alone — meaning emerges from interaction
- The relationship is collaborative, not transactional

---

## The Six Stages

```
┌─────────────────────────────────────────────────────────┐
│  DEFINE (开题调研)                                        │
│  "What are we building? What already exists?"            │
│  开题 = Open the topic  调研 = Research/investigate       │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  REPRESENT                                               │
│  "How do we break this into buildable pieces?"          │
│  Roadmap, data model, sections                          │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  IMPLEMENT                                               │
│  "Build it, run it, show it"                            │
│  Show don't tell — code speaks louder than plans        │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  VALIDATE                                                │
│  "Does it actually work?"                               │
│  Evidence before claims — see it running                │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  EVOLVE                                                  │
│  "Package the final deliverable"                        │
│  Self-contained export, ready for production            │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  REFLECT (Optional)                                      │
│  "What did we learn?"                                   │
│  Capture tech stack lessons, especially failures        │
└─────────────────────────────────────────────────────────┘
```

---

## Key Concepts

### 分头研究 (fēn tóu yán jiū)
**"Parallel research"** — Before building anything, research what exists. You focus on your unique needs; AI researches existing libraries, papers, implementations.

很可能已经有类似的了 = "There's probably something similar already"

### Show Don't Tell
Don't explain what you'll build. **Build it. Run it. Let them see it.**

The fastest feedback loop: See result → Give feedback → Iterate → See updated result

### KISS — Keep It Simple, Structured
- Simple and logical beats elegant and fancy
- Quants need clear data tables, not animations
- A 500-line Python script beats a 50-file TypeScript project

---

## Available Skills

| Skill | Stage | Purpose |
|-------|-------|---------|
| `/driver:init` | Setup | Initialize project structure |
| `/driver:status` | Any | Check progress, get suggestions |
| `/driver:help` | Any | This help page |
| `/driver:define` | DEFINE | Research and define vision |
| `/driver:represent-roadmap` | REPRESENT | Break into sections |
| `/driver:represent-datamodel` | REPRESENT | Define core entities |
| `/driver:represent-tokens` | REPRESENT | Colors/typography (web apps) |
| `/driver:represent-shell` | REPRESENT | Navigation shell (web apps) |
| `/driver:represent-section` | REPRESENT | Spec a section |
| `/driver:implement-data` | IMPLEMENT | Sample data (web apps) |
| `/driver:implement-screen` | IMPLEMENT | Build and run code |
| `/driver:validate` | VALIDATE | Capture screenshots |
| `/driver:evolve` | EVOLVE | Generate export package |
| `/driver:reflect` | REFLECT | Capture learnings |

---

## Recommended Stack for Finance/Quant

```
UI:           Streamlit (or Dash/Panel)
Backend:      FastAPI + Pydantic
Calculations: NumPy, Pandas, SciPy
Finance:      numpy-financial, QuantLib, yfinance, pandas-datareader
Data:         SQLite → PostgreSQL, Parquet files
Testing:      pytest + Hypothesis
```

**Why Python over TypeScript for quant work:**
- Vectorized calculations (NumPy) vs manual loops
- Pydantic catches validation errors at boundaries
- `streamlit run app.py` vs npm/webpack complexity
- Division by zero: `np.divide(..., where=b!=0)` vs manual guards everywhere

---

## Example Projects

| Project | Style | Key Libraries |
|---------|-------|---------------|
| DCF Valuation Tool | Damodaran | numpy-financial, yfinance |
| Portfolio Optimizer | Markowitz | PyPortfolioOpt, scipy.optimize |
| Factor Research | Open Source AP | pandas, statsmodels, alphalens |
| Risk Dashboard | VaR/CVaR | scipy.stats, matplotlib |
| Data Pipeline | ETL | pandas, SQLAlchemy, great_expectations |

---

## Getting Started

1. **New project:** `/driver:init` or just describe what you want to build
2. **Existing project:** `/driver:status` to see where you are
3. **Stuck?** Tell me the finance problem you're solving — we'll figure it out together

---

## Iron Laws (Never Break These)

| Stage | Iron Law |
|-------|----------|
| DEFINE | NO BUILDING WITHOUT 分头研究 FIRST |
| REPRESENT | PLAN THE UNIQUE PART — DON'T REINVENT |
| IMPLEMENT | SHOW DON'T TELL — BUILD AND RUN IT |
| VALIDATE | EVIDENCE BEFORE CLAIMS |
| EVOLVE | SELF-CONTAINED DELIVERABLE |
| REFLECT | CAPTURE WHAT DIDN'T WORK |
