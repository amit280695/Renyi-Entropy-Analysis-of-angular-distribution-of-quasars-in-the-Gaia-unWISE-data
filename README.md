# Renyi Entropy Analysis of angular distribution of quasars in the Gaia-unWISE data

This repository contains the full set of codes used in our analysis of large-scale anisotropy in the angular distribution of quasars from the Gaia-unWISE catalogue. The results are presented in our paper "Revealing a transitional epoch of large-scale cosmic anisotropy in the quasar Distribution" (arXiv:2507.02835)

Data Access:
The Gaia-unWISE quasar catalogue is publicly available on Zenodo: https://zenodo.org/records/10403370

You can download two versions of the Gaia–unWISE quasar catalogue: quaia_G20.0.fits and quaia_G20.5.fits, corresponding to apparent magnitude cuts of G<20.0 and G<20.5, respectively. The G<20.0 sample (quaia_G20.0.fits) offers higher purity and is used throughout our analysis.

Please place the downloaded file in the data_prep/ directory before proceeding.

Step - 1 

Folder name: - data_prep

Code 1 -  (data_prep.ipynb)
This code divides the full quasar dataset into three separate samples, each corresponding to a different redshift range as defined in Table-I of the article.

Code 2 - (masking_1.ipynb)

This code applies a masking procedure to each of the three quasar samples. This is labelled as Mask 1 in our analysis. It first imposes a Galactic latitude cut, then evaluates the completeness of each NSIDE = 8 pixel by checking its corresponding subpixels at NSIDE = 64. Pixels are retained only if more than 90% of their subpixels contain quasars, ensuring a cleaner and more reliable dataset. For each sample, the script saves both the masked data and the indices of the populated NSIDE = 8 pixels.

All subsequent analyses using this masked dataset should be performed at NSIDE = 8. 

Code 3 - (masking_2.ipynb)

This code applies an additional circular mask centered at l=0 degree, b=0 degree, covering a solid angle of 4 steradian, on top of the masking procedure described in Code 2.  This is labelled as Mask 2 in our analysis. For each quasar sample, it outputs the masked dataset along with the indices of the populated NSIDE = 8 pixels.

All subsequent analyses using this masked dataset should be conducted at NSIDE = 8.

Code 4 - (masking_3.ipynb)

This code prepares a version of the Mask 1 dataset for all three quasar samples at a higher HEALPix resolution of NSIDE = 64. At this resolution, each pixel covers (1/64)^th the area of a pixel at NSIDE = 8, making subpixel completeness checks unnecessary. Therefore, we apply only a Galactic latitude cut without additional completeness filtering. For each sample, the script outputs the masked data and the corresponding populated pixel indices at NSIDE = 64.

All subsequent analyses using this masked dataset should be conducted at NSIDE = 64.

Code 5 - (masking_4.ipynb)

This code generates a high-resolution version of the Mask 2 dataset for all three quasar samples at NSIDE = 64. At this resolution, each pixel has (1/64)^th the area of a pixel at NSIDE = 8, so no subpixel completeness criterion is applied. The masking includes both a Galactic latitude cut and a circular exclusion region centered at l=0 degree, b=0 degree, covering a solid angle of 4 steradian, in line with the masking procedure used in Code 3. For each sample, the script saves the masked data along with the indices of the populated NSIDE = 64 pixels.

All subsequent analyses using this dataset should be performed at NSIDE = 64.

Upon completing Step 1, you will have four masked versions each corresponding to a different masking scheme along with the associated populated pixel indices for all three quasar samples.

##################################################################################################################################################################################################


Step - 2

Folder name: - renyi_entropy

Code 1 -  (renyi_data.ipynb)

This code calculates the Renyi entropy of orders 1 to 5 for different masked versions.

To calculate the Renyi entropy of orders 1 to 5 for a specific masking configuration, uncomment the corresponding input file line (f_in) and assign the appropriate NSIDE value:

Masking 1: Uncomment f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 2: Uncomment f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 3: Uncomment f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64

Masking 4: Uncomment f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64

Choose the appropriate combination based on which masking configuration you want to analyze.
 

Code 2 -  (renyi_random.ipynb)

This code calculates the Renyi entropy of orders 1 to 5 for randomized, masked quasar samples.

To use a specific masking configuration, uncomment the corresponding input file lines for f_in and f1, and set the appropriate NSIDE value as follows:

For Masking 1, uncomment: f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 2, uncomment: f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 3, uncomment: f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask3/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

For Masking 4, uncomment: f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask4/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

Choose the appropriate combination depending on the masking setup you wish to analyze.

Code 3 - (plot.ipynb)

This code produces the figure, which shows the variation of Renyi entropy with comoving radial distance for different entropy orders, 1 to 5, for all three masked quasar samples and their randomized versions.


#########################################################################################################################################################################################################



Step - 3

Folder name: - entropy_dispersion

Code 1 -  (entropy_disp_data.ipynb)

This code calculates the normalized entropy dispersion of orders 1 to 5 for the three quasar samples.

To calculate the normalized entropy dispersion of orders 1 through 5 for a specific masking configuration, uncomment the corresponding input file line (f_in) and assign the appropriate NSIDE value:

Masking 1: Uncomment f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 2: Uncomment f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 8

Masking 3: Uncomment f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64

Masking 4: Uncomment f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and use NSIDE = 64


Code 2 -  (entropy_disp_rand.ipynb)

This code calculates the normalized entropy dispersion of orders 1 to 5 for the randomized versions of the three quasar samples after.

To use a specific masking configuration, uncomment the corresponding input file lines for f_in and f1, and set the appropriate NSIDE value as follows:

For Masking 1, uncomment: f_in = '../data_prep/mask1/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask1/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 2, uncomment: f_in = '../data_prep/mask2/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask2/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 8

For Masking 3, uncomment: f_in = '../data_prep/mask3/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask3/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

For Masking 4, uncomment: f_in = '../data_prep/mask4/masked_sample_' + str(n+1) + '.dat' and f1 = '../data_prep/mask4/non_zero_pix_id_' + str(k+1) + '.dat' and use NSIDE = 64

Choose the appropriate combination depending on the masking setup you wish to analyze.


Code 3 - (plot.ipynb)

This code produces the figure, which shows the mean normalized entropy dispersion as a function of comoving radial distance and the significance ratio as a function of comoving radial distance.

#############################################################################################################################################################################################################

Step - 4

Folder name: - conv_norm_entr_disp

Code - (conv_entropy_dispersion_rand.ipynb)

This code evaluates the convergence of the normalized entropy dispersion across random mock samples to determine how many mocks are sufficient for a reliable analysis.


########################################################################################################################################################################################

Required Python Packages - 
These codes require the following Python packages, all of which are available in the Anaconda distribution: numpy, pandas, matplotlib, healpy, astropy, scipy

If you are using Anaconda, these can be installed (if not already available) via: conda install numpy pandas matplotlib healpy astropy scipy

Alternatively, if you are using pip: pip install numpy pandas matplotlib healpy astropy scipy
