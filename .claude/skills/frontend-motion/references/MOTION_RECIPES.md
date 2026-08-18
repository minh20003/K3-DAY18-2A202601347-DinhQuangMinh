# Motion Recipes

These are behavioral recipes, not copy-paste values.

## Button press
Purpose: tactile feedback.

- on pointer down: tiny scale/compression or surface shift
- on release: quick return
- never delay click handling

## Dialog
Purpose: communicate elevation/focus.

- backdrop: quick opacity
- panel: short opacity + small scale/translate
- exit faster than entry
- return focus correctly

## Drawer / side panel
Purpose: preserve spatial origin.

- move from the edge it belongs to
- backdrop may fade
- content should become usable quickly

## Accordion
Purpose: communicate expansion.

- animate size if implementation is stable
- avoid sluggish long duration
- icon rotates only if it clarifies state

## List insertion
Purpose: show new item location.

- preserve surrounding layout
- small fade/translate or layout transition
- avoid bouncing whole list

## Toast
Purpose: acknowledge result.

- short entrance
- stable reading time
- exit without stealing focus

## Chat sending
Purpose: make state explicit.

```text
draft -> sending -> delivered
                 -> failed/retry
```

Use state styling first; motion is secondary.

## Landing hero
Purpose: establish narrative.

Prefer:
- 1 strong coordinated reveal
over:
- 15 independent fade-ups.

The product screenshot/demo should often carry more motion value than decorative headline effects.
