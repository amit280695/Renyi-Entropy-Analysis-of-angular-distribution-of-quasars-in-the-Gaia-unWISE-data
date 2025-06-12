Link for downloading data - https://zenodo.org/records/10403370

You can download quaia_G20.0.fits and quaia_G20.5.fits.
These two files contain the Quaia Quasar catalog, having two different apparent magnitude (G-band) cuts. In our analysis, we use quaia_G20.0.fits.

Step - 1 

Download quaia_G20.0.fits data and keep it in the folder data_prep.


Folder name: - data_prep

Code 1 -  (data_prep.ipynb)
In this code, we divide the entire quasar distribution data into three different samples having different redshift ranges. 

Code 2 - (masking_1.ipynb)

In this code, we apply a masking procedure to three different quasar samples. First, we apply a Galactic latitude cut. Then, for each NSIDE = 8 pixel, we examine its 64 corresponding subpixels at NSIDE = 64. We retain only those NSIDE = 8 pixels where more than 90% of the subpixels are populated. This results in a cleaner and more reliable sample.
For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 8.
Any analysis using this masked dataset must be performed at NSIDE = 8.

Code 3 - (masking_2.ipynb)

Here, we apply a circular mask centered at l = 0 and b = 0 and subtending a solid angle of 4 sr in addition to the mask applied in code 2.
For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 8.
Any analysis using this masked dataset must be performed at NSIDE = 8.

Code 4 - (masking_3.ipynb)

In this code, we use different masking criteria. Here we apply only the galactic latitude mask. For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 64.
Any analysis using this masked dataset must be performed at NSIDE = 64.


Code 5 - (masking_4.ipynb)

In this code, we apply multiple masking criteria. First, a Galactic latitude mask is used. Additionally, we apply a circular mask centered at Galactic coordinates l=0 degree, b=0 degree, covering a solid angle of 4 steradians.
For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 64. Any analysis using this masked dataset must be performed at NSIDE = 64.


After completing Step 1, we obtain four versions of masked data and corresponding populated pixel indices for each of the three quasar samples.
###################################################################################################################################################################################################


Step - 2

Folder name: - renyi_entropy_mask_1

Code 1 -  (renyi_data.ipynb)

This code calculates the Renyi entropy of orders 1 through 5 for the three quasar samples after applying mask 1.


Code 2 -  (renyi_random.ipynb)

This code calculates the Renyi entropy of orders 1 through 5 for the randomized versions of the three quasar samples after applying mask 1.



Step - 3

Folder name : - entropy_dispersion_mask_1

Code 1 -  (entropy_disp_data.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the three quasar samples after applying mask 1.


Code 2 -  (entropy_disp_rand.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the randomized versions of the three quasar samples after applying mask 1.


