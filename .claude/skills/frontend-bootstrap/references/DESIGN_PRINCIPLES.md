# Design Principles

## 1. Hierarchy before decoration

Every screen needs a deliberate scan order.

Ask:
1. What should the user notice first?
2. What should they understand second?
3. What is the primary action?
4. What can recede?

Do not give every card, heading, icon, and button the same visual weight.

## 2. Typography is interface architecture

Use type to communicate hierarchy, not merely to style text.

Prefer:
- fewer font sizes,
- consistent line heights,
- deliberate weight contrast,
- readable line length,
- restrained all-caps.

A product UI often needs stronger body and label typography than giant display headings.

## 3. Spacing should form rhythm

Use a repeatable spacing scale.

Good default family:

```text
4 / 8 / 12 / 16 / 24 / 32 / 48 / 64
```

Do not use random spacing values simply to "make it fit".

Dense products should reduce spacing systematically rather than inconsistently.

## 4. Density follows the job

Low density:
- storytelling,
- marketing,
- focused onboarding.

Medium density:
- SaaS,
- productivity,
- chat.

High density:
- admin,
- monitoring,
- finance,
- data operations.

Do not make operational software look like a marketing page.

## 5. Surfaces are not synonymous with cards

Use a card only when a region genuinely needs:
- grouping,
- elevation,
- independent interaction,
- a bounded state.

Otherwise prefer:
- section rhythm,
- dividers,
- typography,
- background shifts,
- alignment.

## 6. Color should establish meaning

Prefer:
- neutral surface system,
- one product accent,
- semantic success/warning/danger/info.

Avoid multiple accents fighting for attention.

## 7. Radius is a system

Choose a small radius family, e.g.:

```text
control: 6–8
surface: 8–12
modal: 12–16
pill: only when semantics are pill-like
```

Do not make every rectangle `rounded-2xl`.

## 8. Shadows are for elevation, not decoration

Prefer border and surface contrast for normal sections.

Use shadow when something is genuinely elevated:
- modal,
- popover,
- floating toolbar,
- sticky object over content.

## 9. Icons support recognition

Icons should:
- reinforce known actions,
- reduce scanning effort,
- not replace ambiguous text,
- use consistent size/stroke family.

Do not place decorative icons beside every heading.

## 10. Originality comes from product specificity

A UI feels designed when:
- its information hierarchy fits the task,
- the language fits the domain,
- the density fits the workflow,
- the components reflect real product objects.

Originality does not require decorative novelty.
