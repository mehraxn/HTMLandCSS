# Campus Stories — Complete CSS Documentation & README

**Project:** Campus Stories  
**Student:** MEHRAN  
**Assignment:** Introduction to Web Applications — Midterm HTML/CSS/Bootstrap Redesign  
**Tech Stack:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [File Structure](#file-structure)
3. [Pages Included](#pages-included)
4. [Technologies Used](#technologies-used)
5. [Complete CSS Explanation](#complete-css-explanation)
   - [The Universal Selector — `*`](#1-the-universal-selector--)
   - [Body — Global Base Styles](#2-body--global-base-styles)
   - [Links — `a`](#3-links--a)
   - [Navbar](#4-navbar)
   - [Brand Dot](#5-brand-dot)
   - [Nav Links](#6-nav-links)
   - [Hero Panel](#7-hero-panel)
   - [Hero Kicker](#8-hero-kicker)
   - [Hero Title](#9-hero-title)
   - [Hero Text & Actions](#10-hero-text--actions)
   - [Buttons — btn-main and btn-soft](#11-buttons--btn-main-and-btn-soft)
   - [Info Cards (Stats Strip)](#12-info-cards-stats-strip)
   - [Section Title & Text](#13-section-title--text)
   - [Filter Wrap & Filter Buttons](#14-filter-wrap--filter-buttons)
   - [Story Cards](#15-story-cards)
   - [Story Image (CSS Decorative Backgrounds)](#16-story-image-css-decorative-backgrounds)
   - [Image Color Variants](#17-image-color-variants)
   - [Category Badges](#18-category-badges)
   - [Card Title & Story Meta](#19-card-title--story-meta)
   - [Avatar (Small)](#20-avatar-small)
   - [Post Page Shell](#21-post-page-shell)
   - [Post Header Image](#22-post-header-image)
   - [Post Body, Quote Box, Action Bar](#23-post-body-quote-box-action-bar)
   - [Comment Card](#24-comment-card)
   - [Profile Panel & Avatar](#25-profile-panel--avatar)
   - [Profile Stat & Explore Search Panel](#26-profile-stat--explore-search-panel)
   - [Form Controls](#27-form-controls)
   - [Footer](#28-footer)
   - [Media Query — Responsive Mobile](#29-media-query--responsive-mobile)
   - [Real Photo Overrides](#30-real-photo-overrides)
6. [Color Palette Reference](#color-palette-reference)
7. [Design Inspiration](#design-inspiration)
8. [Responsive Design Notes](#responsive-design-notes)

---

## Project Overview

Campus Stories is a static front-end redesign of a student social-blog platform. Students can browse, post, and explore short stories about university life: study routines, projects, campus events, and everyday moments.

The visual design is inspired by the clean, card-based aesthetic of Google Workspace pages — light backgrounds, soft rounded cards, a clear color palette (blue, green, yellow), and readable spacing. No backend is implemented; all interactions are visual prototypes only.

---

## File Structure

```
campus stories/
├── index.html          ← Landing page / homepage
├── explore.html        ← Explore & search page
├── post.html           ← Individual post page
├── profile.html        ← Student profile page
├── README.md
└── static/
    ├── css/
    │   └── style.css   ← All custom CSS
    └── images/
        ├── campus-hero.png
        ├── first-day-vibes.png
        ├── library-vibes.png
        ├── all-nighter-stories.png
        ├── quiet-study-corner.png
        ├── tech-fest-2024.png
        ├── avatar-aj.png
        ├── avatar-maya.png
        └── sketch.jpg
```

---

## Pages Included

| File | Purpose |
|---|---|
| `index.html` | Homepage with hero section, stats strip, and story card grid |
| `explore.html` | Search panel + filter chips + story grid |
| `post.html` | Full individual blog post with comments |
| `profile.html` | Student profile with avatar, stats, and their posts |

---

## Technologies Used

- **HTML5** — semantic page structure
- **CSS3** — all custom styling, gradients, animations
- **Bootstrap 5** — grid system, responsive layout, base components
- **Bootstrap Icons** — icon font (stars, person, heart, etc.)

---

## Complete CSS Explanation

The file `static/css/style.css` is the **custom stylesheet** that sits on top of Bootstrap. Bootstrap handles the grid, spacing utilities, and basic components. This CSS file adds the visual personality: colors, rounded corners, gradients, hover effects, and custom components.

---

### 1. The Universal Selector — `*`

```css
* {
    box-sizing: border-box;
}
```

**What `*` means:**  
The asterisk `*` is the **universal selector** — it targets **every single element** on the entire page: `<div>`, `<p>`, `<img>`, `<nav>`, `<button>`, everything.

**What `box-sizing: border-box` does:**  
By default, CSS calculates the **size of a box** in a confusing way. If you write:

```css
div {
    width: 200px;
    padding: 20px;
    border: 5px solid black;
}
```

Without `border-box`, the actual rendered width would be **250px** (200 + 20 + 20 + 5 + 5), because padding and border are added *on top of* the width.

With `box-sizing: border-box`, the `width: 200px` **includes** the padding and border. The box stays at exactly 200px. This makes layouts far more predictable and is considered a modern best practice. Almost every professional CSS project starts with this rule.

**Why it's on `*`:**  
Putting it on `*` applies it universally so you never have to think about it again for any element.

---

### 2. Body — Global Base Styles

```css
body {
    margin: 0;
    background: rgb(248, 250, 253);
    color: rgb(32, 33, 36);
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
}
```

The `body` element wraps the entire visible page.

- **`margin: 0`** — Browsers add a small default margin around the body. This removes it so the page starts flush against the edges.
- **`background: rgb(248, 250, 253)`** — A very light, slightly blue-grey background. This is the same off-white tone Google uses in its interfaces. Pure white (`rgb(255,255,255)`) can feel harsh; this is softer.
- **`color: rgb(32, 33, 36)`** — A near-black color for all text. Using near-black instead of pure black (`rgb(0,0,0)`) reduces harshness and matches the Google design language.
- **`font-family: Arial, Helvetica, sans-serif`** — Sets the default font for all text. This is a **font stack**: if Arial is not available on the user's device, the browser falls back to Helvetica, and if that's missing, it falls back to any available sans-serif font.
- **`line-height: 1.6`** — Controls the space between lines of text. `1.6` means 1.6× the font size. This makes paragraphs easier to read than the default (~1.2). It is unitless, which means it scales with whatever `font-size` is used.

---

### 3. Links — `a`

```css
a {
    color: rgb(26, 115, 232);
}
```

Sets the default color of all hyperlinks (`<a>` tags) to Google's signature blue. Without this, links would be the browser's default purple or blue. This ensures all links match the site's color palette.

---

### 4. Navbar

```css
.navbar {
    background: rgba(255, 255, 255, 0.94);
    border-bottom: 1px solid rgb(218, 220, 224);
    backdrop-filter: blur(12px);
}
```

- **`background: rgba(255, 255, 255, 0.94)`** — White, but **94% opaque** (the `a` in `rgba` stands for *alpha*, which is the opacity channel, from 0 = invisible to 1 = solid). The 6% transparency allows a subtle blur effect to work on whatever is behind it.
- **`border-bottom: 1px solid rgb(218, 220, 224)`** — A thin light grey line under the navbar to visually separate it from the page content.
- **`backdrop-filter: blur(12px)`** — This is the **frosted glass effect**. It blurs everything *behind* the navbar. Because the background is slightly transparent (0.94), the blurred content behind bleeds through softly. This is the same technique used on iOS, macOS, and many modern web apps.

---

### 5. Brand Dot

```css
.navbar-brand {
    color: rgb(32, 33, 36) !important;
    font-weight: 700;
    letter-spacing: -0.03em;
}

.brand-dot {
    display: inline-block;
    width: 11px;
    height: 11px;
    margin-right: 7px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgb(26, 115, 232), rgb(52, 168, 83), rgb(251, 188, 4));
}
```

**`.navbar-brand`:**
- **`!important`** — Forces this color even if Bootstrap's own CSS would normally override it. `!important` gives a rule the highest priority in the cascade.
- **`font-weight: 700`** — Bold text. Font weights go from 100 (thin) to 900 (black). 700 is standard bold.
- **`letter-spacing: -0.03em`** — Tightens the space between letters slightly. Negative letter-spacing makes headings look more polished and compact. `em` is a relative unit — it scales with the font size.

**`.brand-dot`:**  
This is the small colored circle next to "Campus Stories" in the navbar.
- **`display: inline-block`** — By default, a `<span>` is inline and can't have a width/height. `inline-block` allows sizing while keeping it on the same line as text.
- **`width/height: 11px`** — Makes it a small square, then...
- **`border-radius: 50%`** — Turns any rectangle into a perfect circle (50% of each side).
- **`background: linear-gradient(135deg, ...)`** — A diagonal gradient using all three Google brand colors (blue → green → yellow) in one tiny dot. `135deg` means the gradient runs from top-left to bottom-right.

---

### 6. Nav Links

```css
.nav-link {
    color: rgb(95, 99, 104) !important;
    font-weight: 500;
}

.nav-link.active,
.nav-link:hover {
    color: rgb(26, 115, 232) !important;
}
```

- **`rgb(95, 99, 104)`** — A medium grey for inactive nav links. Less visually dominant than black.
- **`.nav-link.active`** — Targets a link that has both the class `nav-link` AND the class `active` at the same time. Bootstrap adds `active` to the current page's link.
- **`.nav-link:hover`** — The `:hover` pseudo-class applies styles when the user's mouse is over the element.
- Both active and hovered links turn Google blue (`rgb(26, 115, 232)`).

---

### 7. Hero Panel

```css
.hero-panel {
    margin-top: 32px;
    padding: 72px 28px;
    background:
        radial-gradient(circle at 10% 15%, rgba(26, 115, 232, 0.13), transparent 28%),
        radial-gradient(circle at 92% 18%, rgba(52, 168, 83, 0.13), transparent 25%),
        radial-gradient(circle at 50% 90%, rgba(251, 188, 4, 0.16), transparent 28%),
        rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 32px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
    overflow: hidden;
}
```

The hero panel is the large banner at the top of the homepage.

- **`padding: 72px 28px`** — Two-value shorthand: `72px` top/bottom, `28px` left/right. Gives the hero generous breathing room.
- **`background` with multiple `radial-gradient`s** — This is a multi-layer background. CSS allows stacking multiple backgrounds separated by commas. The topmost layer is listed first.
  - Each `radial-gradient(circle at X% Y%, color, transparent Zg%)` creates a soft circular glow at a specific position:
    - Blue glow in the top-left (10% from left, 15% from top)
    - Green glow in the top-right (92% from left, 18% from top)
    - Yellow glow at the bottom center (50%, 90%)
  - The last value `rgb(255, 255, 255)` is the solid white base behind all the gradients.
  - The colors use low `alpha` values (0.13, 0.16) so they are very faint and don't overwhelm the text.
- **`border-radius: 32px`** — Rounds all four corners by 32px, giving the panel its characteristic "card" look.
- **`box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12)`** — A very subtle shadow: `0` horizontal offset, `1px` vertical offset, `2px` blur radius. Makes the panel feel slightly lifted off the page.
- **`overflow: hidden`** — Clips any child content that extends beyond the rounded corners, so the corners stay clean.

---

### 8. Hero Kicker

```css
.hero-kicker {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    margin-bottom: 20px;
    color: rgb(26, 115, 232);
    background: rgb(232, 240, 254);
    border-radius: 999px;
    font-size: 0.9rem;
    font-weight: 700;
}
```

The kicker is the small "⭐ Student stories from around campus" pill above the main title.

- **`display: inline-flex`** — Makes the element a flex container but keeps it inline (like a word, not a full block). `flex` allows using `align-items` and `gap`.
- **`align-items: center`** — Vertically centers the icon and text inside the pill.
- **`gap: 8px`** — Adds 8px of space between the icon and the text (a modern, clean way to space flex children).
- **`border-radius: 999px`** — A very large radius turns any rectangle into a **pill shape**. Using `999px` is a common trick: the radius is so large it will always exceed half the element's height, so it always becomes fully rounded regardless of the pill's size.
- **`background: rgb(232, 240, 254)`** — A light blue tint matching the Google blue family.

---

### 9. Hero Title

```css
.hero-title {
    max-width: 900px;
    margin: 0 auto;
    font-size: clamp(2.6rem, 8vw, 5.6rem);
    line-height: 0.98;
    font-weight: 700;
    letter-spacing: -0.065em;
}
```

- **`max-width: 900px`** — The title won't stretch wider than 900px even on very large screens.
- **`margin: 0 auto`** — `0` top/bottom margin, `auto` left/right. When `auto` is used on both sides, the browser splits the remaining space equally, centering the element horizontally.
- **`font-size: clamp(2.6rem, 8vw, 5.6rem)`** — This is **fluid typography**. `clamp(min, preferred, max)`:
  - Minimum: `2.6rem` — never smaller than this (on very small screens)
  - Preferred: `8vw` — tries to be 8% of the viewport width (scales with the window)
  - Maximum: `5.6rem` — never larger than this (on very large screens)
  - `rem` = relative to the root font size (usually 16px, so `2.6rem` ≈ 42px). `vw` = viewport width.
- **`line-height: 0.98`** — Less than 1, meaning lines are tighter than the font's natural height. This is common for very large display headings to look dense and impactful.
- **`letter-spacing: -0.065em`** — Fairly aggressive letter tightening. Large titles often need this to look designed rather than spaced-out.

---

### 10. Hero Text & Actions

```css
.hero-text {
    max-width: 720px;
    margin: 24px auto 0;
    color: rgb(95, 99, 104);
    font-size: 1.18rem;
}

.hero-actions {
    margin-top: 32px;
}
```

- **`margin: 24px auto 0`** — Three-value shorthand: `24px` top, `auto` left/right (centers it), `0` bottom.
- **`color: rgb(95, 99, 104)`** — Grey, secondary text color, less dominant than the title.
- **`font-size: 1.18rem`** — Slightly larger than default (1rem = 16px) for readability as a subtitle.

---

### 11. Buttons — btn-main and btn-soft

```css
.btn-main {
    background: rgb(26, 115, 232);
    border: 1px solid rgb(26, 115, 232);
    color: rgb(255, 255, 255);
    border-radius: 999px;
    padding: 12px 22px;
    font-weight: 700;
}

.btn-main:hover {
    background: rgb(21, 88, 176);
    border-color: rgb(21, 88, 176);
    color: rgb(255, 255, 255);
}

.btn-soft {
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    color: rgb(32, 33, 36);
    border-radius: 999px;
    padding: 12px 22px;
    font-weight: 700;
}

.btn-soft:hover {
    border-color: rgb(26, 115, 232);
    color: rgb(26, 115, 232);
}
```

Two button styles:
- **`btn-main`** — Filled blue button (primary action).
- **`btn-soft`** — White outlined button (secondary action).

Both use `border-radius: 999px` for the pill shape.

**Hover states** (`:hover` pseudo-class):
- `btn-main:hover` — darkens the blue slightly (`rgb(21, 88, 176)` is a darker blue than `rgb(26, 115, 232)`). This gives the user feedback that the button is interactive.
- `btn-soft:hover` — changes the border and text to blue without filling, creating a subtle highlight.

---

### 12. Info Cards (Stats Strip)

```css
.info-card {
    height: 100%;
    padding: 24px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 24px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
}

.info-number {
    color: rgb(26, 115, 232);
    font-size: 2.2rem;
    font-weight: 700;
    letter-spacing: -0.05em;
}
```

- **`height: 100%`** — The card stretches to fill the full height of its parent container. When Bootstrap columns in the same row have different content heights, this ensures all cards reach the same height.
- **`border-radius: 24px`** — Rounded corners, slightly less than the hero (32px), making it feel like a sub-element.

---

### 13. Section Title & Text

```css
.section-title {
    font-size: clamp(2rem, 4vw, 3.6rem);
    line-height: 1.05;
    font-weight: 700;
    letter-spacing: -0.05em;
}

.section-text {
    color: rgb(95, 99, 104);
    max-width: 680px;
}
```

Same fluid `clamp()` technique as the hero title, but for section headings. Smaller range (2rem–3.6rem vs the hero's 2.6rem–5.6rem).

---

### 14. Filter Wrap & Filter Buttons

```css
.filter-wrap {
    padding: 18px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 24px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
}

.filter-btn,
.badge.filter-btn {
    display: inline-flex;
    align-items: center;
    min-height: 40px;
    padding: 9px 17px;
    margin: 4px;
    color: rgb(32, 33, 36);
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 999px;
    font-size: 0.94rem;
    font-weight: 600;
    text-decoration: none;
    transition: 0.2s ease;
}

.filter-btn:hover,
.filter-btn.active,
.badge.filter-btn.active {
    color: rgb(255, 255, 255);
    background: rgb(26, 115, 232);
    border-color: rgb(26, 115, 232);
}
```

Filter chips are the category pills like "All", "Study Tips", "Events", etc.

- **`.filter-btn, .badge.filter-btn`** — A comma separates multiple selectors. Both `.filter-btn` and any element with both `badge` and `filter-btn` classes will get the same styles. This is necessary because some chips in the HTML use Bootstrap's `badge` class in addition to `filter-btn`.
- **`min-height: 40px`** — Sets a minimum height. The chip will grow taller if text wraps, but never shorter than 40px. This keeps touch targets large enough on mobile.
- **`text-decoration: none`** — Removes the underline from links styled as chips.
- **`transition: 0.2s ease`** — When any property changes (e.g., on hover), the change animates smoothly over 0.2 seconds. `ease` means it starts fast and decelerates. Without this, hover changes would be instant and jarring.

---

### 15. Story Cards

```css
.story-card {
    height: 100%;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 28px;
    overflow: hidden;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
    transition: 0.22s ease;
}

.story-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(60, 64, 67, 0.12);
}
```

- **`transition: 0.22s ease`** — Prepares the card for smooth animation on hover.
- **`transform: translateY(-4px)`** — On hover, moves the card **4px upward**. `translateY` moves along the vertical axis; negative = up. This creates a "lift" effect.
- **`box-shadow` on hover** — The shadow grows from a subtle `1px 2px` to a more pronounced `8px 24px`, reinforcing the lifting effect visually.

---

### 16. Story Image (CSS Decorative Backgrounds)

```css
.story-image {
    min-height: 190px;
    background: linear-gradient(135deg, rgb(232, 240, 254), rgb(255, 255, 255) 55%, rgb(230, 244, 234));
    border-bottom: 1px solid rgb(218, 220, 224);
    position: relative;
    overflow: hidden;
}

.story-image::before,
.story-image::after {
    content: "";
    position: absolute;
    border-radius: 50%;
    opacity: 0.9;
}

.story-image::before {
    width: 105px;
    height: 105px;
    right: 22px;
    top: 22px;
    background: rgb(254, 247, 224);
}

.story-image::after {
    width: 150px;
    height: 150px;
    left: -40px;
    bottom: -55px;
    background: rgba(26, 115, 232, 0.16);
}
```

This section creates the decorative placeholder card header (used when there is no real photo).

- **`position: relative`** — Makes `.story-image` a **positioning context**. This is required so that absolutely-positioned pseudo-elements (`::before` and `::after`) are placed relative to this element, not the whole page.
- **`::before` and `::after`** — These are **CSS pseudo-elements**. They insert virtual elements that don't exist in the HTML but can be styled and positioned. Together they create two decorative circles inside the image area.
- **`content: ""`** — Required for pseudo-elements to appear. An empty string means no text, just the visual box.
- **`position: absolute`** — The circles are positioned relative to `.story-image`. `right: 22px; top: 22px` places the first circle 22px from the top-right corner. `left: -40px; bottom: -55px` partially hides the second circle outside the bottom-left edge, making it feel like an abstract decorative accent.
- **`overflow: hidden`** on `.story-image` — Clips the protruding parts of the second circle so it doesn't escape outside the card.

---

### 17. Image Color Variants

```css
.image-blue  { background: linear-gradient(135deg, rgb(232, 240, 254), rgb(255, 255, 255) 55%, rgb(210, 227, 252)); }
.image-green { background: linear-gradient(135deg, rgb(230, 244, 234), rgb(255, 255, 255) 55%, rgb(206, 234, 214)); }
.image-yellow{ background: linear-gradient(135deg, rgb(254, 247, 224), rgb(255, 255, 255) 55%, rgb(254, 239, 195)); }
.image-red   { background: linear-gradient(135deg, rgb(252, 232, 230), rgb(255, 255, 255) 55%, rgb(250, 210, 207)); }
```

Four color theme variants for story card headers when no real image is used. Each is a diagonal gradient from a light tint of a color, through near-white in the middle, to a slightly deeper tint on the other side. Adding one of these classes to `.story-image` changes its color theme.

---

### 18. Category Badges

```css
.category-badge {
    display: inline-flex;
    align-items: center;
    padding: 6px 10px;
    margin-bottom: 14px;
    color: rgb(26, 115, 232);
    background: rgb(232, 240, 254);
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 700;
}

.category-green  { color: rgb(19, 115, 51);  background: rgb(230, 244, 234); }
.category-yellow { color: rgb(176, 96, 0);   background: rgb(254, 247, 224); }
.category-red    { color: rgb(197, 34, 31);  background: rgb(252, 232, 230); }
```

Small colored labels on story cards (e.g., "Study Tips", "Events"). Default is blue. Adding `.category-green`, `.category-yellow`, or `.category-red` overrides the color. This is the **modifier pattern** — one base class defines the structure, modifier classes change the color theme.

---

### 19. Card Title & Story Meta

```css
.card-title {
    letter-spacing: -0.025em;
}

.story-meta {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding-top: 18px;
    margin-top: 18px;
    border-top: 1px solid rgb(218, 220, 224);
    color: rgb(95, 99, 104);
    font-size: 0.88rem;
}
```

- **`display: flex`** on `.story-meta` — The meta row (author name + date/read time) becomes a flex container.
- **`justify-content: space-between`** — Pushes the two items (author and date) to opposite ends of the row. This is one of the most useful flex properties for header/footer layouts.
- **`gap: 12px`** — Space between the flex children.
- **`border-top`** — A thin divider line separating the card body from the meta row.

---

### 20. Avatar (Small)

```css
.avatar-sm {
    width: 36px;
    height: 36px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: rgb(255, 255, 255);
    background: rgb(26, 115, 232);
    border-radius: 50%;
    font-weight: 700;
}
```

A small circular avatar that shows the user's initials (e.g., "M" for MEHRAN). `border-radius: 50%` makes the square into a circle. `align-items: center` + `justify-content: center` on an `inline-flex` container perfectly centers the letter inside the circle both vertically and horizontally.

---

### 21. Post Page Shell

```css
.post-shell {
    max-width: 960px;
    margin: 32px auto;
    padding: 24px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 32px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
}
```

The white "card" that wraps the entire post page content.

- **`max-width: 960px`** — Keeps the post readable on large screens. Very wide text lines are hard to read.
- **`margin: 32px auto`** — Centers the shell horizontally with 32px top/bottom margin.

---

### 22. Post Header Image

```css
.post-header-img {
    width: 100%;
    min-height: 360px;
    border: 1px solid rgb(218, 220, 224);
    border-radius: 28px;
    background: linear-gradient(135deg, rgb(232, 240, 254), rgb(255, 255, 255) 45%, rgb(230, 244, 234));
    position: relative;
    overflow: hidden;
}

.post-header-img::before {
    content: "";
    position: absolute;
    width: 190px;
    height: 190px;
    right: 9%;
    top: 18%;
    background: rgb(254, 247, 224);
    border-radius: 50%;
}

.post-header-img::after {
    content: "Campus study corner";
    position: absolute;
    left: 32px;
    bottom: 28px;
    color: rgb(95, 99, 104);
    font-weight: 700;
}
```

The decorative header image at the top of the post page (when no real photo is used). Uses the same `::before` / `::after` pseudo-element technique as the story cards, but larger. The `::after` here has actual `content: "Campus study corner"` — it displays a caption text in the bottom-left corner using absolute positioning.

---

### 23. Post Body, Quote Box, Action Bar

```css
.post-body {
    color: rgb(60, 64, 67);
}

.quote-box {
    padding: 24px;
    background: rgb(232, 240, 254);
    border-left: 5px solid rgb(26, 115, 232);
    border-radius: 18px;
    color: rgb(32, 33, 36);
    font-weight: 600;
}

.action-bar {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    padding: 16px 0;
    border-top: 1px solid rgb(218, 220, 224);
    border-bottom: 1px solid rgb(218, 220, 224);
}

.action-pill {
    padding: 9px 14px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 999px;
    font-weight: 600;
}
```

- **`quote-box`** — A styled blockquote. The `border-left: 5px solid` creates the classic "thick left accent line" quote style. Combined with the blue background it creates a visually distinct callout.
- **`action-bar`** — A row of action buttons (Like, Share, Bookmark). `flex-wrap: wrap` allows the buttons to wrap onto a second line on small screens instead of overflowing.
- **`action-pill`** — Individual pill-shaped action buttons inside the bar.

---

### 24. Comment Card

```css
.comment-card {
    padding: 18px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 20px;
}
```

A simple white rounded box for each comment. No shadow here — less visual hierarchy than story cards, indicating it's a sub-element.

---

### 25. Profile Panel & Avatar

```css
.profile-panel {
    padding: 30px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 32px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
}

.profile-avatar {
    width: 128px;
    height: 128px;
    border: 5px solid rgb(255, 255, 255);
    border-radius: 50%;
    background: linear-gradient(135deg, rgb(26, 115, 232), rgb(52, 168, 83));
    box-shadow: 0 8px 24px rgba(60, 64, 67, 0.12);
    color: rgb(255, 255, 255);
    font-size: 2.4rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
```

- **`profile-avatar`** — A large circle (128×128px) with a blue-to-green gradient background showing the user's initials. The `border: 5px solid rgb(255,255,255)` is a white ring around the avatar — a classic profile picture style detail. The larger `box-shadow` gives it depth.

---

### 26. Profile Stat & Explore Search Panel

```css
.profile-stat {
    padding: 14px;
    background: rgb(248, 250, 253);
    border-radius: 18px;
}

.search-panel {
    padding: 24px;
    background: rgb(255, 255, 255);
    border: 1px solid rgb(218, 220, 224);
    border-radius: 28px;
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.12);
}
```

- **`profile-stat`** — A small rounded box for stat numbers (Posts: 12, Followers: 340, etc.). Uses the body background color (`rgb(248, 250, 253)`) rather than white, giving it a slightly recessed look.
- **`search-panel`** — The white card wrapping the search input and filter chips on the Explore page.

---

### 27. Form Controls

```css
.form-control {
    border-color: rgb(218, 220, 224);
}

.form-control:focus {
    border-color: rgb(26, 115, 232);
    box-shadow: 0 0 0 0.2rem rgba(26, 115, 232, 0.14);
}
```

Overrides Bootstrap's default form styling.

- **`.form-control`** — Sets the default border to the site's light grey.
- **`.form-control:focus`** — `:focus` is a pseudo-class that activates when the user clicks inside or tabs to an input. Changes the border to blue and adds a `box-shadow` "glow ring" around the input. The shadow uses `0 0 0 0.2rem` (no offset, no blur, just spread) — this technique creates a perfect uniform outline glow without any directional shadow. The `rgba(..., 0.14)` makes it semi-transparent and subtle.

---

### 28. Footer

```css
.footer-box {
    margin-top: 70px;
    padding: 34px 0;
    background: rgb(255, 255, 255);
    border-top: 1px solid rgb(218, 220, 224);
    color: rgb(95, 99, 104);
}
```

A white footer separated from the page body by a thin top border. `margin-top: 70px` gives significant breathing room between the last section and the footer.

---

### 29. Media Query — Responsive Mobile

```css
@media (max-width: 768px) {
    .hero-panel {
        margin-top: 16px;
        padding: 48px 20px;
        border-radius: 24px;
    }

    .hero-title {
        font-size: 2.8rem;
    }

    .filter-wrap {
        border-radius: 20px;
        overflow-x: auto;
        white-space: nowrap;
        flex-wrap: nowrap !important;
    }

    .post-shell,
    .profile-panel,
    .search-panel {
        border-radius: 24px;
        padding: 20px;
    }

    .post-header-img {
        min-height: 240px;
    }
}
```

`@media (max-width: 768px)` is a **media query** — a conditional CSS block that only applies when the viewport (browser window) width is 768px or less (i.e., on tablets and phones).

Inside the media query, existing classes are overridden with smaller/adjusted values:

- **Hero panel** — less top margin, less padding, slightly less rounded corners. Saves vertical space on small screens.
- **Hero title** — locked to `2.8rem` instead of the fluid `clamp()` value, ensuring it doesn't get too large on mid-sized mobile screens.
- **Filter wrap** — `overflow-x: auto` allows horizontal scrolling. `white-space: nowrap` prevents chips from wrapping. `flex-wrap: nowrap !important` (the `!important` overrides Bootstrap utility classes) keeps all chips on one line so the row can be scrolled horizontally rather than pushing content down.
- **Post/profile/search panels** — smaller padding and border-radius to use screen space efficiently.
- **Post header image** — reduced minimum height since mobile screens are shorter.

---

### 30. Real Photo Overrides

```css
.story-photo {
    width: 100%;
    height: 190px;
    object-fit: cover;
    display: block;
    border-bottom: 1px solid rgb(218, 220, 224);
}

.post-header-img {
    width: 100%;
    height: 420px;
    min-height: 0;
    object-fit: cover;
    display: block;
    border: 1px solid rgb(218, 220, 224);
    border-radius: 28px;
    background: rgb(248, 250, 253);
}

.post-header-img::before,
.post-header-img::after {
    display: none;
}

.profile-avatar-img {
    width: 128px;
    height: 128px;
    object-fit: cover;
    border: 5px solid rgb(255, 255, 255);
    border-radius: 50%;
    box-shadow: 0 8px 24px rgba(60, 64, 67, 0.12);
}
```

These rules apply to `<img>` elements when real photos are used.

- **`object-fit: cover`** — The most important property for images in fixed-size containers. It scales the image so it **fills the container completely** while maintaining its aspect ratio — cropping the overflow instead of distorting it. Without this, images would stretch or squish to fit. `cover` ensures the image always fills its box cleanly.
- **`display: block`** — Images are inline by default, which can add a small gap below them. `block` removes this gap.
- **`.post-header-img::before, .post-header-img::after { display: none; }`** — Disables the decorative CSS pseudo-elements (circles and caption text) when a real image is present. Real photos don't need the CSS placeholder decorations.
- **`profile-avatar-img`** — Applied to `<img>` profile photos. Same circle technique as `.profile-avatar`, but for a real photo using `border-radius: 50%` + `object-fit: cover`.

---

## Color Palette Reference

| Color Name | RGB Value | Used For |
|---|---|---|
| Google Blue | `rgb(26, 115, 232)` | Primary buttons, links, active states, accents |
| Dark Blue (hover) | `rgb(21, 88, 176)` | Button hover states |
| Google Green | `rgb(52, 168, 83)` | Gradient accents, green category badge |
| Google Yellow | `rgb(251, 188, 4)` | Gradient accents, yellow category badge |
| Near-Black | `rgb(32, 33, 36)` | Primary text, headings |
| Medium Grey | `rgb(95, 99, 104)` | Secondary text, subtitles |
| Dark Grey | `rgb(60, 64, 67)` | Post body text |
| Border Grey | `rgb(218, 220, 224)` | All borders, dividers |
| Page Background | `rgb(248, 250, 253)` | Body background, recessed elements |
| White | `rgb(255, 255, 255)` | Card backgrounds, panel fills |
| Blue Tint Light | `rgb(232, 240, 254)` | Blue category badge bg, hero glow, quote box |

---

## Design Inspiration

The visual design is modeled after **Google Workspace** (`workspace.google.com/ai/customers/`):

- Light near-white page background
- White card surfaces with subtle borders and shadows
- Google's brand color palette (blue, green, yellow)
- Large rounded corners (24–32px)
- Compact negative letter-spacing on headings
- Pill-shaped filter chips
- Frosted glass navbar

No Google logos, branding, or text was copied. Only the visual layout language was used as inspiration.

---

## Responsive Design Notes

The layout uses Bootstrap's grid (`container`, `row`, `col-*`) for the main structure. On desktop, story cards appear in 3 columns. On tablet, 2 columns. On mobile, 1 column — Bootstrap handles this with responsive column classes like `col-md-6 col-lg-4`.

The custom `@media` query in `style.css` handles additional mobile refinements beyond what Bootstrap provides: reducing hero padding, enabling horizontal scrolling for filter chips, and adjusting image heights.

---
