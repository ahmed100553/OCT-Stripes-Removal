# OCT-Stripes-Removal
## Introduction
Optical Coherence Tomography (OCT) imaging is a technique used in biomedical engineering to obtain accurate images of microvascular activities. These images are high-resolution, cross-sectional views. In our context, OCT facilitates the volumetric morphological visualization of tissue. However, this method often introduces noise into the images, complicating their interpretation and analysis, and potentially leading to errors in the results. This noise primarily results from the strong scattering properties of erythrocytes within the overlying vasculature. To address this issue, a post-processing computing technique was proposed. This technique effectively eliminates stripe noise in the images using a machine learning algorithm. Although many algorithms have been developed for denoising and destriping, most of them affect the image's signal quality and brightness, thereby impacting the experimental results. The algorithm presented in this paper employs multidirectional noise removal. It includes a contrast enhancer utilizing an image processing library in Python called OpenCV. 
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
