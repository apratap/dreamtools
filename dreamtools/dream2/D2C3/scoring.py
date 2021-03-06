"""D2C3 scoring functions

:Title: DREAM2 - Synthetic Five-Gene Network Inference
:Nickname: D2C3
:Summary: Infer a gene regulation network from qPCR and microarray measurements
:SubChallenges: 
:Synapse page: https://www.synapse.org/#!Synapse:syn3034869

The original algorithm was developed in MATLAB by Gustavo Stolovitzky
"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
from dreamtools.core.rocs import D3D4ROC, DREAM2


class D2C3(Challenge, D3D4ROC, DREAM2):
    """A class dedicated to D2C3 challenge


    ::

        from dreamtools import D2C3
        s = D2C3()
        filename = s.download_template() 
        s.score(filename) 

    There are 12 gold standards and therefore 12 possible submissions.
    6 for the chip case and 6 for the qPCR. Those should be scored independently.
    THere is no sub-challenge per se. 

    This class works for the DIRECTED-SIGNED_EXCITATORY_chip case only but implementation
    for other cases is straightforward.

    """
    def __init__(self):
        """.. rubric:: constructor"""
        super(D2C3, self).__init__('D2C3')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()

        # although there is no sub challenges per se,
        # 12 different GS were used to score 12 types
        # of network. We use those TAGS 
        #: sub challenges
        self.sub_challenges = [
            "DIRECTED-SIGNED_EXCITATORY_chip",
            "DIRECTED-SIGNED_EXCITATORY_qPCR",
            "DIRECTED-SIGNED_INHIBITORY_chip",
            "DIRECTED-SIGNED_INHIBITORY_qPCR",
            "DIRECTED-UNSIGNED_chip",
            "DIRECTED-UNSIGNED_qPCR",
            "UNDIRECTED-SIGNED_EXCITATORY_chip",
            "UNDIRECTED-SIGNED_EXCITATORY_qPCR",
            "UNDIRECTED-SIGNED_INHIBITORY_chip",
            "UNDIRECTED-SIGNED_INHIBITORY_qPCR",
            "UNDIRECTED-UNSIGNED_chip",
            "UNDIRECTED-UNSIGNED_qPCR"]

    def _init(self):
        # should download files from synapse if required.
        pass

    def download_goldstandard(self, subname=None):
        """Returns one of the 12 gold standard file

        :param subname: one of the sub challenge name. See :attr:`sub_challenges`
        """
        self._check_subname(subname)
        gold = self._pj([self._path2data, 'goldstandard', 
            'D2C3_goldstandard_%s.txt' % subname])
        return gold

    def download_template(self, subname=None):
        self._check_subname(subname)
        filename = 'D2C3_templates_%s.txt' % subname
        return self._pj([self._path2data, 'templates', filename])

    def score(self, filename, subname=None, goldstandard=None):
        if goldstandard is None:
            goldstandard = self.download_goldstandard(subname)

        self.gold_edges =  pd.read_csv(goldstandard, sep='\t', header=None)
        self.prediction =  pd.read_csv(filename, sep='\t', header=None)
        newtest = pd.merge(self.prediction, self.gold_edges, how='inner', on=[0,1])

        test = list(newtest['2_x'])
        gold_index = list(newtest['2_y'])

        AUC, AUROC, prec, rec, tpr, fpr = self.get_statistics(self.gold_edges, 
            self.prediction, gold_index)

        P = self.gold_edges[2].sum()
        spec_prec = self.compute_specific_precision_values(P, rec)

        # for plotting
        self.metrics = {'AUPR':AUC, 'AUROC':AUROC ,
            'tpr':  tpr, 'fpr':  fpr,
            'rec':  rec, 'prec':  prec,
            'precision at nth correct prediction': spec_prec}

        results = {'AUPR':AUC, 'AUROC':AUROC }
        results['precision at nth correct prediction'] =spec_prec
        return results

