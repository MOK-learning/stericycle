---
title: Example title
author: Michael O'Keefe
date: 15 July 2021
output: 
beamer_presentation:
slide_level: 2
theme: "CambridgeUS"
colortheme: "beaver"
---

## Introduction
- First line this is some text
    - Second line this is some text
        - Third line this is some text

## Second Slide {.t}
- Sometimes you will have a series of slides with figures on that you want to flick between
- Adding text one one slide, but not the other, will shift the figure placement of this slide but not the others
    - Meaning you can't nicely flick between slides
- To set the alignment to the top of the slide, simply add ```{.t}``` to the slide title

## Third Slide
1. This is
1. How you
1. Do a list!

## This slide has figures
![](./style/ATLAS.png){ width=49% }

## Fourth slide
::: columns

:::: column
- This is my first column
- This is my first column
::::

:::: column
- This is my second column
- This is my second column
::::

:::
