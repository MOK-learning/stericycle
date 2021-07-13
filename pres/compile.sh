#!/usr/bin/env bash

TAG=MOKeefe_Stericycle

pandoc markdown_beamer_example.md -t beamer -o ${TAG}.pdf --slide-level 2 --include-in-header style/my_style.tex --variable urlcolor=steelblue --variable linkcolor=white
