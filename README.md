# nasa-apps-challenge
This is the public repo for the X Æ A-12 team's project for the NASA Apps Challenge 
Team members: Jamie Staeben, Kiran Devine, Sophie Lowen, Daniel Getter

#### Project Summary
We used space imagery data of the Earth at night in conjunction with data about human mobility to develop a prototype model to help predict possible outbreaks. By comparing these data against trends in COVID-19 cases, we were able to identify high light pollution, high mobility, and poor social distancing practices as risk factors for spreading disease. Our model can be applied to determine where outbreaks are likely to occur, which can accelerate the process of delivering aid to these areas and enable leadership to better control the outbreak.

#### What is h5_parser.py
h5_parser.py is a python program that takes in HDF5 data files from the VIIRS/NPP Daily Gridded Day Night Band 500m Linear Lat Lon Grid Night (short-name is VNP46A1) and analyzes the brightness temperature data set.

#### How to use h5_parser.py
Syntax: `python3 h5_parser.py [True/False]`
 - True = Save images and GIF
 - False = Don't save images and GIF
       
Output: 
- If you select False for saving images and GIF:
  - Total Brightness Temperature for each data file
  - Time elapsed for that calculation
  - Full list of Dates and the corresponding Brightness Temperature
  - Saves plot of Date vs. Brightness Temperature into the BrightTempImages directory  
- If you select True for saving images and GIF:
  - Everything from the above section
  - Images and GIF saved into the BrightTempImages directory  '
