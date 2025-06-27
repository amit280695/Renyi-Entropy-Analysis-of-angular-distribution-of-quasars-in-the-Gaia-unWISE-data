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

Code 3 - (masking_3.ipynb)

Here, we apply a circular mask centered at l = 0 and b = 0 and subtending a solid angle of 4 sr in addition to the mask applied in code 2.
For each quasar sample, we save both the masked data and the indices of the populated pixels at NSIDE = 8.
Any analysis using this masked dataset must be performed at NSIDE = 8.


After completing Step 1, we obtain two versions of masked data and corresponding populated pixel indices for each of the three quasar samples.

##################################################################################################################################################################################################


Step - 2

Folder name: - renyi_entropy

Code 1 -  (renyi_data.ipynb)

This code calculates the Renyi entropy of orders 1 to 5.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat'
              

If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 2 -  (renyi_random.ipynb)

This code calculates the Renyi entropy of orders 1 to 5 for randomized masked quasar samples.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat'
              
If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 3 - (plot.ipynb)

This code produces Figure 4 in the paper by combining the results of codes 1 and 2.


In Step 2, we perform the full Renyi entropy calculation for all two masking cases: Maskings 1 and 2 with NSIDE = 8. The necessary inputs for Mask 2 are already included in the code as commented lines; these can be uncommented one by one to obtain the output for each masking as needed. 


##################################################################################################################################################################################################



Step - 3

Folder name: - entropy_dispersion

Code 1 -  (entropy_disp_data.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the three quasar samples.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat'
              
If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 2 -  (entropy_disp_rand.ipynb)

This code calculates the normalized entropy dispersion of orders 1 through 5 for the randomized versions of the three quasar samples after.

In this code  
1. f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat'

2. f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat'
              
If line 1 is uncommented along with setting NSIDE = 8, the code produces results for Masking 1. Similarly, uncommenting line 2 with NSIDE = 8 gives results for Masking 2. 

Code 3 - (plot.ipynb)

This code produces Figure 5 in the paper by combining the results of codes 1 and 2.


