# COMPONENT PLAN

## Existing primitives to reuse
- None (new project)

## New primitives only if required
- Badge (for scores, status)
- Chip (for starter questions)
- ScoreBar (for metric visualization)
- StepIndicator (for pipeline steps)

## Reusable composed components
- Button (primary, secondary, sizes)
- Input (text, textarea)
- Card (surface with border)
- Tabs (for pipeline steps)

## Product/domain components
- ChatMessage (user, assistant variants)
- DebugPanel (chunks list, scores)
- ChunkCard (expandable, with metadata)
- ScoreDisplay (BM25, Dense, RRF, Rerank)
- MetricCard (RAGAS score)
- StarterQuestion (clickable chip)

## Page-level sections
- AppShell (sidebar + main)
- ChatPage
- PipelinePage
- MetricsPage

## Representative screen
Build first: ChatPage

Why: Đây là main interaction - demo RAG chat với citations và debug info

## State ownership
- Chat messages: local state (array)
- Pipeline steps: local state
- Metrics: fetched from API
- Debug panel visibility: local state (sidebar toggle)

## Implementation order
1. App shell + routing (HTML + CSS)
2. Chat page (messages + input)
3. Debug panel (chunks + scores)
4. Starter questions
5. Pipeline demo page
6. Metrics page
7. Mobile responsive

## Dependencies
- Flask (backend API)
- Lucide Icons (CDN)
- Inter + JetBrains Mono fonts (Google Fonts CDN)
- Tailwind CSS (CDN) - simpler cho demo

## Deferred / non-goals
- Streaming animation (can show partial text)
- Full offline support
- Dark mode
- Multi-language
