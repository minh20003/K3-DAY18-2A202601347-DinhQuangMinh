---
name: frontend-bootstrap
description: Analyze a new or existing frontend product and create a project-specific UI blueprint before major implementation. Use for new labs, dashboards, admin panels, chat/RAG apps, SaaS products, landing pages, homepages, redesigns, or any task where the frontend needs an intentional visual system. Do not use for tiny isolated CSS fixes when a design direction already exists.
---

# Frontend Bootstrap

Act as a senior product designer, UX architect, and frontend design-system architect.

Your job is **not** to produce a generic "modern UI". Your job is to derive a visual and interaction system from the actual product.

## Inputs

Inspect, in this order:

1. User request and assignment/brief.
2. Existing product docs: PRD, README, screenshots, wireframes, Figma/Stitch references if provided.
3. Existing frontend stack and component system.
4. Existing data shapes and important user workflows.
5. Existing visual conventions worth preserving.

Do not ask the user to repeat information that is already in the repo or prompt.

## Choose a mode

Use `FAST LAB` when:
- the user explicitly asks for a fast lab/hackathon/prototype,
- expected implementation time is short,
- polished demo quality matters more than exhaustive system design.

Otherwise use `STANDARD`.

### FAST LAB constraints

Prefer the smallest system that can still look intentional:

- 1 primary font family unless branding requires otherwise.
- 1 primary accent color plus semantic colors.
- 1 main navigation model.
- 8–15 meaningful reusable UI primitives/components.
- 2–3 notable motion moments at most before basic polish.
- one representative screen polished first.
- reuse current component primitives.
- avoid custom infrastructure unless it directly improves the demo.

Do not spend time inventing:
- particle systems,
- ornamental 3D,
- custom canvas effects,
- complex illustration systems,
- bespoke primitives that an existing library already solves.

## Workflow

### Step 1 — Understand the product

Write down internally:
- primary user,
- primary job-to-be-done,
- top 3–5 user tasks,
- core information objects,
- critical states,
- demo story.

If these cannot be inferred, make conservative assumptions and record them in `PRODUCT_UI_BRIEF.md`.

### Step 2 — Classify the product archetype

Read [references/PRODUCT_ARCHETYPES.md](references/PRODUCT_ARCHETYPES.md).

Choose one primary archetype and optional secondary archetype.

Examples:
- RAG assistant = Chat/Productivity
- operations portal = Admin/Dashboard
- AI product website = Landing/SaaS marketing
- marketplace home = Homepage/Discovery

Do not force all pages into the same density or composition merely because they are inside one product.

### Step 3 — Define art direction

Read:
- [references/DESIGN_PRINCIPLES.md](references/DESIGN_PRINCIPLES.md)
- [references/ANTI_AI_UI.md](references/ANTI_AI_UI.md)

Define:
- 4–6 personality words,
- visual density,
- typography attitude,
- surface treatment,
- color strategy,
- radius strategy,
- border/shadow strategy,
- imagery/illustration strategy if relevant,
- motion intensity,
- explicit anti-patterns for this product.

Do not use style labels like "modern", "beautiful", or "clean" without concrete implementation meaning.

### Step 4 — Create information architecture

For each major screen identify:
- user goal,
- primary content,
- primary action,
- secondary actions,
- navigation context,
- empty/loading/error states,
- mobile adaptation.

Prioritize scan order and task completion over decorative symmetry.

### Step 5 — Define the design tokens

Define practical tokens for:
- typography,
- spacing,
- layout widths,
- colors,
- borders,
- radii,
- shadows/elevation,
- icon sizing,
- motion defaults.

Prefer a small coherent scale.

Do not invent arbitrary one-off values unless the component has a real reason.

### Step 6 — Define component architecture

Separate:
- primitives,
- composed components,
- product/domain components,
- page-level sections.

Identify which existing components can be reused.

If `components.json` already exists in the project, reuse the existing shadcn configuration. If not, determine whether shadcn is actually appropriate for the stack before suggesting it. Do not force shadcn onto non-React or incompatible stacks.

If shadcn, Motion.dev, or browser MCPs are available, note their potential usage, but degrade gracefully to standard project dependencies and native capabilities if unavailable.

### Step 7 — Define content strategy

Read [references/CONTENT_AND_DATA.md](references/CONTENT_AND_DATA.md).

Specify realistic sample content and stress cases.

Never design only against:
- "John Doe",
- "$12,345",
- "Lorem ipsum",
- 3 perfectly balanced rows.

### Step 8 — Define motion intent

Create motion guidance only at system level:
- what deserves motion,
- what must remain instant,
- preferred intensity,
- reduced-motion behavior.

Detailed animation implementation belongs to `frontend-motion`.

### Step 9 — Write the project UI blueprint

Create or update:

```text
.design/
├── PRODUCT_UI_BRIEF.md
├── DESIGN_SYSTEM.md
├── UI_ARCHITECTURE.md
├── COMPONENT_PLAN.md
└── MOTION_SPEC.md
```

Use the structure in [references/OUTPUT_CONTRACT.md](references/OUTPUT_CONTRACT.md) and templates in [references/TEMPLATES.md](references/TEMPLATES.md).

## Existing projects

If a mature design system already exists:
- do not replace it,
- document it,
- fill only missing product-specific decisions,
- preserve brand tokens and established primitives.

If the user asks for a redesign:
- identify what is being preserved,
- identify what is changing,
- write the reasons,
- avoid gratuitous rewrites.

## Completion criteria

Bootstrap is complete only when:
- product archetype is explicit,
- visual direction is concrete,
- key screens and responsive behaviors are defined,
- component inventory exists,
- anti-AI constraints exist,
- motion intent exists,
- `.design/` can guide another agent without requiring it to re-invent the design.

Do not begin broad frontend implementation inside this skill unless the user explicitly asks to bootstrap and build in one run. If they do, complete the `.design/` contract first, then hand off conceptually to the `frontend-build` workflow.
