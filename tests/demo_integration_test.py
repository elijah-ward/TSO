from src.tso.observation import fixed_constraint, observation_request, dynamic_constraint
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

        c = (123, 123) # Overriding above definition -- this is the new way of defining coordinates??

        block = observation_request.ObservationRequest(
            22, c, 123, 123, 123, 123
        )

        print(
            "Obsevation block: ",
            block
        )

        new_block = transformer.transform("testing")
