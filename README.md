Link for downloading data - https://zenodo.org/records/10403370

You can download quaia_G20.0.fits and quaia_G20.5.fits.
These two files contain the Gaia-unWISE Quasar catalog, having two different apparent magnitude (G-band) cuts. quaia_G20.0.fits is limited to magnitude G < 20.0, which is considered a cleaner sample. And quaia_G20.5.fits is limited to magnitude G < 20.5. We use the G < 20.0 quasar sample in our analysis, so we download quaia_G20.0.fits file.

Step - 1 

Folder name: - data_prep

Download quaia_G20.0.fits data and keep it in the folder data_prep.


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

Actually, we want to analyze the mask 1 data for all three quasar samples with different nside of 64. Here we have to prepare a separate masking data set because we don't have to apply the completeness criteria, as the pixel area of each pixel in nside = 64 is (1/64) times the area of each pixel in nside = 8.
In this code, we apply only a Galactic latitude cut. For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 64.

Any analysis using this masked dataset must be performed at NSIDE = 64.

Code 5 - (masking_4.ipynb)

Actually, we want to analyze the mask 2 data for all three quasar samples with a different nside of 64. Here we have to prepare a separate masking data set because we don't have to apply the completeness criteria as the pixel area of each pixel in nside = 64 is (1/64) times the area of each pixel in nside = 8.

Here, we apply a Galactic latitude cut and circular mask centered at l = 0 and b = 0 and subtending a solid angle of 4 sr in addition to the mask applied in code 4.
For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 64.
Any analysis using this masked dataset must be performed at NSIDE = 64.



After completing Step 1, we obtain four versions of masked data and corresponding populated pixel indices for each of the three quasar samples.

##################################################################################################################################################################################################


Step - 2

Folder name: - renyi_entropy

Code 1 -  (renyi_data.ipynb)

This code calculates the Renyi entropy of orders 1 to 5 for different masked versions.

To calculate the Rényi entropy of orders 1 to 5 for a specific masking configuration, uncomment the corresponding input file line (f_in) and assign the appropriate NSIDE value:

Masking 1: Uncomment f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 2: Uncomment f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 3: Uncomment f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64

Masking 4: Uncomment f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64

Choose the appropriate combination based on which masking configuration you want to analyze.
 

Code 2 -  (renyi_random.ipynb)

This code calculates the Rényi entropy of orders 1 to 5 for randomized, masked quasar samples.

To use a specific masking configuration, uncomment the corresponding input file lines for f_in and f1, and set the appropriate NSIDE value as follows:

For Masking 1, uncomment: f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 2, uncomment: f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 3, uncomment: f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask3/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

For Masking 4, uncomment: f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask4/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

Choose the appropriate combination depending on the masking setup you wish to analyze.

Code 3 - (plot.ipynb)

This code produces the figure, which shows the variation of Renyi entropy with comoving radial distance for different entropy orders, 1 to 5, for all three masked quasar samples and their randomized versions.


##################################################################################################################################################################################################



Step - 3

Folder name: - entropy_dispersion

Code 1 -  (entropy_disp_data.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the three quasar samples.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat'

3. f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat'

4. f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat'

              
If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 2 -  (entropy_disp_rand.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the randomized versions of the three quasar samples after.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat'

3. f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask3/non_zero_pix_id_' + str(k+1) + '.dat'

4. f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask4/non_zero_pix_id_' + str(k+1) + '.dat'
              
If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 3 - (plot.ipynb)

This code produces Figure ... in the paper by combining the results of codes 1 and 2.


