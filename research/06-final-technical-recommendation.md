# 06 — Final Technical Recommendation and Development Roadmap

## 1. Executive Summary

This research investigated how GoSmarter.ai could extend its existing 1D cutting optimisation capabilities into two-dimensional cutting and multi-constraint production planning for metals manufacturers.

The investigation considered four algorithmic approaches and five open-source technologies, alongside real-world manufacturing constraints involving material compatibility, certification, inventory, offcut reuse and production planning.

A preliminary Python proof-of-concept was also implemented using Rectpack.

**My recommendation is that GoSmarter should investigate a modular approach, combining geometric nesting algorithms with its existing manufacturing-specific data and traceability capabilities.**

Rather than developing a completely new optimisation algorithm initially, GoSmarter could evaluate and adapt existing open-source technologies.

Rectpack offers a practical rectangular packing baseline, PackingSolver warrants further evaluation for more advanced cutting problems, and Google OR-Tools could complement these technologies through constraint-based planning and scheduling.

These recommendations are preliminary and require further benchmarking before production adoption.

## 2. Research Findings

### Finding 1 — Geometric efficiency is not sufficient

A cutting arrangement with high material utilisation may still be unsuitable for manufacturing.

For example, a geometrically efficient plan might select a steel plate with the wrong material grade or insufficient thickness.

Therefore, GoSmarter must distinguish between:

- Geometric feasibility.
- Material compatibility.
- Manufacturing feasibility.
- Production and commercial objectives.

Hard constraints should be satisfied before optimising objectives such as cost, scrap reduction or production time.

### Finding 2 — Open-source technologies provide useful foundations

The technologies investigated have different strengths.

| Technology | Recommended Research Role |
|---|---|
| Rectpack | Initial rectangular packing prototype and baseline |
| PackingSolver | Further investigation of cutting-specific optimisation |
| Google OR-Tools | Multi-constraint allocation, planning and scheduling |
| SVGnest | Research into irregular-shape nesting |
| libnest2d | Investigation of customisable nesting integration |

No single technology has been validated during this project as a complete production solution for GoSmarter.

### Finding 3 — GoSmarter's manufacturing capabilities offer potential differentiation

Geometric nesting libraries concentrate on arranging components.

GoSmarter could provide additional value through the integration of:

- Steel grade and thickness matching.
- Mill certificate and heat/batch traceability.
- Inventory availability.
- Reusable offcut management.
- Production planning and order priorities.
- Human review and approval.

This would allow the platform to evaluate not only whether parts can fit, but whether a proposed cutting plan is appropriate for the manufacturer's requirements.

## 3. Python Proof-of-Concept Findings

A preliminary rectangular packing experiment was implemented using Rectpack.

The prototype:

1. Created a rectangular steel plate.
2. Registered components with unique identifiers.
3. Enabled 90-degree rotations.
4. Executed the packing algorithm.
5. Retrieved successfully placed components.
6. Identified unpacked components.
7. Calculated material utilisation and unused area.
8. Reported whether every requested component had been packed.

### Experimental Results

| Metric | Original Scenario | Modified Scenario |
|---|---:|---:|
| Plate dimensions | 5000 × 4000 mm | 5000 × 4000 mm |
| Parts requested | 3 | 3 |
| Parts packed | 2 | 3 |
| Material utilisation | 37.5% | 47.5% |
| Unused area | 62.5% | 52.5% |
| Order geometrically complete | No | Yes |

In the original scenario, one component was too large to fit inside the available plate, even after rotation.

In the modified scenario, that component's dimensions were reduced, allowing all three components to be packed.

### Interpretation

These experiments demonstrate that Rectpack can support basic rectangular placement and that Python can process the results into useful manufacturing metrics.

However, the increase from 37.5% to 47.5% utilisation does not prove that the algorithm improved.

The component requirements changed between the experiments.

The prototype also did not incorporate cutting kerf, machine-specific limitations, material traceability or stock selection.

Therefore, these findings represent an initial technical demonstration rather than proof of production readiness.

## 4. Recommended Technical Direction

### First Priority — Establish a Reliable Rectangular Nesting Baseline

Continue using Rectpack to establish initial rectangular packing performance.

This approach offers a relatively accessible Python implementation and can provide baseline measures of:

- Material utilisation.
- Unpacked components.
- Computation time.
- Number of stock plates required.
- Behaviour under different component sizes and quantities.

The existing prototype provides a starting point for this work.

### Second Priority — Evaluate PackingSolver

PackingSolver should be a priority for the next technical evaluation because it supports multiple cutting and packing formulations.

Its documented capabilities include rectangular and irregular packing, guillotine-cutting problems and cutting-specific constraints within appropriate formulations.

These features could make it suitable for more advanced manufacturing requirements.

However, its performance, integration complexity and practical suitability have not yet been tested in this project.

A controlled benchmark against Rectpack is recommended.

### Third Priority — Investigate Google OR-Tools for Advanced Planning

Google OR-Tools should be evaluated for constraints beyond geometric nesting.

Potential applications include:

- Selecting compatible stock.
- Allocating material to orders.
- Managing production priorities.
- Scheduling machine operations.
- Evaluating alternative production plans.

One possible architecture would allow a nesting engine to generate candidate geometric arrangements while a planning component evaluates allocation and scheduling decisions.

The feasibility and performance of this combined approach would require further investigation.

### Fourth Priority — Explore Irregular Nesting and Reusable Offcuts

The ShapeSight proposal highlights the potential value of measuring and reusing irregular steel plate remnants.

Irregular offcuts cannot always be accurately represented by their rectangular bounding dimensions.

GoSmarter should therefore investigate technologies capable of working with polygon geometry.

PackingSolver's irregular packing functionality and technologies such as SVGnest offer relevant research directions.

libnest2d could also be investigated, although its documented limitations involving concave polygons and holes require particular attention.

The integration of irregular geometry with certification and inventory records would be an important development consideration.

## 5. Proposed GoSmarter Architecture

A possible future workflow could consist of the following stages:

**Stage 1 — Customer Order Input**

Receive component dimensions, quantities, material specifications and delivery requirements.

**Stage 2 — Material Compatibility Validation**

Check stock against material grade, thickness, certification and other mandatory requirements.

**Stage 3 — Inventory and Offcut Selection**

Identify compatible available plates and potentially reusable certified offcuts.

**Stage 4 — Geometric Nesting**

Generate candidate cutting arrangements using an appropriate packing algorithm.

**Stage 5 — Manufacturing Feasibility**

Validate cutting clearances, permitted rotations, machine limitations and relevant process requirements.

**Stage 6 — Production Planning**

Assess cutting time, production priorities, costs and available resources.

**Stage 7 — Results and Recommendations**

Present feasible cutting plans with material utilisation, unplaced parts, estimated waste and relevant trade-offs.

**Stage 8 — Human Approval**

Allow the production planner to review, modify or approve the recommended plan.

This is a conceptual architecture, not an implemented or validated GoSmarter system.

## 6. Recommended Benchmarking Strategy

Before selecting a technology for production, GoSmarter should conduct controlled benchmarking using representative manufacturing problems.

The same input data and comparable constraints should be used when evaluating different algorithms.

### Suggested Metrics

| Metric | What It Measures |
|---|---|
| Material utilisation | Percentage of selected stock area occupied by required parts |
| Order completion | Whether all requested components were accommodated |
| Computation time | Time required to generate a cutting plan |
| Stock consumption | Number and cost of plates used |
| Cutting feasibility | Compliance with geometric and machine constraints |
| Offcut reuse | Ability to incorporate existing remnants |
| Reliability | Consistency and validity of generated results |

### Suggested Test Scenarios

1. Small rectangular packing problems.
2. Larger orders containing many different part sizes.
3. Multiple compatible plates with different dimensions.
4. Rotation restrictions.
5. Cutting-clearance and guillotine-cutting requirements.
6. Irregular components and reusable offcuts.
7. Orders involving different grades, thicknesses and deadlines.

Testing should distinguish between algorithm-supported constraints and rules implemented in GoSmarter's surrounding software.

## 7. Proposed Development Roadmap

### Phase 1 — Prototype Validation

**Objective:** Establish a reliable baseline.

- Refine the existing Rectpack experiment.
- Add repeatable test datasets.
- Record runtime and placement results.
- Evaluate whether all requested parts were accommodated.
- Test and document additional geometric constraints.

**Expected outcome:** A repeatable rectangular packing benchmark.

### Phase 2 — Alternative Technology Evaluation

**Objective:** Identify the most suitable geometric optimisation approach.

- Test PackingSolver on comparable datasets.
- Evaluate relevant cutting-specific features.
- Compare results with the Rectpack baseline.
- Assess integration complexity and applicable licence obligations.

**Expected outcome:** An evidence-based recommendation for the next nesting technology.

### Phase 3 — Manufacturing Integration

**Objective:** Introduce real-world material requirements.

- Connect orders to certified material records.
- Validate steel grade and thickness compatibility.
- Include inventory availability and stock selection.
- Investigate cutting kerf and machine limitations.
- Preserve traceability throughout the cutting workflow.

**Expected outcome:** A prototype capable of evaluating basic manufacturing feasibility.

### Phase 4 — Advanced Production Planning

**Objective:** Support more complex manufacturing decisions.

- Investigate OR-Tools for stock allocation and scheduling.
- Introduce multiple optimisation objectives.
- Explore certified offcut reuse and irregular geometry.
- Compare alternative cutting and production plans.
- Develop planner-facing recommendations and approvals.

**Expected outcome:** A more comprehensive production optimisation prototype.

### Phase 5 — Industrial Validation

**Objective:** Assess suitability for real manufacturing environments.

- Test on representative or appropriately authorised customer data.
- Validate results with manufacturing specialists.
- Assess performance, reliability and integration requirements.
- Review licensing and operational risks.
- Determine what additional development is needed before deployment.

**Expected outcome:** A justified decision on production development.

## 8. Risks and Limitations

The proposed approach faces several important limitations.

**Geometric limitations:** A successful packing arrangement does not automatically guarantee practical cutting feasibility.

**Manufacturing complexity:** Material certification, traceability and machine restrictions require additional software logic.

**Computational performance:** More sophisticated optimisation models may become computationally expensive as problem sizes increase.

**Integration requirements:** Existing libraries may require substantial adaptation to work with GoSmarter's inventory, user interfaces and production workflows.

**Licensing obligations:** Open-source licences and dependencies must be reviewed before commercial deployment.

**Research limitations:** The current project includes direct testing of Rectpack only. The other technologies were assessed using available documentation rather than equivalent hands-on experiments.

These limitations should guide subsequent testing and development.

## 9. Final Recommendation

My overall recommendation is that GoSmarter should **adopt an incremental, evidence-based approach to developing its 2D optimisation capability**.

Rectpack is a suitable starting point for establishing a rectangular packing baseline because a working Python proof-of-concept has already been demonstrated.

PackingSolver should be the next priority for technical evaluation due to its cutting-specific formulations and broader documented functionality.

Google OR-Tools should be investigated as a complementary technology for material allocation, manufacturing constraints and production scheduling.

For irregular geometry and offcut reuse, specialist nesting technologies should be assessed alongside GoSmarter's proposed ShapeSight capabilities.

The main commercial opportunity may lie not in developing a completely new nesting algorithm, but in combining suitable optimisation technologies with GoSmarter's existing material data, inventory, traceability and manufacturing decision-support capabilities.

However, further benchmarking, manufacturing validation and integration analysis are necessary before committing to a production architecture.

## 10. Conclusion

The research demonstrates that open-source optimisation technologies provide several promising foundations for extending GoSmarter's existing 1D cutting capabilities into 2D sheet and plate optimisation.

The Rectpack proof-of-concept confirms that basic rectangular packing can be implemented and its results processed using Python.

Nevertheless, a commercially useful manufacturing system must go beyond geometric nesting to address material compatibility, certificate traceability, machine constraints, inventory, offcut reuse and production planning.

A modular approach, supported by controlled benchmarking and incremental development, offers a practical direction for further research.

The next major decision should be informed by a fair comparison of Rectpack and PackingSolver, followed by an assessment of how advanced planning technologies such as OR-Tools could integrate with the selected nesting engine.

## 11. References and Supporting Research

- [Optimisation Algorithms](02-optimisation-algorithms.md)
- [Rectpack Proof-of-Concept](03-rectpack-proof-of-concept.md)
- [Open-Source Technology Comparison](04-open-source-technology-comparison.md)
- [Manufacturing Constraints](05-manufacturing-constraints.md)
- [Python Implementation](../experiments/gosmarter_report.py)
- [Rectpack — GitHub](https://github.com/secnot/rectpack)
- [PackingSolver — GitHub](https://github.com/fontanf/packingsolver)
- [Google OR-Tools Documentation](https://developers.google.com/optimization)
- [SVGnest — GitHub](https://github.com/Jack000/SVGnest)
- [libnest2d — GitHub](https://github.com/tamasmeszaros/libnest2d)
- GoSmarter.ai — *Research Brief: Advanced Optimisation for 2D and Multi-Constraint Production Planning* (privately supplied).
- Nightingale HQ — *ShapeSight Steel Plate Offcuts for Reuse* (privately supplied proposal).
