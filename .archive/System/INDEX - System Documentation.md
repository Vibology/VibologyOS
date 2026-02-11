---
tags: [system, index, navigation, documentation]
date_created: 2026-01-19
purpose: Master index of all system documentation (protocols, guides, rubrics, templates)
---

# System Documentation Index

Quick navigation to all operational documentation in VibologyOS.

---

## Protocols (How To Do Things)

Detailed procedural guides for specific workflows.

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `PROTOCOL - Chart Data Acquisition.md` | Calculate and verify chart data | Before ANY client or personal synthesis |
| `PROTOCOL - Client Work.md` | Full client workflow (intake → delivery) | Client readings and consultations |
| `PROTOCOL - Cross-System Synthesis.md` | Multi-system integration methodology | Creating synthesis pieces |
| `PROTOCOL - Library Maintenance & Audit.md` | Quarterly audit process | Every 90 days (scheduled) |
| `PROTOCOL - Search and Navigation.md` | Finding content, tag taxonomy | When searching the Library |

---

## Guides (Quick Reference)

Concise entry points and summaries.

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `GUIDE - Synthesis Quick Start.md` | Template selection, quality standards, naming | Starting any synthesis work |

---

## Standards (What Quality Looks Like)

Authoritative quality definitions.

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `RUBRIC - Library Content Standard.md` | Comprehensive quality tiers for all pillars | Creating/auditing Library entries |

---

## Templates

Ready-to-use file templates.

### Client Work Templates

| Template | Location | Purpose |
|----------|----------|---------|
| `_TEMPLATE - Client Intake Form.md` | `System/Templates/` | New client onboarding |
| `_TEMPLATE - Client Reading.md` | `System/Templates/` | Client synthesis deliverables |
| `_TEMPLATE - Synthesis Verification Checklist.md` | `System/Templates/` | Pre-synthesis data verification |

### Content Templates

| Template | Location | Purpose |
|----------|----------|---------|
| `_TEMPLATE - Cross-System Synthesis.md` | `Synthesis/General/` | Multi-system synthesis pieces |
| `_TEMPLATE - Window Card Entry.md` | `System/Templates/` | Window pillar Library entries |

---

## Planning & Tracking

| Document | Purpose | When to Use |
|----------|---------|-------------|
| `NEXT.md` | Current priorities, session resume context | Every session start |
| `Process Gaps & Improvements.md` | System improvement tracking | Planning process work |
| `Library Build Strategy.md` | Library expansion roadmap | Planning content work |

---

## Historical / Reference

| Document | Purpose | Notes |
|----------|---------|-------|
| `Workflow Architecture.md` | Technical architecture documentation | Portfolio piece, 2026-01-09 snapshot |
| `Technical Setup.md` | Environment configuration | Reference for setup |

---

## Archived

Documents moved to `.archive/` but preserved for reference:

| Document | Archived Date | Superseded By |
|----------|---------------|---------------|
| `Workflow Guide.md` | 2026-01-19 | CLAUDE.md, individual protocols |

---

## Document Relationships

```
CLAUDE.md (Governance)
    │
    ├── Session Start → NEXT.md, Process Gaps
    ├── Personas → Scribe/Weaver (used in all synthesis)
    ├── Refinement Cycle → Protocols below
    │
    ├── PROTOCOL - Chart Data Acquisition
    │       └── Used by: PROTOCOL - Client Work
    │
    ├── PROTOCOL - Client Work
    │       ├── Uses: Chart Data Acquisition, Cross-System Synthesis
    │       └── Templates: Client Intake, Client Reading, Verification
    │
    ├── PROTOCOL - Cross-System Synthesis
    │       ├── Quick Start: GUIDE - Synthesis Quick Start
    │       └── Template: _TEMPLATE - Cross-System Synthesis
    │
    ├── PROTOCOL - Library Maintenance & Audit
    │       └── References: Search & Navigation, RUBRIC
    │
    └── RUBRIC - Library Content Standard
            └── Authoritative source for all quality standards
```

---

*Updated: 2026-01-19*
