# MOTION SPEC

## Motion philosophy
Minimal motion - chỉ dùng khi motion mang meaning (feedback, state change)

Intensity: LOW

## Allowed motion
- Feedback: button press scale
- State transition: fade in/out (200ms)
- Streaming: text cursor blink
- Panel: slide in/out (300ms ease)

## Discouraged motion
- Scroll animations
- Hover scale/glow
- Decorative float
- Loading spinners (prefer skeleton)

## Timing defaults
- micro: 100ms (button feedback)
- hover: 150ms
- component: 200ms
- panel: 300ms ease-out

## Key product transitions
1. Debug panel expand/collapse: slide + fade
2. New message appear: fade in
3. Step change in pipeline: crossfade

## Reduced motion
Respect prefers-reduced-motion:
- Disable all animations
- Instant state changes
- Keep functional indicators (loading text, etc.)

## Performance constraints
- No JavaScript animation libraries
- CSS transitions only
- Max 60fps on all animations

## Library
Use existing:
- CSS transitions
- CSS animations (for skeleton shimmer)
- No external animation library
