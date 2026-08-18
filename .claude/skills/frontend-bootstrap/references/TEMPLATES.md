# Design Document Templates

Use these document structures when generating `.design/` files.

---

## PRODUCT_UI_BRIEF.md

```markdown
# PRODUCT UI BRIEF

## Mode
FAST LAB | STANDARD

## Product summary
What is being built and why?

## Target user
Who uses this interface?

## Primary job-to-be-done
What is the single most important job?

## Core workflows
1.
2.
3.

## Product archetype
Primary:
Secondary:

## Demo story
What should a reviewer/mentor understand in the first 1–3 minutes?

## Information objects
- 
- 

## Critical states
- loading
- empty
- error
- permission
- other:

## Assumptions
- 

## Non-goals
- 
```

---

## DESIGN_SYSTEM.md

```markdown
# DESIGN SYSTEM

## Art direction
Personality:
- 
- 
- 
- 

Density:
Typography attitude:
Surface strategy:
Color strategy:
Motion intensity:

## Typography

| Token | Use | Size/line-height | Weight |
|---|---|---:|---:|
| display | | | |
| h1 | | | |
| h2 | | | |
| h3 | | | |
| body | | | |
| small | | | |
| caption | | | |

## Spacing scale
Define the approved spacing family (e.g., 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64).

## Layout
- max content width:
- app shell:
- sidebar:
- page padding:
- section rhythm:
- grid behavior:

## Colors
- background:
- surface:
- elevated:
- text primary:
- text secondary:
- muted:
- border:
- accent:
- success:
- warning:
- danger:

## Radius
- controls:
- surfaces:
- modal:
- pills:

## Borders/elevation
Rules:

## Icons
Family:
Common sizes:
Rules:

## Imagery / illustration
Rules:

## Component visual rules
- buttons:
- inputs:
- cards:
- tables/lists:
- dialogs/drawers:
- navigation:
- status:

## Anti-AI constraints
Explicit patterns this product should avoid:
- 
- 

## Accessibility baseline
- visible focus
- labels
- contrast
- touch targets
- reduced motion
```

---

## UI_ARCHITECTURE.md

```markdown
# UI ARCHITECTURE

## Navigation model

Primary navigation:
Secondary/context navigation:
Mobile navigation:

---

## Screen: <name>

### Purpose

### Primary user goal

### Scan hierarchy
1.
2.
3.

### Sections
1.
2.
3.

### Primary action

### Secondary actions

### Interaction notes

### Loading

### Empty

### Error

### Responsive behavior

### Accessibility notes

---

Repeat for each major screen.
```

---

## COMPONENT_PLAN.md

```markdown
# COMPONENT PLAN

## Existing primitives to reuse
- 

## New primitives only if required
- 

## Reusable composed components
- 

## Product/domain components
- 

## Page-level sections
- 

## Representative screen
Build first:

Why:

## State ownership
Describe important local/server/shared state.

## Implementation order
1.
2.
3.
4.

## Dependencies
Only list new dependencies that are actually justified.

## Deferred / non-goals
- 
```

---

## MOTION_SPEC.md

```markdown
# MOTION SPEC

## Motion philosophy

Intensity:
LOW | MEDIUM | HIGH

## Allowed motion
- feedback
- state transition
- spatial continuity
- attention (rare)

## Discouraged motion
- 

## Timing defaults
- micro:
- hover:
- component:
- panel:
- narrative:

## Key product transitions
1.
2.
3.

## Reduced motion

## Performance constraints

## Library
Use existing:
CSS:
Motion:
Other:
```

---

## VISUAL_QA.md

```markdown
# VISUAL QA

Date:

Reviewed viewport(s):
- desktop:
- mobile:

## Scores (0–5)
- product fit:
- hierarchy:
- typography:
- spacing/alignment:
- density:
- component consistency:
- content realism:
- responsive:
- accessibility:
- motion:
- AI-likeness:

## P0
- 

## P1
- 

## P2
- 

## Fixes applied
- 

## Remaining limitations
- 

## Final verification
- [ ] core flow works
- [ ] desktop inspected
- [ ] mobile inspected
- [ ] loading/empty/error checked where relevant
- [ ] keyboard/focus basics checked
- [ ] motion checked
- [ ] no obvious generic AI patterns remain
```
