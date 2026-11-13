# 2D Cutting Optimisation in Metals Manufacturing

## Project Overview

This repository documents an independent research project undertaken through a voluntary industry collaboration with Nightingale HQ, the company behind GoSmarter.ai.

The project investigates open-source algorithms and optimisation frameworks that could support two-dimensional (2D) cutting and nesting in metals manufacturing.

The primary objective is to evaluate how existing optimisation technologies could help manufacturers reduce material waste, improve stock utilisation, reuse metal offcuts and accommodate practical production constraints.

## Research Objectives

1. Explain the differences between 1D and 2D cutting optimisation.
2. Investigate heuristic, metaheuristic, mixed-integer programming and constraint programming approaches.
3. Compare open-source tools, including Rectpack, Google OR-Tools, PackingSolver, SVGnest and libnest2d.
4. Evaluate manufacturing constraints such as steel grade, thickness, certification, cutting kerf and machine limitations.
5. Recommend promising technical approaches for practical metals manufacturing applications.
6. Propose a small proof of concept using synthetic cutting data.

## Research Methodology

The project uses a combination of technical documentation review, algorithm comparison and assessment of industrial manufacturing requirements.

Where practical, small Python experiments will be used to investigate geometric packing behaviour.

Documented software capabilities will be distinguished from experimental observations and proposed implementations.

## Project Status

**Status:** Research in progress.

The repository will be updated with technical findings, library comparisons, recommendations and any completed experiments.

## Tools and Technologies Under Investigation

- Python
- Rectpack
- Google OR-Tools
- PackingSolver
- SVGnest
- libnest2d

## Research Independence

This is an independently authored research project. It is not an official GoSmarter software product or a representation of its proprietary implementation.

All examples and experiments will use public or synthetic information unless otherwise authorised.


## Practical Experiments

### Rectpack 2D Cutting Proof-of-Concept

Developed a Python prototype using Rectpack to investigate rectangular steel plate cutting.

The experiment covers:
- Material utilisation and unused area
- Successfully packed and unpacked components
- Order completion
- Changes in component dimensions

[View Rectpack Research](research/03-rectpack-proof-of-concept.md)

[View Python Implementation](experiments/gosmarter_report.py)

### Open-Source Technology Comparison

[View Technology Comparison](research/04-open-source-technology-comparison.md)

### Manufacturing Constraints and Production Planning

[View Manufacturing Constraints Research](research/05-manufacturing-constraints.md)

### Final Technical Recommendation and Development Roadmap

[View Final Technical Recommendation](research/06-final-technical-recommendation.md)
