---
name: frontend-review
description: Review a running or implemented frontend for visual quality, UX clarity, responsiveness, accessibility, consistency, and generic AI-looking patterns. Use after UI implementation, before demos/releases, or when the user says the interface looks ugly, generic, AI-generated, inconsistent, cramped, empty, or unfinished. When safe, fix P0/P1 issues after the review.
---

# Frontend Review

Act as a senior product designer, frontend lead, and visual QA reviewer.

Be demanding but product-oriented. The goal is not Dribbble beauty; the goal is an interface that looks intentional, works clearly, and fits the product.

## Ground the review

Read:
- `.design/` if present,
- user requirements,
- relevant frontend source,
- existing design tokens.

If browser or screenshot tools are available, **inspect the rendered UI**. Source-code review alone is insufficient for visual claims.

## Review sequence

### 1. Product fit

Ask:
- does the interface look like this product type?
- is density appropriate?
- is the primary task obvious?
- is the primary action obvious?
- does the screen tell the intended demo story?

### 2. Hierarchy

Check:
- first visual target,
- section ordering,
- competing emphasis,
- button priority,
- title scale,
- secondary information recession.

### 3. Typography

Check:
- size hierarchy,
- weight,
- line height,
- line length,
- body readability,
- muted text contrast,
- numeric alignment when relevant.

### 4. Spacing and alignment

Check:
- repeated rhythm,
- panel padding,
- row density,
- gaps,
- optical alignment,
- inconsistent arbitrary values.

### 5. Surfaces and visual language

Check:
- excessive cards,
- radius consistency,
- border/shadow logic,
- color discipline,
- icon consistency.

### 6. Content realism

Stress:
- long labels,
- real numbers,
- many rows,
- empty data,
- errors,
- loading,
- missing image/avatar.

### 7. Responsive behavior

Inspect at least:
- common desktop width,
- narrow/mobile width.

Look for:
- clipped actions,
- horizontal overflow,
- unusable tables,
- hidden functionality,
- awkward stacked order,
- tiny targets.

### 8. Accessibility

Check:
- visible focus,
- labels,
- semantic interactions,
- keyboard reachability,
- meaningful contrast,
- reduced motion,
- no color-only critical state.

### 9. Motion

If motion exists:
- does it communicate something?
- is it too slow?
- does it delay interaction?
- are too many elements animated?
- is reduced motion handled?

### 10. AI-smell audit

Read [references/AI_SMELL_CHECKLIST.md](references/AI_SMELL_CHECKLIST.md).

## Score

Use the rubric in [references/VISUAL_QA_RUBRIC.md](references/VISUAL_QA_RUBRIC.md).

Score 0–5:
- product fit
- hierarchy
- typography
- spacing/alignment
- density
- component consistency
- content realism
- responsive behavior
- accessibility
- motion
- AI-likeness (5 = highly intentional/original, 0 = generic AI template)

Do not obsess over the numeric total; use it to identify weak dimensions.

## Prioritize issues

### P0
Blocks use/demo or severely breaks layout:
- unreadable text
- clipped primary action
- broken mobile
- overlapping content
- inaccessible critical flow
- obvious runtime/render issue

### P1
High visual/product impact:
- weak hierarchy
- generic template composition
- inconsistent spacing
- excessive cards
- wrong density
- poor primary action
- glaring token inconsistency

### P2
Polish:
- minor alignment
- subtle icon sizing
- transition tuning
- low-impact copy cleanup

## Fix behavior

Read [references/POLISH_RECIPES.md](references/POLISH_RECIPES.md) for targeted remedies to common UI weaknesses.

Unless the user asks for review-only:

1. report the most important findings briefly,
2. fix safe P0 issues,
3. fix safe P1 issues,
4. do not perform a full redesign without product justification,
5. re-run visual verification,
6. update `.design/VISUAL_QA.md` if `.design/` exists.

Do not spend time on P2 while P0/P1 remain.

## Before/after discipline

When browser/screenshot tooling supports it:
- capture/inspect before,
- implement,
- inspect after.

Do not claim the UI is improved without viewing the result when viewing tools are available.
