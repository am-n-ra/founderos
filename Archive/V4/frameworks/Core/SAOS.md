# SAOS — Systems Analysis Operating System

## When to Use This Lens

Design, audit, or debug of a system (architecture, project, workflow, organization).

## Required Questions

1. What are the components of the system?
2. What are the dependencies between components?
3. What is the boundary of each component?
4. What truth does each component own?
5. What truth does each component NOT own?
6. What is the single bottleneck?
7. What breaks if you remove X?
8. What is the single source of truth for each data?
9. Can the component be rebuilt if lost?
10. What is the cost of removing it?

## Principles

- A healthy system has clear boundaries between its components.
- Each component owns ONE truth and ONE only.
- The bottleneck is the single constraint that limits the entire system.
- A component that can be easily rebuilt has less value than one that cannot.
- Separation of responsibilities is the first defense against entropy.

## Analysis Steps

1. Map all components and their boundaries
2. Identify the truths each component owns
3. Trace dependencies between components
4. Find the bottleneck (the component that limits system throughput)
5. Test resilience: mentally remove each component and evaluate the impact
6. Verify Rule 0: each truth has exactly one owner

## Anti-patterns

- Components that own the same truth → duplication, contradiction
- Components without clear boundaries → inconsistency
- Components without their own truth → dead, useless
- System without an identified bottleneck → impossible to prioritize
- Adding components without checking boundaries against existing ones
