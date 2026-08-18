# Responsive and Accessibility

## Responsive is interaction design

Desktop and mobile can use different interaction patterns.

Examples:

```text
desktop sidebar -> mobile drawer
wide filter row -> filter sheet
multi-column inspector -> stacked page or drawer
data table -> prioritized columns + detail sheet
hover actions -> visible/overflow tap actions
split chat/source -> toggleable panels
```

Do not hide important functionality just to fit the screen.

## Breakpoint strategy

Use the project's existing breakpoints.

Design around content pressure, not device names.

Test:
- narrow phone
- common laptop
- wide desktop when the product benefits from it

## Touch

Targets should be comfortably tappable.

Avoid tiny icon buttons packed with 4px gaps on mobile.

## Forms

- explicit labels where possible
- error text near field
- preserve entered data on validation error
- logical keyboard tab order
- correct input types/autocomplete where relevant

## Color and contrast

Critical status must not depend only on red/green.

Pair semantic color with:
- label,
- icon,
- shape,
- text.

## Zoom and text growth

Layouts should tolerate text expansion and browser zoom without clipping critical controls.

## Reduced motion

Any nonessential motion must respect user preference.

See the frontend-motion skill for implementation.
