# DRIVER Plugin

DRIVER is a methodology for AI-augmented product development. It guides you through six stages from concept to completion.

## Philosophy

**Cognition Mate (认知伙伴)** — 互帮互助，因缘合和，互相成就

- You bring: vision, domain expertise, judgment
- AI brings: patterns, research ability, heavy lifting on code
- Neither creates alone. Meaning emerges from interaction.

## The DRIVER Workflow

```
DEFINE (开题调研)
    ↓ "Want me to help create your roadmap?"
REPRESENT (Plan the unique part)
    ↓ "Want me to start building?"
IMPLEMENT (Show don't tell)
    ↓ "What needs to change?"
VALIDATE (See it running)
    ↓ "Ready to generate the export?"
EVOLVE (Final deliverable)
    ↓ "Want to capture what you learned?"
REFLECT (Optional learnings)
```

## Installation

### Local Development

```bash
# From the driver-plugin directory
/plugin marketplace add ./
/plugin install driver@driver-dev
```

Then add to `~/.claude/settings.json`:
```json
{
  "enabledPlugins": {
    "driver@driver-dev": true
  }
}
```

### From GitHub (when published)

```bash
/plugin marketplace add yourname/driver-marketplace
/plugin install driver@driver-marketplace
```

## Skills

| Skill | Stage | Purpose |
|-------|-------|---------|
| `/driver:using-driver` | Bootstrap | Establishes Cognition Mate relationship |
| `/driver:define` | DEFINE | Research and define product vision |
| `/driver:represent-roadmap` | REPRESENT | Break into buildable sections |
| `/driver:represent-datamodel` | REPRESENT | Define core entities |
| `/driver:represent-tokens` | REPRESENT | Choose colors and typography |
| `/driver:represent-shell` | REPRESENT | Design navigation shell |
| `/driver:represent-section` | REPRESENT | Spec a section |
| `/driver:implement-data` | IMPLEMENT | Create sample data |
| `/driver:implement-screen` | IMPLEMENT | Build and run code |
| `/driver:validate` | VALIDATE | Capture screenshots |
| `/driver:evolve` | EVOLVE | Generate export package |
| `/driver:reflect` | REFLECT | Capture learnings |

## Iron Laws

| Stage | Iron Law |
|-------|----------|
| DEFINE | NO BUILDING WITHOUT 分头研究 FIRST |
| REPRESENT | PLAN THE UNIQUE PART — DON'T REINVENT WHAT EXISTS |
| IMPLEMENT | SHOW DON'T TELL — BUILD AND RUN IT |
| VALIDATE | EVIDENCE BEFORE CLAIMS — SEE IT RUNNING |
| EVOLVE | FINAL DELIVERABLE — SELF-CONTAINED |
| REFLECT | CAPTURE TECH STACK LESSONS — ESPECIALLY FAILURES |

## For Quant/Finance Work

DRIVER recommends **Python + Streamlit** over TypeScript/React for analytical tools:

```
UI:          Streamlit (or Dash/Panel)
Backend:     FastAPI + Pydantic
Calculations: NumPy, Pandas, SciPy
```

Why: Python end-to-end, show-don't-tell (see results immediately), fewer bugs than TypeScript for financial calculations.

## License

MIT
