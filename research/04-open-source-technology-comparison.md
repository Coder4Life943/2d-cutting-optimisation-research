# 04 — Open-Source Technology Comparison for 2D Cutting Optimisation

## 1. Introduction

This section compares five open-source optimisation technologies identified in the GoSmarter research brief:

1. Rectpack
2. Google OR-Tools
3. PackingSolver
4. SVGnest
5. libnest2d

The objective is to evaluate their capabilities, limitations, licensing and potential suitability for integration into GoSmarter's manufacturing optimisation platform.

The assessment distinguishes between documented software capabilities and functionality demonstrated through the project's Python experiments.

## 2. Technology Comparison

| Technology | Main Application | Language | Licence | Potential GoSmarter Application |
|---|---|---|---|---|
| Rectpack | Rectangular packing heuristics | Python | Apache 2.0 | Fast rectangular nesting baseline |
| Google OR-Tools | Constraint optimisation and scheduling | C++ with Python and other interfaces | Apache 2.0 | Material allocation, planning and complex constraints |
| PackingSolver | Cutting-stock and geometric packing | C++ and Python | MIT | Guillotine cutting, rectangular and irregular packing |
| SVGnest | Irregular-shape nesting | JavaScript | MIT | Exploring polygon nesting and offcut reuse |
| libnest2d | Customisable 2D nesting framework | C++ | LGPL 3.0 | Integration of specialised nesting functionality |

## 3. Rectpack

Rectpack provides heuristic algorithms for packing rectangular components into rectangular containers.

Its supported approaches include MaxRects, Skyline and Guillotine algorithm families.

**Strengths**
- Python integration is relatively straightforward.
- Suitable for rapid prototyping.
- Supports rectangular packing and 90-degree rotations.
- Provides coordinates and dimensions of successfully packed components.

**Limitations**
- Does not directly provide a complete metals-specific production planning system.
- Does not itself verify steel grade, thickness or certificate traceability.
- Requires additional modelling for cutting clearances and operational constraints.
- Does not provide a general guarantee of globally optimal layouts.

**Practical evidence**

A Python proof-of-concept was implemented and tested.

In the original scenario, Rectpack placed two of three required components, achieving 37.5% utilisation.

After changing the third component's dimensions, all three components were placed, achieving 47.5% utilisation.

These results demonstrate basic functionality, not superiority over other optimisation technologies.

**Assessment:** A promising starting point for rectangular nesting and Python-based prototyping.

## 4. Google OR-Tools

Google OR-Tools is an open-source suite of mathematical and combinatorial optimisation tools.

It includes CP-SAT, which supports constraint-based modelling, including non-overlapping rectangular placement, scheduling and resource allocation.

**Strengths**
- Supports complex logical and mathematical constraints.
- Provides Python integration.
- Suitable for scheduling and resource-allocation problems.
- Could support the modelling of material availability, costs and production priorities.

**Limitations**
- Requires mathematical formulation of the optimisation problem.
- Complex models can be computationally demanding.
- Does not provide a complete, ready-made industrial 2D nesting workflow.
- Irregular geometry requires additional modelling or specialist tools.

**Assessment:** A promising framework for GoSmarter's multi-constraint production planning requirements, potentially complementing a dedicated nesting engine.

## 5. PackingSolver

PackingSolver is an open-source framework specifically developed for cutting and packing optimisation.

Its supported problem types include rectangular packing, guillotine cutting and irregular-shape packing.

**Strengths**
- Provides multiple cutting and packing problem formulations.
- Supports objectives involving bin usage, cost and leftover material.
- Offers cutting-specific constraints, including cut thickness and defects in applicable formulations.
- Provides C++, command-line and Python interfaces.
- Has an MIT licence.

**Limitations**
- Requires selecting and configuring the appropriate problem formulation.
- More advanced features may increase implementation complexity.
- Manufacturing-specific integration is still necessary.
- Real-world performance and suitability would need benchmarking.

**Assessment:** Particularly promising for further evaluation because its documented functionality addresses more cutting-specific requirements than the initial Rectpack prototype.

## 6. SVGnest

SVGnest is a browser-based nesting tool designed for irregular vector shapes.

It uses geometric nesting approaches, including no-fit polygons, alongside a genetic algorithm for optimisation.

**Strengths**
- Supports irregular polygon nesting.
- Supports placing parts within suitable interior holes.
- Useful for exploring nesting of non-rectangular components.
- Open-source and browser-based.

**Limitations**
- Primarily designed around SVG geometry and browser-based interaction.
- Commercial SaaS integration would require engineering work.
- Does not inherently provide steel certification, inventory or production management.
- Industrial reliability and scalability would require independent testing.

**Assessment:** Useful as a research reference for irregular-shape nesting and potential offcut reuse.

## 7. libnest2d

libnest2d is a C++ library for two-dimensional nesting.

It provides a customisable framework for implementing and integrating geometric nesting functionality.

**Strengths**
- Designed for software integration and customisation.
- Uses geometric placement approaches.
- Relevant to applications requiring more control over nesting implementation.

**Limitations**
- Requires C++ integration expertise.
- Has additional software dependencies.
- Its repository documents incomplete functionality and limitations involving concave polygons and holes.
- LGPL 3.0 obligations require assessment before commercial integration.

**Assessment:** A potential longer-term integration option, although its current geometry support and implementation requirements need careful validation.

## 8. Commercial Integration and Licensing

Open-source software is not automatically free of legal obligations.

Rectpack and Google OR-Tools use Apache 2.0 licences, while PackingSolver and SVGnest use MIT licences.

These are generally permissive licences, subject to their relevant conditions.

libnest2d uses LGPL 3.0, which requires additional consideration of distribution, linking, modification and compliance obligations.

Before commercial deployment, GoSmarter should review the applicable licence versions, dependencies and intended deployment architecture.

The existence of an open-source licence does not establish that a solution is production-ready.

## 9. Preliminary Recommendation for GoSmarter

Based on the documented capabilities and the limited Rectpack experiment, a staged approach appears reasonable.

**Short term — Rectpack**

Continue using Rectpack as a baseline for rectangular cutting experiments, measuring utilisation, packing completeness and runtime.

**Next evaluation — PackingSolver**

Investigate PackingSolver as a potentially more manufacturing-focused cutting and packing engine. Its documented cutting constraints and multiple problem types make it particularly relevant.

**Multi-constraint planning — Google OR-Tools**

Evaluate whether OR-Tools could complement a packing engine by handling material allocation, production priorities, stock selection and scheduling.

**Irregular nesting — SVGnest and libnest2d**

Investigate these technologies for more complex geometries, while assessing integration complexity and their limitations.

This is a preliminary technical direction, not a validated production architecture.

## 10. Proposed Integration Approach

A future GoSmarter optimisation workflow could:

1. Receive customer orders and required component dimensions.
2. Filter available inventory by steel grade, thickness, certification and availability.
3. Select a suitable nesting approach for the required geometry.
4. Generate candidate cutting arrangements.
5. Check relevant cutting and manufacturing constraints.
6. Identify unpacked components and alternative compatible stock.
7. Evaluate material utilisation, cost, production time and offcut reuse opportunities.
8. Present feasible recommendations to a human production planner for approval.

This proposed workflow would combine geometric optimisation with GoSmarter's manufacturing-specific data and decision-support requirements.

## 11. Further Validation Required

A fair technology benchmark should use identical datasets and consistent constraints wherever supported.

Relevant evaluation metrics include:

- Material utilisation percentage.
- Number of components successfully placed.
- Computation time.
- Number and cost of steel plates required.
- Cutting feasibility and constraint satisfaction.
- Ability to incorporate reusable offcuts.
- Integration complexity and licence suitability.

The current Rectpack experiments establish a basic prototype but do not establish comparative algorithm performance.

## 12. Conclusion

No single technology has yet been demonstrated to meet every requirement of the GoSmarter research brief.

Rectpack has been successfully tested as a simple rectangular packing prototype.

PackingSolver warrants further investigation for cutting-specific optimisation, while OR-Tools may provide complementary capabilities for constraint-based production planning.

SVGnest and libnest2d offer potential research directions for more complex nesting problems.

A combined approach may ultimately be appropriate, but it should be selected only after controlled benchmarking and evaluation of real manufacturing constraints.

## 13. References

- [Rectpack — GitHub](https://github.com/secnot/rectpack)
- [Google OR-Tools — GitHub](https://github.com/google/or-tools)
- [Google OR-Tools Documentation](https://developers.google.com/optimization)
- [PackingSolver — GitHub](https://github.com/fontanf/packingsolver)
- [PackingSolver Documentation](https://fontanf.github.io/packingsolver/)
- [SVGnest — GitHub](https://github.com/Jack000/SVGnest)
- [libnest2d — GitHub](https://github.com/tamasmeszaros/libnest2d)
- GoSmarter.ai — *Research Brief: Advanced Optimisation for 2D and Multi-Constraint Production Planning* (privately supplied project brief).
