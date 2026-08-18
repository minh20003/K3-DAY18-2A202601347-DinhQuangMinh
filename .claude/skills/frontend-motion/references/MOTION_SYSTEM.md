# Motion System

## Motion hierarchy

Not all motion deserves equal emphasis.

### Level 0 — instant
Use for:
- typing,
- direct manipulation feedback that must feel immediate,
- critical operational controls.

### Level 1 — micro
Use for:
- hover,
- press,
- toggle,
- icon state,
- selection.

### Level 2 — component
Use for:
- dropdown,
- tooltip,
- accordion,
- dialog,
- drawer,
- panel.

### Level 3 — layout
Use for:
- sidebar resize,
- list insertion,
- card/detail continuity,
- tab content where spatial context matters.

### Level 4 — narrative
Use selectively for:
- landing page hero,
- product walkthrough,
- feature storytelling.

Operational software should rarely use Level 4.

## Choreography

For multiple elements:
- animate groups, not every child,
- stagger only when it improves comprehension,
- keep stagger small,
- do not make users wait for sequential decoration.

## Entrance and exit

Entrances:
- subtle opacity + small transform when spatially appropriate.

Exits:
- usually slightly faster than entrance.

Do not animate large 30–60px travel distances for ordinary app UI.

## Hover

Hover should confirm interactivity.

Good:
- subtle surface change,
- border change,
- 1–2px optical elevation where appropriate.

Avoid:
- scale every card to 1.03,
- large shadow pop,
- spring wobble.

## Chat

Good motion:
- new message insertion,
- sending/pending -> sent,
- source/citation expansion,
- panel open/close,
- streaming status transition.

Avoid animating every token or making messages bounce.

## Dashboard

Good motion:
- filter/state updates,
- drill-down panel,
- chart transition when meaningful,
- expandable rows.

Avoid chart animation on every routine refresh.

## Landing

Motion can support:
- product reveal,
- sticky storytelling,
- controlled parallax,
- section transitions.

Keep text readable and interaction responsive.
