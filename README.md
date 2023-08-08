# OCT-Stripes-Removal
Optical coherence tomography(OCT) imagining is one of the techniques used in biomedical engineering to obtain accurate images of microvascular activities. The images are high resolution cross-sectional images. In our case, OCT enables in finding volumetric morphological visualization of tissue. However, such a method produces noises in the image making it harder to interpret and analyze, and which produces errors in the results. These noises are resulted from the strong scattering property of erythrocytes
within overlying vasculature.
To tackle this problem, a post-processing computing technique was proposed. It accurately eliminates stripes noise produced in the image through machine learning algorithm. Many algorithms have been developed to deionize and destripe, however, most of them impact the signaling of the image, and the brightness of the image will be impacted, thus impact the result of the experiment. The algorithm developed in this paper is multidirectional removal. It includes a contrast enhancer using an image processing library in python called OpenCV. 
