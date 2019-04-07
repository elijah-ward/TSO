class CFHTObservationBlock:
    """
    CFHTObservationBlock

    Represents entities in the observation_block table of the CFHT database
    """

    def __init__(
        self,
        **properties
    ):
        self.observation_block_id = properties.get('id', -1)
        self.token = properties.get('token', -1)
        self.observing_groups_id = properties.get('observing_groups_id', -1)
        self.observing_block_data = properties.get('observing_block_data', -1)
        self.candidate = properties.get('candidate', -1)
        self.sky_address = properties.get('sky_address', -1)
        self.public = properties.get('public', -1)
        self.active_runid = properties.get('active_runid', -1)
        self.min_qrun_millis = properties.get('min_qrun_millis', -1)
        self.max_qrun_millis = properties.get('max_qrun_millis', -1)
        self.contiguous_exposure_time_millis = properties.get('contiguous_exposure_time_millis', -1)
        self.priority = properties.get('priority', -1)
        self.next_observable_at = properties.get('next_observable_at', -1)
        self.unobservable_at = properties.get('unobservable_at', -1)
        self.remaining_observing_chances = properties.get('remaining_observing_chances', -1)
        self.created_at = properties.get('created_at', -1)
        self.updated_at = properties.get('updated_at', -1)
        self.dirty = properties.get('dirty', -1)
        self.version = properties.get('version', -1)
        self.label = properties.get('label', -1)
        self.program_id = properties.get('program_id', -1)

        self.exposure_count = -1
