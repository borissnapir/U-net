# Example comes from https://docs.astropy.org/en/stable/api/astropy.modeling.physical_models.BlackBody.html?highlight=BlackBody

# Numerical stuff
import numpy as np

# Viz
import matplotlib.pyplot as plt

# Physics
from astropy.modeling.models import BlackBody
from astropy.visualization import quantity_support
from astropy.modeling import models
from astropy import units as u #https://docs.astropy.org/en/stable/units/

def get_astropy_bb(temp_deg):
    return models.BlackBody(temperature=(temp_deg*u.deg_C).to(
        u.K,equivalencies=u.temperature()))

# Define the whole range of wavelength
wav = np.arange(6000, 15000) * u.nm
wav_unit = wav.unit
temp_range = [5,15,25,40]
cm = plt.get_cmap('gist_rainbow')
colors = [cm(1. * i / len(temp_range)) for i in range(len(temp_range))]
hz_flux_unit=u.Joule/(u.cm**2 * u.Hertz * u.second * u.steradian)
nm_flux_unit=u.W/(u.cm**2 * u.nanometer * u.steradian)

# Also read reference sensor from file
lepton = np.recfromcsv("../../../data/lepton_10_15_25.csv")
lepton = np.array([list(i) for i in lepton])
lepton_wav = lepton[:,0]
lepton_response = lepton[:,1]

with quantity_support():
    fig, ax1 = plt.subplots(figsize=(16, 5))
    fig.suptitle("Black body spectral profile vs thermal camera response")
    ax1.set_xlabel("Wavelength $\lambda$ in nm")
    ax1.set_ylabel(f"Spectral radiance in {nm_flux_unit}")

    # Lepton response
    ax2 = ax1.twinx()
    ax2.plot(lepton_wav, lepton_response*100, color='black', label=f"Lepton")
    ax2.set_ylabel('Relative response of lepton camera in %', color='g')

    # Spectral density
    #ax2 = ax1.twinx()
    #ax2.set_ylabel(f"Flux in {nm_flux_unit}")

    for temp_c, color in zip(temp_range, colors):
        bb_astropy = get_astropy_bb(temp_c)
        flux_astropy = bb_astropy(wav)
        #ax1.plot(wav, flux_astropy.to(hz_flux_unit), color=color)
        ax1.plot(wav, flux_astropy.to(nm_flux_unit,
                                      equivalencies=u.spectral_density(wav)),
                 color=color, label=f"{temp_c:.1f} C$^\circ$")
        #ax1.axvline(bb_astropy.lambda_max.to(wav_unit,
        #                                     equivalencies=u.spectral()).value,
        #            color=color, )
        max_wav = bb_astropy.lambda_max.to(wav_unit, equivalencies=u.spectral())
        markerline, stemlines, baseline = ax1.stem([max_wav], [bb_astropy(max_wav).to(nm_flux_unit,
                                      equivalencies=u.spectral_density(max_wav))],use_line_collection=True)
        plt.setp(stemlines, 'color', color)
        plt.setp(markerline, 'color', color)

        #ax1.axvline(bb_astropy.nu_max.to(u.nm,
        #                         equivalencies=u.spectral()).value, ls='--',
        #            color=color)
    ax1.legend( loc="upper left") #bbox_to_anchor=(0.05,0.70),
    ax2.legend(loc="upper right") #bbox_to_anchor=(0.85,0.70),

plt.show()
