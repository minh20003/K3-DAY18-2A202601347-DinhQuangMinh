# Claude Code Project Guidelines — Frontend Workflow

This project includes local skills under `.claude/skills/`. Use them for all frontend and UI development tasks:

- `/frontend-bootstrap`: Product analysis, UX architecture, art direction, and generating the `.design/` blueprint.
- `/frontend-build`: Implementing UI components, screens, responsive layouts, and states from `.design/`.
- `/frontend-review`: Visual QA audit, detecting AI UI smells, ranking P0/P1/P2 issues, and applying fixes.
- `/frontend-motion`: Purposeful state transitions, micro-interactions, and accessibility-safe animations.

## Workflow & Execution Rules

1. **Default Mode**: For short labs, hackathons, and demos, default to **FAST LAB MODE** (build one representative primary screen to high polish, reuse existing primitives, focus on hierarchy & typography, skip overengineering).
2. **Execution Sequence**:
   ```text
   /frontend-bootstrap → /frontend-build → /frontend-review → /frontend-motion
   ```
3. **Inspect First**: Check existing code, `components.json` (if shadcn is present), dependencies, and product requirements before writing code.
4. **Anti-AI UI**: Avoid generic AI SaaS smells (purple/blue gradients, glassmorphism, cards everywhere, excessive rounding, scroll fade-ups, fake metrics).
5. **Visual Verification**: Use browser inspection tooling to visually verify rendered desktop and mobile viewports when available.
6. **Tool Fallback**: Utilize Motion or shadcn tools/MCPs if available, but degrade gracefully to standard project code if absent.
