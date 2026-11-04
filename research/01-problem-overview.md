# 01 — Problem Overview: 2D Cutting Optimisation

## 1. Introduction

Material utilisation is an important challenge in metals manufacturing. Manufacturers must determine how to cut required components from available stock while minimising unnecessary waste and satisfying production requirements.

GoSmarter.ai currently provides cutting optimisation for long metal products, including bars, beams, tubes and profiles.

This research investigates the potential extension of such optimisation capabilities into two-dimensional (2D) cutting and nesting for sheet and plate metals.

## 2. Understanding 1D and 2D Optimisation

### 1D Cutting Optimisation

One-dimensional cutting optimisation determines how to cut required lengths from long stock materials while minimising unused material.

For example, a manufacturer may need to cut several shorter steel bars from a single 10-metre bar.

### 2D Cutting Optimisation

Two-dimensional cutting optimisation determines how to arrange required shapes within available sheets or plates.

Unlike 1D cutting, 2D nesting introduces additional geometric decisions involving:

- Positioning of parts within a sheet.
- Permitted rotations and orientations.
- Preventing geometric overlap.
- Accounting for cutting kerf and machine restrictions.

These factors make the optimisation problem more complex.

## 3. Measuring Material Utilisation

Material utilisation measures the proportion of available stock used to produce the required parts.

For 2D cutting:

**Material utilisation (%) = (Total area of finished parts / Total area of stock used) × 100**

For example, consider a steel plate measuring 5 m × 4 m.

The total area is 20 m².

If the required parts occupy 12 m², material utilisation is:

**(12 / 20) × 100 = 60%**

The remaining 40% is unused area, but it is not necessarily scrap. Some material may be recoverable as reusable offcuts.

## 4. Manufacturing Constraints

An efficient geometric arrangement is not automatically a valid manufacturing solution.

A practical optimisation system must consider material properties, available inventory and manufacturing requirements.

Relevant constraints include steel grade, thickness, certification, batch traceability, cutting kerf, machine limitations and order priorities.

## 5. Research Problem

The central research challenge is to identify how open-source 2D nesting algorithms could be combined with metals-specific manufacturing constraints.

The objective is to investigate approaches capable of improving material utilisation while supporting practical decisions about costs, production efficiency and reusable offcuts.

The next stage of this research will evaluate mathematical optimisation approaches and existing open-source software libraries.
