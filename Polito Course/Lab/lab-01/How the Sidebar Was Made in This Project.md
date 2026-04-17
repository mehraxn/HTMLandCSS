# How the Sidebar Was Made in This Project

This README explains how the sidebar was built in your project, step by step, in a beginner-friendly way.

---

## 1. What is a sidebar

A sidebar is a section of the page that usually stays on one side of the main content.

It is often used for

 navigation
 filters
 categories
 related links
 extra information

In your project, the sidebar is used for time filters such as

 Oggi
 Questa settimana
 Questo mese

So the sidebar helps the user browse content by time.

---

## 2. The HTML part of the sidebar

Your sidebar HTML is

```html
aside id=sidebar aria-label=Time filters
  h2 class=sidebar-headingSfogliah2
  ul id=filter-list
    lia href=# class=filter-link activeOggiali
    lia href=# class=filter-linkQuesta settimanaali
    lia href=# class=filter-linkQuesto meseali
  ul
aside
```

---

## 3. Why did we use `aside`

We used `aside` because it is a semantic HTML element.

That means it gives meaning to the content.

`aside` tells the browser and the developer

 “This is related content, but it is not the main content.”

So in this project

 the main content is probably the list of events or items
 the sidebar is an extra section used to filter or browse that content

If we had used a `div` instead, it could still work visually, but it would not give the same meaning.

---

## 4. What does each line in the HTML do

### `aside id=sidebar aria-label=Time filters`

 `aside` creates a semantic side section
 `id=sidebar` gives it a unique name for CSS styling
 `aria-label=Time filters` helps screen readers understand the purpose of this sidebar

### `h2 class=sidebar-headingSfogliah2`

 this is the title of the sidebar
 `Sfoglia` is Italian and here it means something like Browse or Explore
 in this project, it means browse the content using these time filters

### `ul id=filter-list`

 creates an unordered list
 the filter options are organized as list items

### `lia href=# class=filter-link activeOggiali`

 one filter option
 `Oggi` means Today
 the `a` tag makes it clickable
 `active` usually means this is the currently selected filter

### The other `li` items

 `Questa settimana` = This week
 `Questo mese` = This month
 these are more filter options

---

## 5. The CSS of the sidebar

Your sidebar CSS is

```css
#sidebar {
  width 200px;
  flex-shrink 0;
  background-color #ffffff;
  border 1px solid #e0dbd2;
  border-radius 10px;
  padding 1.5rem;
  box-shadow 0 2px 12px rgba(0, 0, 0, 0.07);
  position sticky;
  top 88px;
}
```

Now let us understand each property.

---

## 6. What each CSS line does

### `width 200px;`

This gives the sidebar a fixed width.

So the sidebar takes 200 pixels of horizontal space.

---

### `flex-shrink 0;`

This is important when the sidebar is inside a flex container.

It means

 “Do not shrink this sidebar when there is less space.”

Without this line, flexbox might make the sidebar smaller.

---

### `background-color #ffffff;`

This makes the background white.

---

### `border 1px solid #e0dbd2;`

This gives the sidebar a thin border.

---

### `border-radius 10px;`

This rounds the corners.

---

### `padding 1.5rem;`

This adds inner space between the content and the border.

If the root font size is 16px, then

 `1rem = 16px`
 `1.5rem = 24px`

So this means about 24px of inner spacing.

---

### `box-shadow 0 2px 12px rgba(0, 0, 0, 0.07);`

This adds a soft shadow around the sidebar.

It makes the box look slightly lifted from the page.

---

### `position sticky;`

This makes the sidebar stick while scrolling.

It does not place the sidebar on the left.

It only controls how the sidebar behaves when the page scrolls.

---

### `top 88px;`

This works together with `position sticky`.

It means

 “When the sidebar becomes sticky, keep it 88px from the top of the page.”

Usually this is done so the sidebar does not go under a top header.

---

## 7. What actually puts the sidebar on the left

This is the most important idea.

The sidebar is not on the left because of `#sidebar` alone.

The `#sidebar` CSS only gives it

 width
 style
 sticky behavior

What usually puts it on the left is the parent container.

For example

```html
div class=layout
  aside id=sidebar...aside
  main class=content...main
div
```

And then

```css
.layout {
  display flex;
  gap 2rem;
}
```

### Why does this make the sidebar go left

Because

 `display flex` puts children side by side
 by default, flexbox arranges them in a row
 in left-to-right pages, the first child goes on the left
 the second child goes on the right

So if the sidebar comes first in the HTML, it appears on the left side.

---

## 8. Why does the sidebar take space before the items

Because it is still part of the normal layout.

It is not floating above the content.

It is not `position absolute`.

It is a normal box inside the layout, and it has

```css
width 200px;
```

So the browser says

 sidebar gets 200px
 main content gets the remaining space

That is why the content starts after the sidebar.

---

## 9. Does `position sticky` place it on the left

No.

This is a very important point.

`position sticky` does not mean

 left
 right
 before content
 after content

It only means

 while scrolling, keep this element stuck at a certain position

So in your project

 the parent layout likely places the sidebar on the left
 `sticky` only makes it stay visible while the user scrolls

---

## 10. What is the likely full layout idea in this project

A very common structure for your project would be something like this

```html
div class=page-layout
  aside id=sidebar
    ...filters...
  aside

  section class=items-area
    ...cards or events...
  section
div
```

And the CSS would be something like

```css
.page-layout {
  display flex;
  gap 2rem;
  align-items flex-start;
}

#sidebar {
  width 200px;
  flex-shrink 0;
}

.items-area {
  flex 1;
}
```

### What happens here

 the parent uses `display flex`
 the sidebar comes first, so it goes left
 the sidebar keeps its 200px width
 the items area stretches and uses the remaining width

---

## 11. Why is `ul` used inside the sidebar

Because the filter options are a list of choices.

That makes `ul` a good and semantic choice.

So the structure is

 `aside` = side related content
 `h2` = title of the sidebar
 `ul` = list of filters
 `li` = each filter item
 `a` = clickable filter link

This is a clean and logical HTML structure.

---

## 12. Summary of the whole sidebar creation process

Here is the full process in simple order

### Step 1 Create the sidebar in HTML

Use a semantic element

```html
aside id=sidebar...aside
```

This creates the sidebar section.

### Step 2 Put it together with the main content

Wrap both in a parent container.

```html
div class=layout
  aside id=sidebar...aside
  main...main
div
```

### Step 3 Use flexbox on the parent

```css
.layout {
  display flex;
}
```

This puts the sidebar and main content side by side.

### Step 4 Give the sidebar a width

```css
#sidebar {
  width 200px;
}
```

Now the sidebar takes its own space.

### Step 5 Prevent shrinking

```css
flex-shrink 0;
```

Now the sidebar keeps its width.

### Step 6 Style it

Add

 background color
 border
 border radius
 padding
 shadow

This gives it the card-like look.

### Step 7 Make it sticky

```css
position sticky;
top 88px;
```

Now it stays visible while scrolling.

---

## 13. Final conclusion

In this project, the sidebar was made by combining

### Semantic HTML

 `aside` for the sidebar
 `h2` for the heading
 `ul` and `li` for the filter options

### Layout CSS

 a parent container, usually with `display flex`
 the sidebar placed first in the HTML, so it appears on the left

### Sidebar CSS

 `width 200px` to reserve space
 `flex-shrink 0` to keep that width
 visual styling like background, border, radius, padding, and shadow
 `position sticky` and `top 88px` to keep it visible while scrolling

So the key idea is

 The sidebar is on the left because of the parent layout and HTML order, not because of `position sticky`.

And the key role of the sidebar in your project is

 to let the user browse or filter the content by time.
