from astroplan import Constraint
import warnings
from astropy.time import Time
import numpy as np


class TsoOutageConstraint(Constraint):
    """
    Tso Outage Constraint

    This is a class representing a global constraint that will live if TSO users have configured any planned outages.
    This will be configured through a JSON config file and created through the constraint aggregator.
    """

    @staticmethod
    def default_outage_config():
        return {
        }

    def __init__(self, outage_config=None):
        self.outage_config = outage_config if outage_config is not None else TsoOutageConstraint.default_outage_config()
        for outage in self.outage_config.get('times', []):
            if "start" in outage and "end" in outage:
                print('NOTE: Scheduled outage is configured for the period of {} to {}'.format(outage.get("start"), outage.get("end")))

    def compute_constraint(self, times, observer, targets):
        """
        Implementation of the Constraint interface.
        The processing within this method will first determine those blocks that DO NOT fall within an outtage time.
        Those who do will return false for the given times input array.

        :param times: the times of the scheduling blocks
        :param observer: the observer object
        :param targets: the targets being observed
        :return: an array matching the dimensions of times that determines whether it is observable or not.
        """
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            min_time = Time("1950-01-01T00:00:00")
            max_time = Time("2120-01-01T00:00:00")

        masks = []
        for outage in self.outage_config.get('times', []):
            min_out_time = Time(outage.get("start", max_time))
            max_out_time = Time(outage.get("end", min_time))

            # if the time is OUTSIDE of the given range, it is valid
            masks.append(np.logical_not(np.logical_and(times > min_out_time, times < max_out_time)))

        masks__any = np.array(masks).all(axis=0)
        return masks__any
