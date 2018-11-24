import fixed_constraint
import observation_block
import dynamic_constraint
from astropy import units as u
from astropy.coordinates import SkyCoord
def transform(dataString):
	# convert string to observationBlock

	#------------------change--------------
	dConstraint = dynamic_constraint.DynamicConstraint(2590, 2)
	constraints = [dConstraint]
	c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
	tempBlock = observation_block.ObservationBlock(22, "Kirk", 10, c, constraints)
	#--------------------------------------
	return tempBlock