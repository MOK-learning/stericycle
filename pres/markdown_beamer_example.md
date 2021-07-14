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

## What fraction of customers churn?
\centering
\includegraphics[width=0.7\textwidth]{images/churn.png}

- 73.5% of customers are loyal
- 26.5% have churned
- Can we predict when this is going to happen?

## Churn demographics
\centering
\includegraphics[width=0.49\textwidth]{images/males.png}
\includegraphics[width=0.49\textwidth]{images/females.png}

- Firstly, we will look at how demographic information plays a part in predicting customer churn
- Looks like gender does not provide any useful insight into whether or not a customer will churn

## Churn demographics
\centering
\includegraphics[width=0.3\textwidth]{images/partner.png}
\includegraphics[width=0.3\textwidth]{images/age.png}
\includegraphics[width=0.3\textwidth]{images/children.png}

- Customers who: 
    - Do not have partners are 13% more likely to churn
    - Are senior citizens are 18% more likely to churn
    - Do not have dependents are 16% more likely to churn

## Services used
\centering
\includegraphics[width=0.3\textwidth]{images/phone.png}
\includegraphics[width=0.3\textwidth]{images/internet.png}
\includegraphics[width=0.3\textwidth]{images/streaming.png}

- Whether or not a customer uses a phone service does not seem to effect whether or not they will churn
- Fibre optic internet users are much more likely to churn (42%) than DSL (19%) and non internet users (7%)
- Streaming service users are 8% more likely to churn
