# 3-parts-of-a-line-for-3D-Slicer
3D Slicer Segment Divider for Morphoanatomical Analysis
This Python script is designed for 3D Slicer to facilitate morphoanatomical and radiological studies. It was specifically developed for the systematic characterization of vascular structures in relation to vertebral levels.
Overview
The script automates the process of dividing anatomical landmarks (lines) into equal segments. In the context of lumbar artery research, it allows for the precise mapping of arterial origins relative to the upper, middle, and lower thirds of vertebral bodies.
Key Features
Automated Segmentation: Automatically detects all vtkMRMLMarkupsLineNode objects in the scene.
Equal Division: Calculates and marks the 1/3 and 2/3 points of each line.
Visual Coding:
Green Points: Represent the start and end of the original line.
Red Points: Represent the calculated division points for anatomical segmentation.
Batch Processing: Processes all active lines simultaneously, ensuring consistency and saving time during large-scale cohort analyses.
How to Use
Open 3D Slicer (v.5.8.1 or higher is recommended).
Create your line markups (e.g., spanning a vertebral body from the superior to the inferior plate).
Open the Python Interactor (Ctrl + g).
Copy and paste the code from slicer_divider.py into the interactor and press Enter.
A new Fiducial Node named DividedPoints_... will be created with the segmented points.
## Citation
If you use this script in your research, please cite the following study:
* **Talan, A. T.** "Morphoanatomical Analysis of Lumbar Arteries Using Computed Tomography Angiography: A Retrospective, Cross-Sectional Study" (2026).
