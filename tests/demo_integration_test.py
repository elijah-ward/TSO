from src.tso.observation import fixed_constraint, observation_block, dynamic_constraint
from src.tso.importer import transformer

from astropy import units as u
from astropy.coordinates import SkyCoord


class TestDemoIntegration:

    def test_observation_and_transform(self):
        d_constraint = dynamic_constraint.DynamicConstraint(2590, 2)
        print("Dynamic Constraint: ", d_constraint.weight, d_constraint.confidence)

        f_constraint = fixed_constraint.FixedConstraint(22, 22.0)
        print("fixed constraint: ", f_constraint.weight, f_constraint.timeHorizon)

        constraints = [f_constraint, d_constraint]
        c = SkyCoord(
            ra=10.625*u.degree,
            dec=41.2*u.degree,
            frame='icrs'
        )

        block = observation_block.ObservationBlock(22, "Kirk", 10, c, constraints)
        print(
            "Observation block: ",
            block.researcher_name,
            block.priority,
            block.coordinates,
            block.constraints[0].type,
            block.constraints[1].type
        )

        new_block = transformer.transform("testing")
        print("New Block, researcher name: ", new_block.researcher_name)
