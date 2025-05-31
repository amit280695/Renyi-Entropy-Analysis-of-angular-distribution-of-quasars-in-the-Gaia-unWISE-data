Link for downloading data - https://zenodo.org/records/10403370
You can download quaia_G20.0.fits and quaia_G20.5.fits.
These two files contain the Quaia Quasar catalog, having two different apparent magnitude (G-band) cuts. In our analysis we use quaia_G20.0.fits .

Step - 1 

Folder name : - data_prep

Code 1 -  (data_prep.ipynb)
In this code, we divide the entire quasar distribution data to three different samples having different redshift ranges. 

Code 2 - (masking_1.ipynb)

In this code, we apply masking on these three different samples.
First, we apply a Galactic latitude mask. Then, for each pixel at NSIDE 8, we examine its corresponding 64 subpixels at NSIDE 64 and retain only those NSIDE 8 pixels for which more than 90% of the sub pixels are filled. In this way we produce a cleaner sample.

Code 3 - (masking_2.ipynb)

Same goal like Code 2, aim to create cleaner samples. Here, we apply a circular mask centered at l = 0 and b = 0 and subtending a solid angle of 4 sr in addition to the mask applied in the code 2.

Code 4 - (masking_3.ipynb)

In this code we use different masking criteria. Here we apply only the galactic latitude mask.

Code 4 - (masking_4.ipynb)

In this code we choose different masking criteria. First, we apply a Galactic latitude mask. In addition to this we apply a circular mask centered at l = 0 and b = 0 and subtending a solid angle of 4 sr.


Thus we create four sets of masked versions for all the three quasar samples.
