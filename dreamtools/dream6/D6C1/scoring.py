"""

scoring author: bobby prill
"""
import os
from dreamtools.core.challenge import Challenge


class D6C1(Challenge):
    """A class dedicated to D6C1 challenge


    ::

        from dreamtools import D6C1
        s = D6C1()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D6C1, self).__init__('D6C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        # should return full path to a template file
        raise NotImplementedError

    def download_goldstandard(self):
        # should return full path to a gold standard file
        raise NotImplementedError
