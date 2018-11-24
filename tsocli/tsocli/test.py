import fixed_constraint
import observation_block
import dynamic_constraint


dConstraint = dynamic_constraint.DynamicConstraint(2590, 2)
print("Dynamic Constraint: ", dConstraint.weight, dConstraint.confidence)

fConstraint = fixed_constraint.FixedConstraint(22, 22.0)
print("fixed constraint: ", fConstraint.weight, fConstraint.timeHorizon)

constraints = [fConstraint, dConstraint]

block = observation_block.ObservationBlock(22, "Kirk", 10, 0.0001, constraints, 200) 
print("Observation block: ", block.researcher_name, block.priority, block.coordinates, block.constraints, block.duration)
