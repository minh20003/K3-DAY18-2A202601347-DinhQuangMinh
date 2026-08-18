# Bootstrap Output Contract

Create `.design/` at the project root unless the repository has a documented alternative.

## PRODUCT_UI_BRIEF.md

Must contain:
- product summary
- target user
- primary job-to-be-done
- core workflows
- product archetype
- FAST LAB or STANDARD mode
- demo story
- assumptions
- explicit non-goals

## DESIGN_SYSTEM.md

Must contain:
- art direction
- personality words
- density
- typography scale
- spacing scale
- layout widths/grid
- color tokens
- border tokens
- radius tokens
- elevation/shadow
- icon rules
- image/illustration rules
- component visual rules
- anti-AI constraints
- accessibility baseline

Use actual token names/value guidance that can map to the project's styling system.

## UI_ARCHITECTURE.md

For each major screen:
- purpose
- primary user goal
- hierarchy
- sections
- primary action
- secondary actions
- navigation behavior
- responsive behavior
- loading/empty/error behavior
- important interactions

## COMPONENT_PLAN.md

Organize:
- existing primitives to reuse
- new primitives only if necessary
- composed reusable components
- domain/product components
- page sections
- state ownership
- implementation sequence

Mark the representative screen to build first.

## MOTION_SPEC.md

Must contain:
- motion philosophy
- intensity: low / medium / high
- allowed motion categories
- discouraged motion
- timing/spring defaults
- key transitions
- reduced-motion behavior
- performance constraints

Do not specify dozens of individual animations during bootstrap.

## Versioning

If `.design/` already exists:
- preserve decisions that still match the product,
- change only what the new task requires,
- add a short "Changes" section when the update is substantial.
