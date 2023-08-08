# OCT-Stripes-Removal
## Introduction
Optical coherence tomography(OCT) imagining is one of the techniques used in biomedical engineering to obtain accurate images of microvascular activities. The images are high resolution cross-sectional images. In our case, OCT enables in finding volumetric morphological visualization of tissue. However, such a method produces noises in the image making it harder to interpret and analyze, and which produces errors in the results. These noises are resulted from the strong scattering property of erythrocytes
within overlying vasculature.
To tackle this problem, a post-processing computing technique was proposed. It accurately eliminates stripes noise produced in the image through machine learning algorithm. Many algorithms have been developed to deionize and destripe, however, most of them impact the signaling of the image, and the brightness of the image will be impacted, thus impact the result of the experiment. The algorithm developed in this paper is multidirectional removal. It includes a contrast enhancer using an image processing library in python called OpenCV. 
## Methodology
* FFT modified itself depending on decomposition function of each sub-image.
* Decompose function go throw different layers. First it is decomposed into one low-pass sub-band layer, and five high-pass sub-band layer.
* Rotational invariance is one of the properties of FFT, if the image has rotated at an angle, its Fourier transform will also rotate the same angle. 
* Therefore, the stripe frequency coefficients will concentrate on a narrow frequency band
* This will reduce the contribution of these stripe artifacts. 
* For multidirectional LSFM, FFT filtering is repeated several times according to the angle number.
* At the end, the output image will go through an contrast enhancer technique implemented by OpenCV.
* The technique use the method ConvertScaleAbs, which computes absolute values and converts them to 8-bit.
* Two parameters will be set in the image, first parameter is alpha which is a scale factor for contrast control. Second parameter is beta, which is the brightness control.
* Alpha was set for 1.5 while beta for 0.
