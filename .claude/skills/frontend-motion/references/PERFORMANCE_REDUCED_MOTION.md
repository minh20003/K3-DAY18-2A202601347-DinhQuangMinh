# Performance and Reduced Motion

## Performance

Prefer:
- transform
- opacity

Avoid frequent animation of:
- width/height across large trees,
- box-shadow blur,
- filter blur,
- huge backdrop-filter regions,
- top/left positioning,
- complex SVG paths unless justified.

For long lists:
- do not layout-animate hundreds of rows,
- animate the changed region only.

For streaming chat:
- keep token rendering stable,
- do not re-trigger container entrance animation on each chunk.

## Reduced motion

Respect `prefers-reduced-motion`.

Possible reduced alternatives:
- remove large translate/parallax,
- use opacity only,
- shorten durations,
- disable autoplay decorative loops,
- preserve instant state clarity.

Do not disable functional affordances:
- focus indication,
- loading status,
- selected state.

## Motion QA questions

- Does this move more than necessary?
- Does it happen too often?
- Would a user see it hundreds of times per day?
- Does it block input?
- Does it cause layout shift?
- Does it make mobile feel slower?
- Is the state still understandable with motion disabled?
