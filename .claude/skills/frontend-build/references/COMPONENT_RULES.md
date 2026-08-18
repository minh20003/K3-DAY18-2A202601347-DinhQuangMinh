# Component Rules

## Primitive vs product component

Primitive:
- Button
- Input
- Dialog
- Popover
- Tabs
- Tooltip
- Checkbox
- Select

Composed component:
- SearchToolbar
- DataTable
- FilterBar
- EmptyState
- StatGroup

Product/domain component:
- MessageBubble
- CitationPanel
- TranslationToggle
- IncidentRow
- RoutePerformanceCard
- CustomerConversationHeader

Prefer domain components when they make product meaning explicit.

## Avoid component soup

Do not create a component for every 8 lines of JSX.

Extract when:
- reused,
- meaningful domain object,
- state isolation is useful,
- complexity deserves a boundary.

## Variants

Use component variants for real semantic differences:
- primary / secondary / destructive
- compact / normal
- status-specific

Do not create variants for arbitrary one-off page styling.

## Cards

Use a card if the content is independently grouped or elevated.

Do not wrap:
- every section,
- every KPI,
- every toolbar,
- every row

in separate cards without reason.

## Tables and lists

Operational data normally benefits from:
- stable column alignment,
- compact row rhythm,
- sticky headers when needed,
- inline status,
- contextual row actions.

Do not turn a dense table into giant cards on desktop simply because cards look "modern".

## shadcn or similar libraries

Use primitives for behavior/accessibility.

Then adapt:
- tokens,
- sizing,
- radius,
- borders,
- density,
- composition.

Do not treat default demo styling as final product design.
