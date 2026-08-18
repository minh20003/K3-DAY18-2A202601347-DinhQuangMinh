# Anti-AI UI Rules

These patterns are not forbidden. They are forbidden **by default without product justification**.

## Common AI-generated smells

### Decoration
- purple/blue gradient as the default brand
- random radial glow
- glassmorphism
- background blobs
- aurora mesh
- decorative grid background everywhere
- pointless noise texture
- shiny CTA treatment without brand reason

### Shape
- every container is a rounded card
- every tag is a pill
- excessive `rounded-2xl` / `rounded-3xl`
- giant detached cards floating in empty space
- identical radius on every object regardless of function

### Layout
- generic bento grid for unrelated information
- three identical feature cards because "three looks balanced"
- excessive centered alignment
- huge empty hero space
- sections that exist to fill a template rather than answer product questions
- card-inside-card-inside-card

### Typography
- giant 64–96px heading on ordinary app screens
- weak body contrast
- every section has eyebrow + heading + paragraph
- all labels are tiny uppercase tracking
- generic marketing copy instead of domain language

### Icons
- Lucide icon in a colored circle beside every feature
- icons used as decoration rather than recognition
- arbitrary icon variation across equivalent actions

### Motion
- every block fades upward on scroll
- every card scales on hover
- looping decorative float
- perpetual pulse
- spring animation on ordinary text
- delayed interface response merely to show animation

### Content
- "$12,345"
- "1,234 users"
- "John Doe"
- "Project Alpha"
- perfect +12.5% growth
- unrealistic short labels
- fake testimonials that shape the entire layout

## Better replacements

Instead of more decoration:
- improve typography,
- improve alignment,
- improve spacing rhythm,
- improve information ordering,
- improve content realism,
- improve responsive composition.

Instead of 6 cards:
- use one structured section,
- a table/list,
- inline statistics,
- grouped rows,
- a split panel.

Instead of "make it pop":
- establish a stronger primary action,
- improve contrast,
- reduce competing accents.

## Final AI-smell question

Before shipping, ask:

> If the logo and copy were removed, could this screenshot belong to 500 unrelated AI SaaS products?

If yes, increase product specificity.
