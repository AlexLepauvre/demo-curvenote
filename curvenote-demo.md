---
title: Curvenote demo
date: 2024-11-19
authors:
    - name: 'Alex Lepauvre'
      affiliations:
        - id: 'MPIAE'
          name: Max Planck Institute for empirical aesthetics
          email: alex.lepauvre@ae.mpg.de
    - name: 'Lucia Melloni'
      affiliations:
        - id: MPIAE
abstract: |
    In this paper, I am illustrating all the useful features of curvtenote to make paper writing more efficient and transparent. With this tool, we can directly link the output of our Jupyter notebook code in our paper. Any changes to the code are automatically reflected in the paper
exports:
  - format: pdf
---


# Introduction
The study of penguin species provides key insights into the ecological adaptations of seabirds to diverse environments. The Palmer Penguins dataset [](doi:10.32614/RJ-2022-020), featuring three species from the Palmer Archipelago (see [](#Figure1)), has become a benchmark dataset for exploring biological trends in bill morphology, flipper length, and body mass. Here, we aim to investigate the differences in body mass across species and sexes to understand how sexual dimorphism and ecological pressures shape these traits. By using statistical and visualization techniques, we provide a concise analysis while showcasing the utility of Curvenote for creating dynamic, reproducible scientific documents.

:::{figure} ./PalmerArchipelago.svg
:label: Figure1
Palmer Archipelago
:::

# Methods

We analyzed the Palmer Penguins dataset, which includes data on three penguin species (Adélie, Chinstrap, and Gentoo). The dataset was preprocessed to remove missing values, and body mass was grouped by species and sex. Mean body mass and the standard deviation of the mean (STD) were computed for each group (see [](#Figure2)). Visualizations were created using Python and Matplotlib, with error bars to represent variability. All analyses and figures were dynamically integrated into the manuscript using Curvenote.

:::{figure} #PenguinWeight
:name: Figure 2
Weight of the Penguin separately with each species and sex (error bars: standard deviation from the mean)
:::

