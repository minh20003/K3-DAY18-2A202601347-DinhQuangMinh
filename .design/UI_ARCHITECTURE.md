# UI ARCHITECTURE

## Navigation model

Primary navigation: Sidebar (fixed, 280px)
- Logo/App name at top
- 3 nav items: Chat, Pipeline Demo, Metrics
- Active state highlighted

Secondary/context navigation: Tab bar within pages

Mobile navigation: Hamburger menu → slide-in drawer

---

## Screen: Chat (Main)

### Purpose
Primary interaction - user asks HR questions, gets answers with citations

### Primary user goal
Get accurate HR policy answers with source transparency

### Scan hierarchy
1. Chat messages (main content)
2. Input composer (bottom)
3. Debug panel (collapsible, right)

### Sections
1. Header: App title + pipeline status indicator
2. Chat area: Scrollable message list
3. Input composer: Question input + submit button
4. Debug panel (right sidebar): Chunks, scores, timing

### Primary action
Submit question

### Secondary actions
Clear chat, Toggle debug panel, View metrics

### Interaction notes
- Enter to submit, Shift+Enter for newline
- Click chunk to expand
- Copy answer button

### Loading
Streaming text display với pulsing cursor

### Empty
Show starter questions as clickable chips

### Error
Inline error message với retry button

### Responsive behavior
Desktop: 3-column (nav + chat + debug)
Tablet: 2-column (chat + debug, nav collapsible)
Mobile: 1-column (chat only, debug in modal)

### Accessibility notes
- Alt text for any icons
- Keyboard navigation for messages

---

## Screen: Pipeline Demo

### Purpose
Visualize each step of RAG pipeline

### Primary user goal
Understand how RAG pipeline works step-by-step

### Scan hierarchy
1. Step indicator (1-5)
2. Current step visualization
3. Input/output of each step

### Sections
1. Step tabs: Enrich → Chunk → Search → Rerank → Answer
2. Visualization area
3. Step-by-step output

### Primary action
Navigate through steps

### Secondary actions
Run full pipeline, Reset

### Loading
Step-by-step loading animation

### Empty
Initial state with explanation

### Error
Step-level error display

### Responsive behavior
Vertical stack on mobile

---

## Screen: Metrics

### Purpose
Show RAGAS evaluation results

### Primary user goal
Understand pipeline quality metrics

### Scan hierarchy
1. Metric cards (4 scores)
2. Improvement comparison
3. Failure analysis list

### Sections
1. Score cards: Faithfulness, Answer Relevancy, Context Precision, Context Recall
2. Before/After comparison
3. Bottom-5 failures table

### Primary action
None (view only)

### Secondary actions
Refresh metrics, Export report

### Loading
Skeleton cards

### Empty
"No metrics yet" message

### Error
Retry button

### Responsive behavior
Cards stack on mobile
