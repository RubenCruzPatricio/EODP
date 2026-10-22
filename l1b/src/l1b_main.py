
# LEVEL-1B MODULE

from l1b.src.initL1b import initL1b
from common.io.writeToa import writeToa, readToa
from common.src.auxFunc import getIndexBand
from common.io.readFactor import readFactor, EQ_MULT, EQ_ADD, NC_EXT
import numpy as np
import os
import matplotlib.pyplot as plt

class l1b(initL1b):

    def __init__(self, auxdir, indir, outdir):
        super().__init__(auxdir, indir, outdir)

    def processModule(self):

        self.logger.info("Start of the L1B Processing Module")

        for band in self.globalConfig.bands:

            self.logger.info("Start of BAND " + band)

            # Read TOA - output of the ISM in Digital Numbers
            # -------------------------------------------------------------------------------
            toa = readToa(self.indir, self.globalConfig.ism_toa + band + '.nc')
            gain = self.l1bConfig.gain[getIndexBand(band)]
            toa_noeq = self.restoration(toa, gain)

            # Equalization (radiometric correction)
            # -------------------------------------------------------------------------------
            if self.l1bConfig.do_equalization:
                self.logger.info("EODP-ALG-L1B-1010: Radiometric Correction (equalization)")

                # Read the multiplicative and additive factors from auxiliary/equalization/
                eq_mult = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_mult+band+NC_EXT),EQ_MULT)
                eq_add = readFactor(os.path.join(self.auxdir,self.l1bConfig.eq_add+band+NC_EXT),EQ_ADD)

                # Do the equalization and save to file
                toa = self.equalization(toa, eq_add, eq_mult)
                writeToa(self.outdir, self.globalConfig.l1b_toa_eq + band, toa)

            # Restitution (absolute radiometric gain)
            # -------------------------------------------------------------------------------
            self.logger.info("EODP-ALG-L1B-1020: Absolute radiometric gain application (restoration)")
            toa = self.restoration(toa, self.l1bConfig.gain[getIndexBand(band)])

            # Write output TOA
            # -------------------------------------------------------------------------------
            writeToa(self.outdir, self.globalConfig.l1b_toa + band, toa)
            toa_isrf = readToa(self.indir, 'ism_toa_isrf_' + band + '.nc')  # truth
            self.plotL1bToa(toa, toa_noeq, toa_isrf, self.outdir, band)

            self.logger.info("End of BAND " + band)

        self.logger.info("End of the L1B Module!")


    def equalization(self, toa, eq_add, eq_mult):
        """
        Equlization. Apply an offset and a gain.
        :param toa: TOA in DN
        :param eq_add: Offset in DN
        :param eq_mult: Gain factor, adimensional
        :return: TOA in DN, equalized
        """

        toa_out = np.zeros(toa.shape)
        for ialt in range(toa.shape[0]):
            toa_out[ialt, :] = (toa[ialt, :] - eq_add) / eq_mult

        return toa_out

    def restoration(self,toa,gain):
        """
        Absolute Radiometric Gain - restore back to radiances
        :param toa: TOA in DN
        :param gain: gain in [rad/DN]
        :return: TOA in radiances [mW/sr/m2]
        """

        toa= toa*gain
        self.logger.debug('Sanity check. TOA in radiances after gain application ' + str(toa[1,-1]) + ' [mW/m2/sr]')

        return toa

    def plotL1bToa(self, toa_eq, toa_noeq, toa_isrf, outputdir, band):
        mid = int(toa_eq.shape[0] / 2)
        fig, ax = plt.subplots()
        ax.plot(toa_noeq[mid, :], label='Non-equalised')
        ax.plot(toa_eq[mid, :], 'k', label='Equalised')
        ax.plot(toa_isrf[mid, :], 'r--', label='Truth (ism_toa_isrf)')
        ax.set_title(band)
        ax.set_xlabel('Across Track [-]')
        ax.set_ylabel('TOA [mW/m2/sr]')
        ax.grid(True)
        ax.legend()
        os.makedirs(outputdir, exist_ok=True)
        fig.savefig(os.path.join(outputdir, 'l1b_toa_' + band + '_graph.png'), dpi=200)
        plt.close(fig)