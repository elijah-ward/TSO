from src.tso.observation import fixed_constraint, observation_block, dynamic_constraint
from src.tso.importer import transformer

from astropy import units as u
from astropy.coordinates import SkyCoord


dConstraint = dynamic_constraint.DynamicConstraint(2590, 2)
print("Dynamic Constraint: ", dConstraint.weight, dConstraint.confidence)

fConstraint = fixed_constraint.FixedConstraint(22, 22.0)
print("fixed constraint: ", fConstraint.weight, fConstraint.timeHorizon)

constraints = [fConstraint, dConstraint]
c = SkyCoord(
    ra=10.625*u.degree,
    dec=41.2*u.degree,
    frame='icrs'
)

block = observation_block.ObservationBlock(22, "Kirk", 10, c, constraints)
print("Observation block: ", block.researcher_name, block.priority, block.coordinates, block.constraints[0].type, block.constraints[1].type)

newBlock = transformer.transform("testing")
print("New Block, researcher name: ", newBlock.researcher_name)
