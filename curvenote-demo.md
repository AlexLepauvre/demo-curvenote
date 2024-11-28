---
title: Curvenote demo
date: 2024-11-19
authors:
    - name: 'Alex Lepauvre'
      affiliations:
        - id: 'MPIAE'
          name: 'Max Planck Institute for empirical aesthetics'
          email: 'alex.lepauvre@ae.mpg.de'
          orcid: 
    - name: 'Lucia Melloni'
      affiliations:
        - id: 'MPIAE'
          name: 'Max Planck Institute for empirical aesthetics'
          email: 'lucia.melloni@ae.mpg.de'
        - id: 'NYU'
          name: 'Department of Neurology, NYU Grossman School of Medicine, New York, USA'
        - id: 'CIFAR'
          name: 'Canadian Institute for Advanced Research (CIFAR), Brain, Mind, and Consciousness Program, Toronto, ON, Canada'
abstract: |
    In this paper, I am illustrating all the useful features of curvtenote to make paper writing more efficient and transparent. With this tool, we can directly link the output of our Jupyter notebook code in our paper. Any changes to the code are automatically reflected in the paper
exports:
  - format: pdf
    template: arxiv_two_column
keywords: penguins, tutorial
---


# Introduction
The study of penguin species provides key insights into the ecological adaptations of seabirds to diverse environments. The Palmer Penguins dataset [](doi:10.32614/RJ-2022-020), featuring three species from the Palmer Archipelago (see [](#Figure1)), has become a benchmark dataset for exploring biological trends in bill morphology, flipper length, and body mass. Here, we aim to investigate the differences in body mass across species and sexes to understand how sexual dimorphism and ecological pressures shape these traits. By using statistical and visualization techniques, we provide a concise analysis while showcasing the utility of Curvenote for creating dynamic, reproducible scientific documents.

:::{figure} ./PalmerArchipelago.png
:label: Figure1
:name: Figure 1
Palmer Archipelago
:::


# Methods

We analyzed the Palmer Penguins dataset, which includes data on three penguin species (Adélie, Chinstrap, and Gentoo). The dataset was preprocessed to remove missing values, and body mass was grouped by species and sex. Mean body mass and the standard deviation of the mean (STD) were computed for each group (see [](#Figure2)). Visualizations were created using Python and Matplotlib, with error bars to represent variability. All analyses and figures were dynamically integrated into the manuscript using Curvenote.

:::{figure} #PenguinWeight
:label: Figure2
:name: Figure 2
Weight of the Penguin separately with each species and sex (error bars: standard deviation from the mean)
:::

# Results
To investigate the relationship between penguin body mass, beak size, and species, we performed a multiple linear regression analysis. This analysis considered the effects of beak size, species, and their interaction on body mass. The regression model indicated significant effects of beak size with a significant interaction with species (see [](#Table1)), such that the correlation between bill size and weight was weakest for the Gintoo species (see [](#SupplementaryTable1)). This suggests that the relationship between beak size and body mass varies across species. As visualized in [](#Figure3), the ordinary least squares (OLS) regression lines highlight these interspecies differences, providing a deeper understanding of how morphological traits co-vary in response to ecological pressures.

:::{figure} #PenguinCorrelation
:label: Figure3
:name: Figure 3
Correlation between penguins beak size and weight (OLS)
:::


:::{figure} #ANOVAResults
:label: Table1
:name: Table 1
Correlation between penguins beak size and weight (OLS)
:::

# Discussion
Our analysis reveals distinct patterns of body mass variation among the three penguin species, shaped by differences in beak size and the interaction of these traits with species identity. These findings align with previous studies emphasizing the role of ecological adaptation in shaping avian morphology [](doi:10.1038/s41467-018-07634-8). Specifically, the significant interaction term underscores the species-specific adaptations, likely reflecting dietary specialization and niche partitioning among the Palmer Archipelago's penguins.

Sexual dimorphism in penguins has been documented in other contexts [](doi:10.1111/jeb.14168), and our approach demonstrates how statistical modeling can uncover nuanced interrelationships between morphology and ecological traits. The use of dynamic tools like Curvenote enables seamless integration of such analyses, promoting transparency and reproducibility in ecological research. Future studies could extend this work by examining longitudinal changes in body mass and beak size in response to environmental shifts, such as climate change and habitat alteration.

# Acknowledgement

# Supplementary
:::{figure} #ANOVAResults
:label: SupplementaryTable1
:name: Supplementary Table 1
Correlation between penguins beak size and weight (OLS)
:::
