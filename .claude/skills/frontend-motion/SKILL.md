---
name: frontend-motion
description: Add or refine purposeful frontend animation and micro-interactions after layout and visual hierarchy are stable. Use for React/Next or other web UIs that need state transitions, panel/dialog motion, list/layout continuity, button feedback, chat streaming polish, landing-page motion, or reduced-motion/performance cleanup. Do not use to animate every element or to compensate for weak static design.
---

# Frontend Motion

Act as a motion designer and frontend motion engineer.

Motion must explain:
- feedback,
- state,
- spatial relationship,
- continuity,
- attention.

It must not exist merely because animation is possible.

## Preconditions

Before adding motion:
1. inspect `.design/MOTION_SPEC.md` if present,
2. inspect existing animation library and conventions,
3. confirm layout/hierarchy are stable enough,
4. prefer the current stack.

If the screen still has major hierarchy/layout problems, recommend or perform `frontend-review` first.

## Select motion intensity

### Low
Best for:
- admin,
- finance,
- monitoring,
- enterprise operations.

Use:
- hover/press feedback,
- dialog/panel transitions,
- small status changes,
- layout continuity.

### Medium
Best for:
- SaaS,
- productivity,
- chat,
- RAG.

Add:
- list insertion/removal,
- panel transitions,
- contextual control reveal,
- smooth streaming/status changes.

### High
Best for:
- landing,
- product storytelling,
- creative showcase.

May include:
- section choreography,
- scroll-linked product storytelling,
- richer shared-layout transitions.

Even at high intensity, avoid constant decorative movement.

## Motion categories

Use [references/MOTION_SYSTEM.md](references/MOTION_SYSTEM.md) and [references/MOTION_RECIPES.md](references/MOTION_RECIPES.md).

### Feedback
Examples:
- button press,
- toggle,
- copy success,
- validation.

### State transition
Examples:
- loading -> content,
- collapsed -> expanded,
- tab change,
- filter applied.

### Spatial continuity
Examples:
- card -> detail,
- list item -> drawer,
- sidebar collapse,
- shared element.

### Attention
Examples:
- new notification,
- newly inserted message,
- critical status change.

Attention motion should be rare.

## Library choice

Prefer:
1. CSS transitions/animations for simple contained motion,
2. the project's existing motion library,
3. Motion for React when richer gestures/layout transitions are justified.

Do not add a motion dependency for a single opacity transition.

If Motion tooling / Motion AI Kit is available, use it for implementation guidance, not for deciding what should animate.

## Timing guidance

Use these as starting points, then tune visually:

```text
micro feedback:     80–160ms
hover/focus:        120–180ms
small reveal:       160–220ms
panel/dialog:       180–300ms
page/hero sequence: 300–700ms selectively
```

Fast operational products should feel faster than marketing pages.

Prefer natural easing/springs for spatial movement.

## Performance

Read [references/PERFORMANCE_REDUCED_MOTION.md](references/PERFORMANCE_REDUCED_MOTION.md).

Prefer animating:
- transform
- opacity

Be cautious with expensive layout/paint effects.

Avoid animation that causes jank in:
- long lists,
- message streams,
- tables,
- charts.

## Reduced motion

Every nonessential animation must have a reduced-motion fallback.

Reduced motion does not always mean no transition; it means avoid unnecessary spatial/vestibular movement.

## Review loop

After implementation:
1. run the UI,
2. interact with the animated state,
3. verify it does not slow task completion,
4. verify repeated use does not become annoying,
5. inspect mobile,
6. inspect reduced-motion behavior when possible.

## Completion criteria

Motion is complete when:
- every notable animation has a purpose,
- timings are coherent,
- repeated interactions remain fast,
- reduced motion is respected,
- no obvious jank is introduced,
- static design still looks good when motion is removed.
