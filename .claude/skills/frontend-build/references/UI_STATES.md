# UI States

## Loading

Choose the state by duration/context:
- immediate button pending state,
- compact spinner for contained action,
- skeleton for stable content geometry,
- progressive rendering when partial data is useful.

Avoid full-page blocking spinners for small updates.

## Empty

An empty state should answer:
1. what is empty?
2. why might it be empty?
3. what can the user do next?

Do not use a giant illustration by default.

## Error

Show:
- what failed,
- whether existing data is still usable,
- recovery action,
- support/debug information only when appropriate.

## Disabled

Disabled UI should remain legible and explain prerequisites when not obvious.

## Selected / active

Use more than tiny color shifts when selection matters:
- border,
- surface,
- check,
- icon,
- text weight.

## Hover

Hover is enhancement, not the only way to reveal essential actions.

## Focus

Keyboard focus must be visible.

Do not remove outline without an accessible replacement.

## Pending / optimistic

Clearly distinguish:
- saved,
- saving,
- failed,
- retrying.

## Streaming / AI

For AI interfaces:
- show meaningful retrieval/generation progress,
- do not fake precision,
- make cancel/retry available when useful,
- keep partial output stable,
- preserve citations/provenance.
