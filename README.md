# Working_BaseCode_Muon
fitter.py contains functions and parameters for these functions are set here
readhistogram.py is the main part of the code. It analyzes the AnalysisResults_combined_AllTrigger.root and produces histograms, fit the histograms, produce the angular distributions
editor.C and editormc.C are to correct the calculation of tildephi which was not properly calculation in initial analysisi file. The branch created with this analysis are accessed in readhistogram.py usring add friend. resulting trees are TildePhi.root and TildePhiMC.root
for the simultaneous fitting I used the Simone's simultaneous 1D fitting code.
Data_Comparison.xlsx excel sheet comparing yeilds from different bins phi, costheta and tildephi in both frame of reference
JPsi_Polarization.pptx is the slide with current result from the analysis.
