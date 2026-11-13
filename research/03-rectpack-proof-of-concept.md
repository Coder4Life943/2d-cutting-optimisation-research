## Preliminary Proof-of-Concept: Rectpack for 2D Steel Plate Optimisation

### Objective

The objective of this experiment was to investigate whether the open-source Python library Rectpack could be used to arrange rectangular steel components within a larger steel plate.

The experiment also examined how packing results could be processed to calculate material utilisation, identify unpacked components and assess whether all requested parts had been accommodated.

### Methodology

A simple Python prototype was developed using Rectpack.

The prototype:

1. Defined a single rectangular steel plate measuring 5,000 × 4,000 mm.
2. Added three rectangular components with unique identifiers.
3. Enabled 90-degree rotation.
4. Executed Rectpack's packing algorithm.
5. Extracted successfully packed component identifiers.
6. Identified components that could not be placed.
7. Calculated total occupied area, material utilisation and unused area percentage.
8. Checked whether every requested component had been packed.

Two scenarios were tested, with different dimensions for Part C.

### Experimental Results

| Metric | Scenario A | Scenario B |
|---|---|---|
| Steel plate | 5000 × 4000 mm | 5000 × 4000 mm |
| Part A | 3000 × 2000 mm | 3000 × 2000 mm |
| Part B | 1500 × 1000 mm | 1500 × 1000 mm |
| Part C | 6000 × 1000 mm | 2000 × 1000 mm |
| Parts requested | 3 | 3 |
| Parts packed | 2 | 3 |
| Unpacked parts | C | None |
| Used area | 7,500,000 mm² | 9,500,000 mm² |
| Material utilisation | 37.5% | 47.5% |
| Unused area | 62.5% | 52.5% |
| Order completed geometrically | No | Yes |

### Interpretation

In Scenario A, Rectpack successfully accommodated two of the three requested components. Part C could not fit within the available plate because one of its dimensions exceeded the corresponding plate dimension in either permitted orientation.

In Scenario B, Part C was reduced to 2,000 × 1,000 mm. Rectpack successfully accommodated all three components, producing 47.5% material utilisation.

The results demonstrate that Rectpack can produce rectangular packing arrangements and provide geometric placement information that can be processed using Python.

However, the higher utilisation in Scenario B does not demonstrate that the algorithm performed better. The component dimensions changed between experiments, meaning the optimisation problems were different.

### Current Limitations

This preliminary prototype does not yet incorporate:

- Steel grade or thickness compatibility.
- Mill certificate and heat/batch traceability.
- Cutting kerf and required spacing between parts.
- Machine-specific cutting constraints.
- Irregular-shaped components.
- Reusable offcut inventory.
- Material costs, job priorities or production deadlines.

Material utilisation represents the proportion of plate area occupied by packed components. The remaining area should not automatically be classified as scrap because some material may be reusable.

Furthermore, successfully packing all components geometrically does not guarantee that the resulting cutting plan is suitable for production.

### Preliminary Conclusion

Rectpack appears to be a useful starting point for rectangular 2D packing experiments.

The prototype demonstrates basic rectangle placement, material utilisation calculations and detection of unpacked components.

Further investigation is required to determine how Rectpack could be integrated with GoSmarter's manufacturing-specific requirements, and whether alternative optimisation approaches offer advantages for more complex cutting and production-planning problems.

### Recommended Next Steps

1. Compare alternative packing algorithms using identical input data.
2. Evaluate performance using utilisation, runtime and successful component placement.
3. Investigate how cutting clearances and material compatibility could be incorporated.
4. Compare Rectpack with other open-source optimisation tools.
5. Assess requirements for integration with GoSmarter's inventory and traceability workflows.
