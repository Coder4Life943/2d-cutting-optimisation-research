# 05 — Manufacturing Constraints and Real-World Suitability

## 1. Introduction

Two-dimensional cutting optimisation involves more than arranging geometric shapes to minimise material waste.

In metals manufacturing, a cutting plan must also satisfy material specifications, certification requirements, available inventory and production limitations.

This research examines how these constraints affect the suitability of open-source optimisation technologies for GoSmarter.ai.

## 2. Hard Constraints and Optimisation Objectives

Manufacturing requirements can be divided into two main categories.

### Hard Constraints

Hard constraints are mandatory conditions that a valid cutting plan must satisfy.

Examples include:

- Correct steel grade.
- Required material thickness.
- Suitable plate dimensions.
- Material certification and traceability.
- Parts fitting within available material without overlapping.
- Sufficient clearance for the cutting process.
- Relevant machine restrictions.

A plan that violates these conditions may be unsuitable for production, regardless of its material utilisation.

### Optimisation Objectives

Optimisation objectives describe outcomes the manufacturer wants to improve.

Examples include:

- Minimising material waste.
- Reducing material costs.
- Increasing reusable offcut utilisation.
- Minimising production time.
- Reducing the number of plates required.
- Meeting customer deadlines.

Some objectives may conflict. For example, a plan that minimises waste might require additional cutting time.

## 3. Steel Grade and Thickness Matching

Steel components must be manufactured using material that meets the customer's specifications.

An optimisation algorithm might identify a geometrically efficient arrangement while selecting material of an unsuitable grade or thickness.

This creates a distinction between geometric feasibility and manufacturing feasibility.

### Proposed GoSmarter Approach

Before running the nesting algorithm, GoSmarter could filter available inventory according to:

1. Required steel grade.
2. Required thickness.
3. Required dimensions.
4. Relevant material specifications.
5. Stock availability.

Only compatible material would then be considered for cutting optimisation.

## 4. Certification and Heat/Batch Traceability

Metal products may require certification documenting their material properties and origin.

GoSmarter's existing product capabilities include mill certificate processing and material traceability.

A future 2D cutting workflow should preserve relevant certificate and heat/batch information when allocating steel plates to customer orders.

This is particularly important when reusable offcuts are introduced into production.

The optimiser should not recommend material solely because its shape and dimensions are suitable.

Material compatibility and traceability must also be verified.

## 5. Cutting Kerf and Machine Limitations

Kerf is the width of material removed by a cutting process.

A geometric nesting layout that places components directly against each other may not provide sufficient space for the intended cutting operation.

Relevant constraints may include:

- Cutting kerf.
- Required spacing between components.
- Plate edge clearances.
- Machine working-area dimensions.
- Permitted component orientations.
- Machine availability and cutting time.

The applicable restrictions depend on the manufacturing process.

### Rectpack Limitation

The initial Rectpack prototype successfully arranged rectangles but did not independently validate manufacturing cutting clearances or machine restrictions.

These requirements would need further modelling and testing before production deployment.

## 6. Inventory Availability and Stock Selection

A cutting plan must use material that is actually available or can be obtained.

For example, the initial Python experiment used a 5,000 × 4,000 mm steel plate.

One requested component measured 6,000 × 1,000 mm.

The component could not fit within the plate, even with 90-degree rotation.

The prototype correctly identified the component as unpacked.

A more advanced GoSmarter workflow could investigate alternative stock or flag the need to obtain compatible material from a supplier.

Any recommendation would still require checking material specifications, availability, cost and delivery requirements.

## 7. Reusable Offcuts and Remnants

Sheet and plate cutting can generate reusable material with irregular outlines or internal cutouts.

Traditional length-and-width measurements may not represent the true remaining usable shape.

GoSmarter's ShapeSight pilot proposal investigates using computer vision to measure irregular metal offcuts and record their geometry alongside material information.

Potential benefits include:

- Identifying reusable material.
- Reducing unnecessary purchases of new steel.
- Preserving material certificate traceability.
- Improving inventory accuracy.
- Supporting future nesting operations using existing remnants.

### Technical Challenge

Rectpack operates on rectangular geometry.

Irregular offcuts may require polygon-based representations and more specialised nesting approaches.

Technologies such as SVGnest, libnest2d or appropriate PackingSolver formulations warrant further investigation.

## 8. Production Planning Constraints

Manufacturers must consider more than geometric material utilisation.

Operational requirements may include:

- Customer order priorities.
- Production deadlines.
- Machine availability.
- Cutting duration.
- Production sequencing.
- Material handling requirements.
- Stock allocation across multiple orders.

A useful optimisation system should help manufacturers understand the trade-offs between these considerations.

Google OR-Tools is a potential candidate for investigating constraint-based scheduling and allocation alongside a geometric nesting engine.

This potential combination remains a research recommendation rather than a validated GoSmarter implementation.

## 9. Scenario Planning and Human Approval

Manufacturers may benefit from comparing alternative production plans.

For example, a planner could compare:

| Scenario | Potential Advantage | Potential Limitation |
|---|---|---|
| Use existing stock | Avoids purchasing new material | May generate more waste |
| Reuse certified offcuts | Reduces consumption of new steel | Requires suitable geometry and traceability |
| Purchase a larger plate | May accommodate oversized parts | Additional cost and lead time |
| Prioritise urgent orders | May improve delivery performance | Could reduce overall cutting efficiency |

The preferred option depends on the manufacturer's priorities and mandatory requirements.

GoSmarter could provide recommendations while retaining human approval over production decisions.

## 10. Implications for Open-Source Technology Selection

| Requirement | Potential Technical Approach |
|---|---|
| Rectangular placement | Rectpack or PackingSolver |
| Complex material allocation | Mathematical optimisation or constraint programming |
| Production scheduling | Google OR-Tools |
| Irregular-shaped nesting | Specialist polygon nesting technology |
| Certification and traceability | GoSmarter-specific application logic and integration |
| Offcut inventory | Geometry storage, material records and stock-management integration |
| Human approval | Planner-facing interface and decision-support workflow |

These are potential approaches requiring further investigation, not a completed software architecture.

## 11. Recommended Development Approach

A staged development approach could involve:

**Stage 1 — Geometric Optimisation**

Use Rectpack or another appropriate packing engine to generate candidate layouts.

**Stage 2 — Material Compatibility**

Introduce checks for grade, thickness, dimensions, certification and stock availability.

**Stage 3 — Manufacturing Feasibility**

Investigate cutting kerf, machine limitations and permitted orientations.

**Stage 4 — Inventory and Offcut Reuse**

Integrate suitable stock and measured reusable offcuts into the planning workflow.

**Stage 5 — Advanced Production Planning**

Evaluate multiple objectives, production priorities and scheduling requirements.

**Stage 6 — Validation**

Benchmark proposed solutions using representative manufacturing datasets and obtain planner feedback.

## 12. Conclusion

The Rectpack proof-of-concept demonstrates basic rectangular nesting, component identification and material utilisation calculations.

However, it does not establish manufacturing readiness.

A commercially useful GoSmarter 2D optimisation capability would need to combine geometric packing with material compatibility, traceability, inventory, cutting constraints and production planning.

The most promising direction is therefore to evaluate existing optimisation technologies alongside GoSmarter's manufacturing-specific capabilities.

This approach could reduce unnecessary custom algorithm development while allowing GoSmarter to add value through integrated manufacturing decision support.

## 13. References

- GoSmarter.ai — *Research Brief: Advanced Optimisation for 2D and Multi-Constraint Production Planning* (privately supplied).
- Nightingale HQ — *ShapeSight Steel Plate Offcuts for Reuse* (privately supplied proposal).
- GoSmarter — *Initial Future Leaders Briefs* (privately supplied).
- [Rectpack — GitHub](https://github.com/secnot/rectpack)
- [Google OR-Tools Documentation](https://developers.google.com/optimization)
- [PackingSolver — GitHub](https://github.com/fontanf/packingsolver)
