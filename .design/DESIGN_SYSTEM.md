# DESIGN SYSTEM

## Art direction
Personality:
- Professional nhưng không boring
- Tech-forward nhưng không overwhelming
- Clean, data-focused
- RAG pipeline visualization là hero feature

Density: Medium (phù hợp với chat + debug info)

Typography attitude: Precise, readable, monospace cho code/metrics

Surface strategy: Subtle surface hierarchy, dùng border thay vì shadow

Color strategy: Neutral + single accent (blue), semantic colors cho states

Motion intensity: LOW - chỉ essential feedback, streaming text

## Typography

| Token | Use | Size/line-height | Weight |
|-------|-----|-------------------|--------|
| display | Logo/title | 24px/32px | 600 |
| h1 | Section headers | 18px/28px | 600 |
| h2 | Subsection | 16px/24px | 500 |
| body | Chat messages | 15px/24px | 400 |
| small | Labels, metadata | 13px/20px | 400 |
| caption | Timestamps | 12px/16px | 400 |
| mono | Scores, code | 13px/20px | 400 |

Font stack: Inter (sans), JetBrains Mono (mono)

## Spacing scale
4 / 8 / 12 / 16 / 24 / 32 / 48

## Layout
- max content width: 1200px
- app shell: sidebar (280px) + main content
- page padding: 24px
- section rhythm: 24px gap
- grid behavior: flexible, collapse sidebar on mobile

## Colors

```css
--bg-base: #f8fafc;
--bg-surface: #ffffff;
--bg-elevated: #ffffff;
--bg-hover: #f1f5f9;
--text-primary: #0f172a;
--text-secondary: #475569;
--text-muted: #94a3b8;
--border: #e2e8f0;
--border-focus: #3b82f6;
--accent: #3b82f6;
--accent-hover: #2563eb;
--success: #22c55e;
--warning: #f59e0b;
--danger: #ef4444;
--info: #06b6d4;
```

## Radius
- controls: 6px
- surfaces: 8px
- modal: 12px
- pills: 9999px

## Borders/elevation
Rules:
- Dùng border 1px solid thay vì shadow cho normal sections
- Shadow chỉ cho elevated elements (dropdown, modal)
- Border-radius nhất quán theo radius scale

## Icons
Family: Lucide Icons (CDN)
Common sizes: 16px, 20px, 24px
Rules: Chỉ dùng khi cần reinforce action/recognition

## Imagery / illustration
Rules: Không có illustration, chỉ icons đơn giản

## Component visual rules

### Buttons
- primary: bg-accent, text-white, hover:bg-accent-hover
- secondary: bg-transparent, border, text-primary
- sizes: sm (32px), md (40px), lg (48px)

### Inputs
- height: 40px (md), 48px (lg)
- border: 1px solid border
- focus: ring 2px accent
- padding: 0 12px

### Cards
- bg-surface, border 1px, radius 8px
- padding: 16px
- Header + content pattern

### Chat bubbles
- user: bg-accent, text-white, right-aligned
- assistant: bg-surface, border, left-aligned
- max-width: 80%

### Debug panel
- Collapsible section
- Monospace font cho scores
- Color-coded scores (high=green, low=red)

### Tables/lists
- Striped rows
- Sticky header
- Compact padding

### Dialogs/drawers
- Backdrop blur
- Centered modal với shadow
- Escape to close

### Navigation
- Sidebar: fixed, 280px
- Logo at top
- Nav items với icons
- Active state: bg-hover + border-left accent

### Status
- Streaming: pulsing dot animation
- Loading: skeleton shimmer
- Error: danger bg + icon

## Anti-AI constraints
Explicit patterns this product should avoid:
- Gradient backgrounds
- Glass/blur effects
- Decorative AI sparkles
- Purple/blue gradient brand color
- Rounded-2xl on everything
- Card-inside-card patterns
- Generic "modern" styling

## Accessibility baseline
- visible focus: 2px accent ring
- labels: all inputs have labels
- contrast: AA compliant (4.5:1 minimum)
- touch targets: minimum 44px
- reduced motion: respect prefers-reduced-motion
