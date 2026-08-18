---
name: frontend-build
description: Implement or extend a polished frontend from the project's requirements and .design blueprint. Use for chat apps, RAG interfaces, dashboards, admin panels, landing pages, homepages, SaaS products, and other frontend implementation work where visual quality, responsiveness, states, and reusable components matter. Prefer this after frontend-bootstrap has created a design contract.
---

# Frontend Build

Act as a senior frontend engineer with strong product-design judgment.

The goal is to convert an intentional design contract into a working, polished frontend **without destroying the existing codebase**.

## Before coding

Inspect:
1. user request,
2. `.design/` files if present,
3. package/framework configuration,
4. current component library,
5. routing,
6. existing styles/tokens,
7. current API/data contracts.

If `.design/` is missing and this is a major/new frontend, use the `frontend-bootstrap` workflow first.

If `.design/` is missing but the task is a small isolated component, infer from the existing product instead of generating a whole new system.

## Preserve the stack

Do not replace:
- framework,
- styling solution,
- state management,
- component library,
- icon system,
- routing,
- data fetching

merely because another tool/library is fashionable.

Adopt a new dependency only when it clearly reduces risk/effort and fits the repo.

## Implementation sequence

### 1. Foundation

Map `.design/DESIGN_SYSTEM.md` to actual project tokens:
- CSS variables,
- Tailwind theme,
- theme object,
- component variants,
- typography utilities.

Avoid scattered magic values.

### 2. App shell

Build/verify:
- page container,
- navigation,
- sidebar/header,
- background/surface hierarchy,
- responsive shell.

Do not prematurely implement every feature.

### 3. Reusable primitives/compositions

Read [references/COMPONENT_RULES.md](references/COMPONENT_RULES.md).

Reuse existing library primitives.

Create product components only when repeated structure or domain meaning justifies them.

### 4. Representative screen

Build the representative screen identified in `.design/COMPONENT_PLAN.md`.

Polish it enough to establish:
- spacing rhythm,
- typography,
- density,
- control styling,
- state styling,
- responsive rules.

Do not expand to 8 pages while the first page still looks generic.

### 5. Expand consistently

Use the representative screen as the visual source of truth.

Reuse:
- token values,
- row heights,
- panel spacing,
- control variants,
- icon sizing,
- table/list patterns,
- empty-state grammar.

### 6. Implement real UI states

Read [references/UI_STATES.md](references/UI_STATES.md).

Implement relevant:
- loading,
- empty,
- error,
- disabled,
- selected,
- active,
- hover,
- focus,
- permission,
- stale/retry,
- optimistic/pending states.

A screenshot-only happy path is not complete frontend work.

### 7. Responsive composition

Read [references/RESPONSIVE_ACCESSIBILITY.md](references/RESPONSIVE_ACCESSIBILITY.md).

Do not merely collapse columns.

Adapt:
- navigation,
- tables,
- toolbars,
- side panels,
- dialogs/drawers,
- action placement,
- touch targets.

### 8. Accessibility

At minimum:
- semantic elements,
- labels,
- keyboard access,
- visible focus,
- adequate target sizes,
- useful alt text when images convey information,
- reduced-motion respect,
- no color-only critical meaning.

### 9. Visual verification

If browser tools are available:
1. run the app,
2. inspect the representative desktop screen,
3. inspect a narrow/mobile viewport,
4. test at least one interaction/state,
5. check runtime/console issues if tool supports it,
6. take screenshots if possible.

Fix obvious visual defects before declaring completion.

If browser tools are unavailable, explicitly note that final visual QA remains unverified.

## Anti-generic rules

Read [references/IMPLEMENTATION_ANTI_PATTERNS.md](references/IMPLEMENTATION_ANTI_PATTERNS.md).

Never "improve" a plain interface by automatically adding:
- gradient,
- glow,
- glass,
- huge rounding,
- extra cards,
- animations,
- fake metrics.

## Code quality rules

- keep components focused,
- keep domain meaning visible,
- avoid needless abstraction,
- avoid giant page components,
- prefer existing patterns,
- maintain type safety,
- preserve tests,
- do not hide broken data behind visual placeholders.

## FAST LAB behavior

In FAST LAB:
- prioritize visible critical path,
- prioritize the demo story,
- use existing primitives,
- avoid nonessential abstractions,
- still implement key empty/loading/error states,
- still verify responsive behavior,
- still perform one visual review loop.

FAST LAB means less scope, not lower craft.

## Completion criteria

The implementation is complete when:
- the core flow works,
- the representative visual language is consistent,
- the screen handles realistic content,
- responsive behavior is intentional,
- relevant states exist,
- accessibility basics are present,
- visual verification has been performed when tools allow it.
