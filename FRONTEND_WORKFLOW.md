# Frontend Agent Workflow Guide

This document defines the complete end-to-end frontend execution workflow for AI coding agents (OpenAI Codex, Claude Code, Google Antigravity).

---

## The Complete Pipeline

```text
NEW PROJECT / FEATURE BRIEF
           │
           ▼
   frontend-bootstrap
           │
           ▼
 .design/ UI Blueprint
 ├── PRODUCT_UI_BRIEF.md
 ├── DESIGN_SYSTEM.md
 ├── UI_ARCHITECTURE.md
 ├── COMPONENT_PLAN.md
 └── MOTION_SPEC.md
           │
           ▼
     frontend-build
           │
           ▼
    Run Application
           │
           ▼
   Browser Inspection
           │
           ▼
    frontend-review ──(Fix P0/P1)──┐
           │                        │
           ▼                        │
    frontend-motion                 │
           │                        │
           ▼                        │
       Final QA ◄──────────────────┘
           │
           ▼
      DEMO READY
```

---

## Execution Modes & Effort Levels

Select the appropriate mode based on time constraints and scope. Agents automatically adapt their effort according to the selected mode.

### 1. QUICK (1–3 Hour Lab / Assignment)

**Goal**: Deliver a working, clean demo with zero design overhead.

- **Bootstrap**: Generate a concise `.design/` contract focused on 1 core flow.
- **Build**: Implement 1 primary screen using existing primitives (or simple HTML/CSS/Tailwind). Focus strictly on typography, hierarchy, and basic spacing.
- **Review**: Quick visual sanity check (fix breaking issues / unreadable text).
- **Motion**: Minimal or instant (hover states only).

### 2. FAST LAB (Half-Day / 1-Day Project — DEFAULT)

**Goal**: Maximum perceived product quality per minute of implementation.

- **Bootstrap**: Analyze product archetype, user jobs, density, art direction. Write standard `.design/` blueprint.
- **Build**: Reuse existing component library or `shadcn` if compatible. Build 1 representative screen to high polish before expanding. Use domain-realistic data and implement key loading, empty, and error states.
- **Review**: Perform desktop and mobile browser visual QA. Rank issues P0/P1/P2 and fix P0/P1. Update `.design/VISUAL_QA.md`.
- **Motion**: Add restrained micro-interactions (button press, dialog open, streaming state, list insertion) without animating everything. Ensure `prefers-reduced-motion` is respected.

### 3. FULL (Production-Quality Frontend)

**Goal**: Complete multi-page, production-grade frontend with full design system and visual assurance.

- **Bootstrap**: Deep analysis of requirements, multiple screen architectures, design tokens, accessibility baseline, component inventory.
- **Build**: Systematically construct design tokens, app shell, reusable primitives, composed domain components, and full screen coverage with all UI states.
- **Review**: Comprehensive visual and UX audit across viewports and browsers, strict compliance with Anti-AI UI principles, fixing all P0/P1 issues.
- **Motion**: Complete motion choreography using Motion for React / CSS springs, complete reduced-motion fallbacks, performance audit.

---

## Phase Breakdown

| Phase | Responsible Skill | Key Output |
|---|---|---|
| 1. Product & UI Architecture | `frontend-bootstrap` | `.design/` blueprint files |
| 2. Senior Frontend Build | `frontend-build` | Clean, responsive UI code & states |
| 3. Visual & UX Audit | `frontend-review` | `.design/VISUAL_QA.md` & P0/P1 fixes |
| 4. Purposeful Motion | `frontend-motion` | Micro-interactions & transitions |
| 5. Demo Handover | Agent / User | Demo-ready application |
