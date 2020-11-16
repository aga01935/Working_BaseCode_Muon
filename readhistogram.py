#!/usr/bin/python
#include<stdio.h>
import code
import math
import cuts as ct
import ROOT as rt
import fitter as ft
from ROOT import TFile, TTree, TCanvas, TH1F, TList, TH2F,TH3F ,TMath, TF1, TStyle, gStyle, TRefArray, TClonesArray, TObjArray, gPad, TPaveText, TLegend ,TString, TObject,gROOT,TFormula, TEllipse, TDirectory,TLorentzVector
from ROOT import TMath as mt
from datetime import date
import re
import xlwt
import copy
from xlwt import Workbook

# this code creates the histograms from the analysis results and also applies some additional cuts
# however I am still new to the pyroot so I might be defining histogram more than I needed
# my goal was to create just one set of histogram and clear it after every time I store them in root file for different level of cuts
# Different directory are created to store all the histogram at different level of cuts


#Opening the file>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#filename = "/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults"
#filename = "/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults_New"
#filename = "/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults_New_hopefullycomplete"
filename = "/home/amrit/Analysis/MyTestCode2/Data/combinedata/AnalysisResults_combined_AllTrigger"
#filename = "/home/amrit/Analysis/MyTestCode2/Data/combinedata/AnalysisResults_2018q_2018r.root"
infilename =filename+".root"



mcfilename_psi = "/home/amrit/Analysis/TestCode/nano/output_2018q_0608_2020/AnalysisResults_MC_Psi_MuMu_Incomplete"
mcfilename_jpsi = "/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults_Simulated_JPsi"
mcfilename_gammagamma = "/home/amrit/Analysis/TestCode/nano/output_2018q_0608_2020/AnalysisResults_GammaGamma_Medium"
inmc_psi_filename = mcfilename_psi+".root"
inmc_jpsi_filename = mcfilename_jpsi+".root"

inmc_gammagamma = mcfilename_gammagamma+".root"
file = TFile.Open(infilename)
mcfile_psi = TFile.Open(inmc_psi_filename)
mcfile_jpsi = TFile.Open(inmc_jpsi_filename)
#this file contains corrected tildephi values

TildePhi = TFile.Open("/home/amrit/Analysis/MyTestCode2/Data/combinedata/TildePhi.root")
TildePhiMC = TFile.Open("/home/amrit/Analysis/MyTestCode2/Data/combinedata/TildePhiMC.root")

##this line below will be used after obtaining gamma gamma mc analysis result

mcfile_gammagamma = TFile.Open(inmc_gammagamma)


#file = TFile.Open("AnalysisResults.root")
#list = TList()
#list = file.Get("Polar")
tree = TTree()
mcrectree_psi = TTree()
#mcgentree_psi = TTree()
mcrectree_jpsi = TTree()
mcgentree_jpsi = TTree()
mcrectree_gammagamma = TTree()

tree = file.Get("PolarizationJP/fRecTree")
tildephi_tree = TildePhi.Get("tildephi")

tildephimc_rectree = TildePhiMC.Get("tildephi")
tildephimc_gentree = TildePhiMC.Get("tildephigen")

print "main tree entry = ",tree.GetEntries(),"tildephi tree entry =", tildephi_tree.GetEntries()
tree.AddFriend(tildephi_tree)

#tildephi_tree.AddFriend("tree")

mcgentree_jpsi = mcfile_jpsi.Get("PolarizationJP/fGenTree")

mcrectree_jpsi = mcfile_jpsi.Get("PolarizationJP/fRecTree")
mcrectree_psi = mcfile_psi.Get("PolarizationJP/fRecTree")
mcrectree_jpsi.AddFriend(tildephimc_rectree)
mcgentree_jpsi.AddFriend(tildephimc_gentree)





mcrectree_gammagamma = mcfile_gammagamma.Get("PolarizationJP/fRecTree")


#entry_loop = tree.GetEntries()
#histo_loop = TH1F("histo_loop","histo_loop",1000,0,7)
histo_loop = TH1F("histo_loop","histo_loop",4000,-4,4)
canvas_loop = TCanvas()
#a =0;
#while a<entry_loop:
#    tildephi_tree.GetEntry(a)
    #tree.SetBranchAddress("fRecHelicityTildePhi_corrected", AddressOf(tree,"fRecHelicityTildePhi_corrected"))
    #if(fRecHelicityTildePhi_corrected>3.768 and fRecHelicityTildePhi_corrected<4.019):
#        histo_loop.Fill(fRecHelicityTildePhi_corrected)
#    a = a+1
#fRecHelicityTildePhi_corrected>3.768 && fRecHelicityTildePhi_corrected<4.019
canvas_loop.cd()
tree.Draw("fRecHelicityPhi>>histo_loop","","e")

histo_loop.Draw()
canvas_loop.SaveAs("helicitycheck.pdf")




#daughter2 = TLorentzVector()
#parent  =   TLorentzVector()
#parent = tree.parent()
#daughter =
#tree2 = file.Get("tree2")

#tree2.AddFriend(tree)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
text = TPaveText(.05,.1,.95,.8)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#legend = TLegend(x1,y1,x2,y2)

##########################x1,y1###########################x2y1
#wk = Workbook()


###########################x1y2##########################x2y2
#rb = open_workbook(file_path,formatting_info =True)
wk = Workbook()




legend = TLegend(0.45,0.8,0.8,0.4)
legend.SetFillStyle(0)
legend_angle = TLegend(0.45,0.8,0.8,0.4)
legend_angle.SetFillStyle(0)
legend_angle.SetLineColor(0)
#this is to use to run in batch mode  to avoid printing all the plots
gROOT.SetBatch(rt.kTRUE)
#this create the master canvas color and the entries to print
#gStyle.SetCanvasColor(22)
gStyle.SetOptStat("")
Date = date.today()
date_today = filename+str(Date)+".root"



#########################################################################
#filenamelist= ["AnalysisResults_MC_Psi_MuMu_Incomplete.root","AnalysisResults_MC_Jpsi_Incomplete.root","AnalysisResults_MC_gammagamma.root"]

#histo_canvas_names = ["_mcrectree_psi","_mcrectree_jpsi","_mcrectree_gammagamma"]#,"_mcgentree_gammagamma","_mcgentree_jpsi","_mcgentree_jpsi"]


file2 = TFile(date_today,"Recreate")




mcfits = TDirectory()
mcfits = file2.mkdir("mcfits")
tcut = "0.628<fRecHelicityPhi<0.879"


mcfits.cd()
"""psi_canvas = TCanvas("psi_canvas","psi_canvas",600,300)
psi_histogram = TH1F("psi_histogram","psi_histogram",100,0,5)
psi_canvas.cd()
mcrectree_psi.Draw("fRecPair_ParentMass>>psi_histogram","","e")
psi_histogram.SetDirectory(0)
psi_histogram.Fit(ft.sig_func_psi,"R")"""

psi_canvas = TCanvas("psi_canvas","psi_canvas",600,300)
psi_histogram = TH1F("psi_histogram","psi_histogram",300,2,6)
psi_canvas.cd()
mcrectree_psi.Draw("fRecPair_ParentMass>>psi_histogram","","e")





psi_histogram.SetDirectory(0)
psi_histogram.Sumw2()
integ_psi_hisogram = psi_histogram.Integral()
psi_histogram.Scale(1/integ_psi_hisogram)
#gaus_func= TF1("gaus_func","gaus",3.6,3.8)
#gaus_func.SetParameters(1,1,1)

#psi_histogram.Fit(gaus_func,"QR")
#psi_histogram.Fit(ft.mycris_func,"R")
#crystalball function order "constant , mean , sigma , alpha , N"""
 #                                 0      1       2      3      4

#ft.sig_func_psi.FixParameter(1,gaus_func.GetParameter(1))
#ft.sig_func_psi.FixParameter(2,gaus_func.GetParameter(2))
ft.sig_func_psi.SetLineColor(rt.kBlack)
psi_histogram.Fit(ft.sig_func_psi,"NQR+","",3,4.2)


#psi_histogram.Fit(ft.mycris_func,"R")

#psi_canvas.SaveAs("psi.png")
psi_canvas.Write()


"""jpsi_canvas = TCanvas("jpsi_canvas","jpsi_canvas",600,300)
jpsi_histogram = TH1F("jpsi_histogram","jpsi_histogram",100,0,5)
jpsi_canvas.cd()
mcrectree_jpsi.Draw("fRecPair_ParentMass>>jpsi_histogram","","e")
jpsi_histogram.SetDirectory(0)

jpsi_histogram.Fit(ft.sig_func_jpsi,"R+")"""





jpsi_canvas = TCanvas("jpsi_canvas","jpsi_canvas",600,300)
jpsi_histogram = TH1F("jpsi_histogram","jpsi_histogram",200,2,6)
jpsi_canvas.cd()
mcrectree_jpsi.Draw("fRecPair_ParentMass>>jpsi_histogram","","e")
jpsi_histogram.SetDirectory(0)
jpsi_histogram.Sumw2()
integ_jpsi_hisogram = jpsi_histogram.Integral()
jpsi_histogram.Scale(1/integ_jpsi_hisogram)

gStyle.SetOptStat("")










#jpsi_histogram.Fit(gaus_func2,"R","",2.5,3.16)

#ft.sig_func_jpsi.FixParameter(1,gaus_func2.GetParameter(1))
#ft.sig_func_jpsi.FixParameter(2,gaus_func2.GetParameter(2))

#ft.sig_func_jpsi.SetParameter(1,gaus_func2.GetParameter(1))
#ft.sig_func_jpsi.SetParameter(2,gaus_func2.GetParameter(2))


ft.sig_func_jpsi.SetLineColor(rt.kBlack)
jpsi_histogram.Fit(ft.sig_func_jpsi,"QR+","",2,4)           #2.5,3.2)



#jpsi_histogram.Fit(ft.sig_func2,"R+")
jpsi_canvas.Write()

gamma_canvas = TCanvas("gamma_canvas","gamma_canvas",600,300)
gamma_histogram = TH1F("gamma_histogram","gamma_histogram",100,0,10)
gamma_canvas.cd()
mcrectree_gammagamma.Draw("fRecPair_ParentMass>>gamma_histogram","","e")


gamma_histogram.SetDirectory(0)

gamma_histogram.Fit(ft.GammaGammaFit,"QR+","",1.8,4.5)
#gamma_histogram.Fit(ft.GammaGammaFit,"R")
#print "chisquare/NDF is : ", ft.GammaGammaFit.GetChisquare()/ft.GammaGammaFit.GetNDF()
gamma_canvas.Write()


#framelist_mc_rec = []

"""
jpsi_phi_collinsoper_canvas_gen = TCanvas("jpsi_phi_collinsoper_canvas_gen","jpsi_phi_collinsoper_canvas_gen",600,300)
jpsi_phi_collinsoper_histogram_gen= TH1F("jpsi_phi_collinsoper_histogram_gen","jpsi_phi_collinsoper_histogram_gen",25,-3.14,3.14)
jpsi_phi_collinsoper_histogram = jpsi_phi_collinsoper_histogram_gen.Clone("jpsi_phi_collinsoper_histogram")
jpsi_phi_collinsoper_canvas_gen.cd()
mcgentree_jpsi.Draw("fMCCollinPhi>>jpsi_phi_collinsoper_histogram_gen","","e")
#mcrectree_jpsi.Draw("fSimulated_Reconstructed_CollinPhi>>jpsi_phi_collinsoper_histogram_gen","","e")
jpsi_phi_collinsoper_histogram_gen.SetDirectory(0)
jpsi_phi_collinsoper_histogram_gen.Sumw2()

jpsi_phi_collinsoper_canvas_rec= TCanvas("jpsi_phi_collinsoper_canvas_rec","jpsi_phi_collinsoper_canvas_rec",600,300)
jpsi_phi_collinsoper_histogram_rec = TH1F("jpsi_phi_collinsoper_histogram_rec","jpsi_phi_collinsoper_histogram_rec",25,-3.14,3.14)
jpsi_phi_collinsoper_canvas_rec.cd()
#mcgentree_jpsi.Draw("fRecCollinPhi>>jpsi_phi_collinsoper_histogram_rec","","e")
mcrectree_jpsi.Draw("fRecCollinPhi>>jpsi_phi_collinsoper_histogram_rec","","e")
jpsi_phi_collinsoper_histogram_rec.SetDirectory(0)
jpsi_phi_collinsoper_histogram_rec.Sumw2()

jpsi_phi_collinsoper_canvas = TCanvas("jpsi_phi_collinsoper_canvas","jpsi_phi_collinsoper_canvas",600,300)
jpsi_phi_collinsoper_canvas.cd()
jpsi_phi_collinsoper_histogram.Divide(jpsi_phi_collinsoper_histogram_rec,jpsi_phi_collinsoper_histogram_gen)

jpsi_phi_collinsoper_histogram.SetDirectory(0)
jpsi_phi_collinsoper_histogram.Draw()
jpsi_phi_collinsoper_histogram.Sumw2()
jpsi_phi_collinsoper_canvas.Write()
jpsi_phi_collinsoper_canvas.SaveAs("anglebintest.pdf")

"""

mcfits.cd("../")







##################################


#defining the canvas for the reconstructed and grenerated mc events to fit them
#nmchistogram=0
#mcxmin=0.0
#mcxmax=6.0
#mcn_bin = 80
#mcbin_width = (mcxmax-mcxmin)/mcn_bin

#signal_func_psi_parameters= [0,0,0,0]
#signal_func_jpsi_parameters= [0,0,0,0]
#tail_func_parammeters = [0,0,0,0]
"""
while nmchistogram<len(histo_canvas_names):
    mcfolder = filenamelist[nmchistogram]

    vars()[mcfolder] = TDirectory()

    #folder = TDirectory()

    mcfolder = file2.mkdir(filenamelist[nmchistogram])


    mcfolder.cd()
    mcrecfile = TFile.Open(filenamelist[nmchistogram])
    mcrectree = mcrecfile.Get("PolarizationJP/fRecTree")

    canvasname = "canvas"+histo_canvas_names[nmchistogram]
    mccanvas = TCanvas(canvasname,canvasname,600,300)
    histoname = "hisogram"+histo_canvas_names[nmchistogram]
    histotitle = "Massplots"+ histo_canvas_names[nmchistogram]
    mchistogram = TH1F(histoname,histotitle,mcn_bin,mcxmin,mcxmax)
    bin_width = (mcxmax-mcxmin)/mcn_bin
    mcytitle = "Number of Events/{}GeV/C #rightarrow".format(mcbin_width)

    mchistogram.SetXTitle("Invariant mass of #mu^+mu^- pair(GeV/C^2)#rightarrow")

    mchistogram.SetYTitle(mcytitle)
    mchistogram.GetYaxis().SetTitleOffset(1.4)
    mchistogram.GetYaxis().CenterTitle()
    mchistogram.GetXaxis().CenterTitle()

    mccanvas.cd()


    #mcrectree.Draw("fRecPair_ParentMass>>mchistogram","","e")  #need to define the cut parameter which will be on cos theta

    #mchistogram.SetDirectory(0)


    #mchistogram.Write()
    if(filenamelist[nmchistogram]=="AnalysisResults_MC_Psi_MuMu_Incomplete.root"):

        #mchistogram.Fit(ft.sig_func_mc_psi,"QR")
                #mccanvas.Write()
        #mccanvas.SaveAs("recpari.png")
        int1=0
        print "fitting psi2s data", ft.sig_func_mc_psi.GetParameter(int1)
        while int1<4:
            signal_func_psi_parameters.append(ft.sig_func_mc_psi.GetParameter(int1))
            int1= int1+1

    elif (filenamelist[nmchistogram]== "AnalysisResults_MC_JPsi_MuMu_Incomplete.root"):

        #mchistogram.Fit(ft.sig_func_mc_jpsi,"QR")
        #mccanvas.Write()
        #mccanvas.SaveAs("recpari2.png")
        int2=0
        while int2<4:
            signal_func_jpsi_parameters.append(ft.sig_func_mc_jpsi.GetParameter(int2))
            #print signal_func_jpsi_parameters[int2]
            int2= int2+1

    elif (filenamelist[nmchistogram]== "AnalysisResults_MC_gammagamma_MuMu.root"):
        mchistogram.Fit(ft.tail_func_mc,"QR")
        mccanvas.Write()
        mccanvas.SaveAs("recpari3.png")
        int3=0
        while int3<4:
            tail_func_parammeters.append(ft.tail_func_mc.GetParameter(int3))
            int3= int3+1

    else:
        print "there is some error in the code with fitting mc data"

    #histogram.Fit(ft.sig_func,"NQR+")
    #ft.comb_func.SetParameters(ft.sig_func.GetParameter(0),ft.sig_func.GetParameter(1),ft.sig_func.GetParameter(2),ft.sig_func.GetParameter(3),ft.tail_func.GetParameter(0),ft.tail_func.GetParameter(1),ft.tail_func.GetParameter(6),ft.tail_func.GetParameter(3))
    #histogram.Fit(ft.comb_func,"NQR+")
    #tailclone = ft.tail_func.Clone("tailclone")
    #sigclone  = ft.sig_func.Clone("sigclone")
    #combclone = ft.comb_func.Clone("comb_func")

    #tailclone.FixParameter(0,ft.tail_func.GetParameter(0))
    #tailclone.FixParameter(1,ft.tail_func.GetParameter(1))
    #tailclone.FixParameter(2,ft.tail_func.GetParameter(2))
    #tailclone.FixParameter(3,ft.tail_func.GetParameter(3))


    #sigclone.FixParameter(0,ft.sig_func.GetParameter(0))
    #sigclone.FixParameter(1,ft.sig_func.GetParameter(1))
    #sigclone.FixParameter(2,ft.sig_func.GetParameter(2))
    #sigclone.FixParameter(3,ft.sig_func.GetParameter(3))

    #combclone.FixParameter(0,ft.comb_func.GetParameter(0))
    #combclone.FixParameter(1,ft.comb_func.GetParameter(1))
    #combclone.FixParameter(2,ft.comb_func.GetParameter(2))
    #combclone.FixParameter(3,ft.comb_func.GetParameter(3))
    #combclone.FixParameter(4,ft.comb_func.GetParameter(4))
    #combclone.FixParameter(5,ft.comb_func.GetParameter(5))
    #combclone.FixParameter(6,ft.comb_func.GetParameter(6))
    #combclone.FixParameter(7,ft.comb_func.GetParameter(7))

    #tailclone.SetLineColor(rt.kRed)
    #sigclone.SetLineColor(rt.kGreen)
    #combclone.SetLineColor(rt.kBlue)
    #tailclone.Draw("SAME")
    #sigclone.Draw("SAME")
    #combclone.Draw("SAME")





    #kmccanvas.Write()
    mcfolder.cd("../")
    nmchistogram= nmchistogram + 1
##########################################################################


"""
#defining histograms to find the fit parameters for dataset





#print hist





#ytitle = "Number of Events/"+ str(bin_width) + " GeV/C #rightarrow"









#print date_today

#list of theta bins in helicity
#helicitytheta = ["-0.6<fRecHelicityTheta&&fRecHelicityTheta<-0.520","-0.520<fRecHelicityTheta<-0.440","-0.440<fRecHelicityTheta<-0.360","-0.360<fRecHelicityTheta<-0.280","-0.280<fRecHelicityTheta<-0.200","-0.200<fRecHelicityTheta<-0.120","-0.120<fRecHelicityTheta<-0.040","-0.040<fRecHelicityTheta<0.040","0.040<fRecHelicityTheta<0.120","0.120<fRecHelicityTheta<0.200","0.200<fRecHelicityTheta<0.280","280<fRecHelicityTheta<0.360","0.360<fRecHelicityTheta<0.440","0.440<fRecHelicityTheta<0.520","0.520<fRecHelicityTheta<0.600"]


helicitytheta = ["-0.6<fRecHelicityTheta && fRecHelicityTheta<-0.520","-0.520<fRecHelicityTheta && fRecHelicityTheta<-0.440","-0.440<fRecHelicityTheta && fRecHelicityTheta<-0.360","-0.360<fRecHelicityTheta && fRecHelicityTheta<-0.280","-0.280<fRecHelicityTheta && fRecHelicityTheta<-0.200","-0.200<fRecHelicityTheta && fRecHelicityTheta<-0.120","-0.120<fRecHelicityTheta && fRecHelicityTheta<-0.040","-0.040<fRecHelicityTheta && fRecHelicityTheta<0.040","0.040<fRecHelicityTheta && fRecHelicityTheta<0.120","0.120<fRecHelicityTheta && fRecHelicityTheta<0.200","0.200<fRecHelicityTheta && fRecHelicityTheta<0.280","0.280<fRecHelicityTheta && fRecHelicityTheta<0.360","0.360<fRecHelicityTheta && fRecHelicityTheta<0.440","0.440<fRecHelicityTheta && fRecHelicityTheta<0.520","0.520<fRecHelicityTheta && fRecHelicityTheta<0.600"]






#list of phi bins in helicity

#helicityphi = ["-3.14<fRecHelicityPhi<-2.889","-2.889<fRecHelicityPhi<-2.638","-2.638<fRecHelicityPhi<-2.386","-2.386<fRecHelicityPhi<-2.135","-2.135<fRecHelicityPhi<-1.884","-1.884<fRecHelicityPhi<-1.633","-1.633<fRecHelicityPhi<-1.382","-1.382<fRecHelicityPhi<-1.130","-1.130<fRecHelicityPhi<-0.879","-0.879<fRecHelicityPhi<-0.628","-0.628<fRecHelicityPhi<-0.377","-0.377<fRecHelicityPhi<-0.126","-0.126<fRecHelicityPhi<0.126","0.126<fRecHelicityPhi<0.377","0.377<fRecHelicityPhi<0.628","0.628<fRecHelicityPhi<0.879","0.879<fRecHelicityPhi<1.130","1.130<fRecHelicityPhi<1.382","1.382<fRecHelicityPhi<1.633","1.633<fRecHelicityPhi<1.884","1.884<fRecHelicityPhi<2.135","2.135<fRecHelicityPhi<2.386","2.386<fRecHelicityPhi<2.638","2.638<fRecHelicityPhi<2.889","2.889<fRecHelicityPhi<3.14"]


#helicityphi = ["-3.14<fRecHelicityPhi && fRecHelicityPhi<-2.889","-2.889<fRecHelicityPhi && fRecHelicityPhi<-2.638","-2.638<fRecHelicityPhi && fRecHelicityPhi<-2.386","-2.386<fRecHelicityPhi && fRecHelicityPhi<-2.135","-2.135<fRecHelicityPhi && fRecHelicityPhi<-1.884","-1.884<fRecHelicityPhi && fRecHelicityPhi<-1.633","-1.633<fRecHelicityPhi && fRecHelicityPhi<-1.382","-1.382<fRecHelicityPhi && fRecHelicityPhi<-1.130","-1.130<fRecHelicityPhi && fRecHelicityPhi<-0.879","-0.879<fRecHelicityPhi && fRecHelicityPhi<-0.628","-0.628<fRecHelicityPhi && fRecHelicityPhi<-0.377","-0.377<fRecHelicityPhi && fRecHelicityPhi<-0.126","-0.126<fRecHelicityPhi && fRecHelicityPhi<0.126","0.126<fRecHelicityPhi && fRecHelicityPhi<0.377","0.377<fRecHelicityPhi && fRecHelicityPhi<0.628","0.628<fRecHelicityPhi && fRecHelicityPhi<0.879","0.879<fRecHelicityPhi && fRecHelicityPhi<1.130","1.130<fRecHelicityPhi && fRecHelicityPhi<1.382","1.382<fRecHelicityPhi && fRecHelicityPhi<1.633","1.633<fRecHelicityPhi && fRecHelicityPhi<1.884","1.884<fRecHelicityPhi && fRecHelicityPhi<2.135","2.135<fRecHelicityPhi && fRecHelicityPhi<2.386","2.386<fRecHelicityPhi && fRecHelicityPhi<2.638","2.638<fRecHelicityPhi && fRecHelicityPhi<2.889","2.889<fRecHelicityPhi && fRecHelicityPhi<3.14"]


helicityphi = ["-3.14<fRecHelicityPhi && fRecHelicityPhi<-2.889","-2.889<fRecHelicityPhi && fRecHelicityPhi<-2.638","-2.638<fRecHelicityPhi && fRecHelicityPhi<-2.386","-2.386<fRecHelicityPhi && fRecHelicityPhi<-2.135","-2.135<fRecHelicityPhi && fRecHelicityPhi<-1.884","-1.884<fRecHelicityPhi && fRecHelicityPhi<-1.633","-1.633<fRecHelicityPhi && fRecHelicityPhi<-1.382","-1.382<fRecHelicityPhi && fRecHelicityPhi<-1.130","-1.130<fRecHelicityPhi && fRecHelicityPhi<-0.879","-0.879<fRecHelicityPhi && fRecHelicityPhi<-0.628","-0.628<fRecHelicityPhi && fRecHelicityPhi<-0.377","-0.377<fRecHelicityPhi && fRecHelicityPhi<-0.126","-0.126<fRecHelicityPhi && fRecHelicityPhi<0.126","0.126<fRecHelicityPhi && fRecHelicityPhi<0.377","0.377<fRecHelicityPhi && fRecHelicityPhi<0.628","0.628<fRecHelicityPhi && fRecHelicityPhi<0.879","0.879<fRecHelicityPhi && fRecHelicityPhi<1.130","1.130<fRecHelicityPhi && fRecHelicityPhi<1.382","1.382<fRecHelicityPhi && fRecHelicityPhi<1.633","1.633<fRecHelicityPhi && fRecHelicityPhi<1.884","1.884<fRecHelicityPhi && fRecHelicityPhi<2.135","2.135<fRecHelicityPhi && fRecHelicityPhi<2.386","2.386<fRecHelicityPhi && fRecHelicityPhi<2.638","2.638<fRecHelicityPhi && fRecHelicityPhi<2.889","2.889<fRecHelicityPhi && fRecHelicityPhi<3.14"]


#helicitytildephi =["3.768<fRecHelicityTildePhi && fRecHelicityTildePhi<4.019"]

#helicitytildephi =["0.000<fRecHelicityTildePhi && fRecHelicityTildePhi<0.251","0.251<fRecHelicityTildePhi && fRecHelicityTildePhi<0.502","0.502<fRecHelicityTildePhi && fRecHelicityTildePhi<0.754","0.754<fRecHelicityTildePhi && fRecHelicityTildePhi<1.005","1.005<fRecHelicityTildePhi && fRecHelicityTildePhi<1.256","1.256<fRecHelicityTildePhi && fRecHelicityTildePhi<1.507","1.507<fRecHelicityTildePhi && fRecHelicityTildePhi<1.758","1.758<fRecHelicityTildePhi && fRecHelicityTildePhi<2.010","2.010<fRecHelicityTildePhi && fRecHelicityTildePhi<2.261","2.261<fRecHelicityTildePhi && fRecHelicityTildePhi<2.512","2.512<fRecHelicityTildePhi && fRecHelicityTildePhi<2.763","2.763<fRecHelicityTildePhi && fRecHelicityTildePhi<3.014","3.014<fRecHelicityTildePhi && fRecHelicityTildePhi<3.266","3.266<fRecHelicityTildePhi && fRecHelicityTildePhi<3.517","3.517<fRecHelicityTildePhi && fRecHelicityTildePhi<3.768","3.768<fRecHelicityTildePhi && fRecHelicityTildePhi<4.019","4.019<fRecHelicityTildePhi && fRecHelicityTildePhi<4.270","4.270<fRecHelicityTildePhi && fRecHelicityTildePhi<4.522","4.522<fRecHelicityTildePhi && fRecHelicityTildePhi<4.773","4.773<fRecHelicityTildePhi && fRecHelicityTildePhi<5.024","5.024<fRecHelicityTildePhi && fRecHelicityTildePhi<5.275","5.275<fRecHelicityTildePhi && fRecHelicityTildePhi<5.526","5.526<fRecHelicityTildePhi && fRecHelicityTildePhi<5.778","5.778<fRecHelicityTildePhi && fRecHelicityTildePhi<6.029","6.029<fRecHelicityTildePhi && fRecHelicityTildePhi<6.280"]

helicitytildephi =["0.000<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<0.251","0.251<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<0.502","0.502<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<0.754","0.754<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<1.005","1.005<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<1.256","1.256<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<1.507","1.507<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<1.758","1.758<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<2.010","2.010<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<2.261","2.261<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<2.512","2.512<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<2.763","2.763<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<3.014","3.014<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<3.266","3.266<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<3.517","3.517<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<3.768","3.768<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<4.019","4.019<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<4.270","4.270<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<4.522","4.522<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<4.773","4.773<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<5.024","5.024<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<5.275","5.275<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<5.526","5.526<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<5.778","5.778<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<6.029","6.029<fRecHelicityTildePhi_corrected && fRecHelicityTildePhi_corrected<6.280"]



#tildephi = [0.251]

colinsopertheta =["-0.6<fRecCollinTheta && fRecCollinTheta<-0.520","-0.520<fRecCollinTheta && fRecCollinTheta<-0.440","-0.440<fRecCollinTheta && fRecCollinTheta<-0.360","-0.360<fRecCollinTheta && fRecCollinTheta<-0.280","-0.280<fRecCollinTheta && fRecCollinTheta<-0.200","-0.200<fRecCollinTheta && fRecCollinTheta<-0.120","-0.120<fRecCollinTheta && fRecCollinTheta<-0.040","-0.040<fRecCollinTheta && fRecCollinTheta<0.040","0.040<fRecCollinTheta && fRecCollinTheta<0.120","0.120<fRecCollinTheta && fRecCollinTheta<0.200","0.200<fRecCollinTheta && fRecCollinTheta<0.280","0.280<fRecCollinTheta && fRecCollinTheta<0.360","0.360<fRecCollinTheta && fRecCollinTheta<0.440","0.440<fRecCollinTheta && fRecCollinTheta<0.520","0.520<fRecCollinTheta && fRecCollinTheta<0.600"]



#colinsoperphi = ["0.879<fRecCollinPhi && fRecCollinPhi<1.130"]
colinsoperphi =["-3.14<fRecCollinPhi && fRecCollinPhi<-2.889","-2.889<fRecCollinPhi && fRecCollinPhi<-2.638","-2.638<fRecCollinPhi && fRecCollinPhi<-2.386","-2.386<fRecCollinPhi && fRecCollinPhi<-2.135","-2.135<fRecCollinPhi && fRecCollinPhi<-1.884","-1.884<fRecCollinPhi && fRecCollinPhi<-1.633","-1.633<fRecCollinPhi && fRecCollinPhi<-1.382","-1.382<fRecCollinPhi && fRecCollinPhi<-1.130","-1.130<fRecCollinPhi && fRecCollinPhi<-0.879","-0.879<fRecCollinPhi && fRecCollinPhi<-0.628","-0.628<fRecCollinPhi && fRecCollinPhi<-0.377","-0.377<fRecCollinPhi && fRecCollinPhi<-0.126","-0.126<fRecCollinPhi && fRecCollinPhi<0.126","0.126<fRecCollinPhi && fRecCollinPhi<0.377","0.377<fRecCollinPhi && fRecCollinPhi<0.628","0.628<fRecCollinPhi && fRecCollinPhi<0.879","0.879<fRecCollinPhi && fRecCollinPhi<1.130","1.130<fRecCollinPhi && fRecCollinPhi<1.382","1.382<fRecCollinPhi && fRecCollinPhi<1.633","1.633<fRecCollinPhi && fRecCollinPhi<1.884","1.884<fRecCollinPhi && fRecCollinPhi<2.135","2.135<fRecCollinPhi && fRecCollinPhi<2.386","2.386<fRecCollinPhi && fRecCollinPhi<2.638","2.638<fRecCollinPhi && fRecCollinPhi<2.889","2.889<fRecCollinPhi && fRecCollinPhi<3.14"]



#there is some mistake in tilde calculation... In original analysis, negative value of tilde phi were added with 2*pi
#I missed that step. I have two option, I can analyze the analysis result file and correct the tildephicalculation
#or adjust in such a way that I calculate tilde phi before applying the cut
#either way the result will be same as goal is to add 2*pi to every negative value of tildephi on both frame of refercne

#colinsopertildephi =["0.000<fRecCollinTildePhi && fRecCollinTildePhi<0.251","0.251<fRecCollinTildePhi && fRecCollinTildePhi<0.502","0.502<fRecCollinTildePhi && fRecCollinTildePhi<0.754","0.754<fRecCollinTildePhi && fRecCollinTildePhi<1.005","1.005<fRecCollinTildePhi && fRecCollinTildePhi<1.256","1.256<fRecCollinTildePhi && fRecCollinTildePhi<1.507","1.507<fRecCollinTildePhi && fRecCollinTildePhi<1.758","1.758<fRecCollinTildePhi && fRecCollinTildePhi<2.010","2.010<fRecCollinTildePhi && fRecCollinTildePhi<2.261","2.261<fRecCollinTildePhi && fRecCollinTildePhi<2.512","2.512<fRecCollinTildePhi && fRecCollinTildePhi<2.763","2.763<fRecCollinTildePhi && fRecCollinTildePhi<3.014","3.014<fRecCollinTildePhi && fRecCollinTildePhi<3.266","3.266<fRecCollinTildePhi && fRecCollinTildePhi<3.517","3.517<fRecCollinTildePhi && fRecCollinTildePhi<3.768","3.768<fRecCollinTildePhi && fRecCollinTildePhi<4.019","4.019<fRecCollinTildePhi && fRecCollinTildePhi<4.270","4.270<fRecCollinTildePhi && fRecCollinTildePhi<4.522","4.522<fRecCollinTildePhi && fRecCollinTildePhi<4.773","4.773<fRecCollinTildePhi && fRecCollinTildePhi<5.024","5.024<fRecCollinTildePhi && fRecCollinTildePhi<5.275","5.275<fRecCollinTildePhi && fRecCollinTildePhi<5.526","5.526<fRecCollinTildePhi && fRecCollinTildePhi<5.778","5.778<fRecCollinTildePhi && fRecCollinTildePhi<6.029","6.029<fRecCollinTildePhi && fRecCollinTildePhi<6.280"]

#colinsopertildephi =["3.768<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<4.019"]
colinsopertildephi =["0.000<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<0.251","0.251<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<0.502","0.502<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<0.754","0.754<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<1.005","1.005<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<1.256","1.256<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<1.507","1.507<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<1.758","1.758<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<2.010","2.010<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<2.261","2.261<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<2.512","2.512<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<2.763","2.763<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<3.014","3.014<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<3.266","3.266<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<3.517","3.517<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<3.768","3.768<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<4.019","4.019<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<4.270","4.270<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<4.522","4.522<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<4.773","4.773<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<5.024","5.024<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<5.275","5.275<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<5.526","5.526<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<5.778","5.778<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<6.029","6.029<fRecCollinTildePhi_corrected && fRecCollinTildePhi_corrected<6.280"]


#colinsopertildephi =["-3.14<fRecCollinPhi && fRecCollinPhi<-2.889","-2.889<fRecCollinPhi && fRecCollinPhi<-2.638","-2.638<fRecCollinPhi && fRecCollinPhi<-2.386","-2.386<fRecCollinPhi && fRecCollinPhi<-2.135","-2.135<fRecCollinPhi && fRecCollinPhi<-1.884","-1.884<fRecCollinPhi && fRecCollinPhi<-1.633","-1.633<fRecCollinPhi && fRecCollinPhi<-1.382","-1.382<fRecCollinPhi && fRecCollinPhi<-1.130","-1.130<fRecCollinPhi && fRecCollinPhi<-0.879","-0.879<fRecCollinPhi && fRecCollinPhi<-0.628","-0.628<fRecCollinPhi && fRecCollinPhi<-0.377","-0.377<fRecCollinPhi && fRecCollinPhi<-0.126","-0.126<fRecCollinPhi && fRecCollinPhi<0.126","0.126<fRecCollinPhi && fRecCollinPhi<0.377","0.377<fRecCollinPhi && fRecCollinPhi<0.628","0.628<fRecCollinPhi && fRecCollinPhi<0.879","0.879<fRecCollinPhi && fRecCollinPhi<1.130","1.130<fRecCollinPhi && fRecCollinPhi<1.382","1.382<fRecCollinPhi && fRecCollinPhi<1.633","1.633<fRecCollinPhi && fRecCollinPhi<1.884","1.884<fRecCollinPhi && fRecCollinPhi<2.135","2.135<fRecCollinPhi && fRecCollinPhi<2.386","2.386<fRecCollinPhi && fRecCollinPhi<2.638","2.638<fRecCollinPhi && fRecCollinPhi<2.889","2.889<fRecCollinPhi && fRecCollinPhi<3.14"]











# directory is created to fill histograms without cuts
# way to create a string as a variable
#angle_cut = ["fRecCollinTheta<0.6 &&fRecCollinTheta>-0.6 && fRecCollinTildePhi_corrected<6.28 &&fRecCollinTildePhi_corrected<0 && fRecCollinTildePhi_corrected<6.28 &&fRecCollinTildePhi_corrected<0", "fRecCollinPhi<3.14 && fRecCollinPhi>-3.14 && fRecCollinTildePhi_corrected<6.28 &&fRecCollinTildePhi_corrected<0","fRecCollinTheta<0.6 &&fRecCollinTheta>-0.6 && fRecCollinTildePhi_corrected<6.28 &&fRecCollinTildePhi_corrected<0"]
angle_cut = "fRecCollinTheta<0.6 && fRecCollinTheta>-0.6 && fRecHelicityTheta<0.6 && fRecHelicityTheta>-0.6"
angle_cut_gen = "fMCCollinTheta<0.6 && fMCCollinTheta>-0.6 && fMCHelicityTheta<0.6 && fMCHelicityTheta>-0.6"
reference_frame = ["colinsoper_phi","collinsoper_theta","helicity_phi","helicity_theta","colinsoper_tilde{#phi}","helicity_tilde{#phi}"]
#reference_frame = ["colinsoper_tilde{#phi}"]#,"helicity_tilde{#phi}"]

branchname_gen = ["fMCCollinPhi","fMCCollinTheta","fMCHelicityPhi","fMCHelicityTheta","fMCCollinTildePhi_corrected","fMCHelicityTildePhi_corrected"]
#branchname_gen = ["fMCCollinPhi","fMCCollinTheta","fMCHelicityPhi","fMCHelicityTheta","(fMCCollinTildePhi < 0) ? fMCCollinTildePhi+ 2 * 3.14 : fMCCollinTildePhi","(fMCHelicityTildePhi<0)? fMCHelicityTildePhi+2 * 3.14: fMCHelicityTildePhi"]

branchname_rec = ["fRecCollinPhi","fRecCollinTheta","fRecHelicityPhi","fRecHelicityTheta","fRecCollinTildePhiMC_corrected"," fRecHelicityTildePhiMC_corrected"]
#branchname_rec = ["fRecCollinPhi","fRecCollinTheta","fRecHelicityPhi","fRecHelicityTheta","(fRecCollinTildePhi < 0) ? fRecCollinTildePhi+ 2 * 3.14 : fRecCollinTildePhi"," (fRecHelicityTildePhi<0)? fRecHelicityTildePhi+ 2 * 3.14: fRecHelicityTildePhi"]


#creating the list of yeild to fit with respective angular bins
# i am using 1 dimensional list for simplicity, I might use multidimensional list later
#however, i think if I just create the histogram with low and high value of angle with total bins equal to the bins for mass distribution
# i might be able to plot the histogram without any problem. This is version1(9/29/2020)
list_yeild_colinsoper_phi =[]
list_yeild_collinsoper_theta =[]
list_yeild_helicity_phi = []
list_yeild_helicity_theta = []
list_yeild_colinsoper_tildephi =[]
list_yeild_helicity_tilde = []

list_angle_colinsoper_phi =[]
list_angle_collinsoper_theta =[]
list_angle_helicity_phi = []
list_angle_helicity_theta = []
list_angle_colinsoper_tildephi =[]
list_angle_helicity_tilde = []
#angle_xmin= 0.0
#angle_xmax= 0.0


#master_canvas = []
 # print vars()



#histograms = []

nframe = 0
cut_add = "fRecPair_Parent.Pt()<0.25 && fRecPair_Parent.Rapidity()<-2.5"
cut_add_gen = "fMCPair_Parent.Pt()<0.25 && fMCPair_Parent.Rapidity()<-2.5"


"""
mycanvas = TCanvas("mycanvas","canvas",600,600)
mycanvas.cd()
#myhistogram = TH1F("myhistogram","myhistogram",100,0,2)
myhistogram = TH1F()
#tree.Draw("fRecPair_Parent.Pt()>>myhistogram","fRecPair_Parent.Pt()<0.25","e")
tree.Draw("fRecPair_Parent.Pt()>>myhistogram","fRecPair_Parent.Pt()<0.25 && fRecPair_Parent.Rapidity()<-2.5 && fRecPair_Parent.Rapidity()>-4.0","e")
mycanvas.SaveAs("pt.pdf")
"""
#print "reference frame length must be 4 and it is : " , len(reference_frame)



while  nframe<len(reference_frame):
  print "reference frame is" , reference_frame[nframe]
  #new = copy.copy(reference_frame[nframe])

  new = wk.add_sheet(reference_frame[nframe],True)
  #new.SetName(reference_frame[nframe])

  #folder = reference_frame[nframe]
  #vars()[folder] = TDirectory()
  folder = TDirectory()
  folder = file2.mkdir(reference_frame[nframe])

  folder.cd()
  cutlist_name = "cutlist_{}".format(reference_frame[nframe])
  cut = []




  angle_xmin= 0.0
  angle_xmax= 0.0
  if (reference_frame[nframe] == "helicity_theta"):
    cut = list(helicitytheta)
    angle_xmin=-0.6
    angle_xmax= 0.6
  if(reference_frame[nframe] == "helicity_phi"):
    cut = list(helicityphi)
    angle_xmin=-3.14
    angle_xmax= 3.14
  if(reference_frame[nframe] == "colinsoper_phi"):
    cut = list(colinsoperphi)
    angle_xmin=-3.14
    angle_xmax= 3.14
  if(reference_frame[nframe] == "collinsoper_theta"):
    cut = list(colinsopertheta)
    angle_xmin=-0.6
    angle_xmax= 0.6
  if(reference_frame[nframe] == "colinsoper_tilde{#phi}"):
    cut = list(colinsopertildephi)
    angle_xmin= 0.00
    angle_xmax= 6.280
  if(reference_frame[nframe] == "helicity_tilde{#phi}"):
    cut = list(helicitytildephi)
    angle_xmin= 0.00
    angle_xmax= 6.280




###############histogram for angles#########################################################
  angle_hist_name = "angle_histname_{}".format(reference_frame[nframe])
  angle_nbins = len(cut)
  angle_histogram = TString()
  angle_histogram = "{}".format(angle_hist_name)
  angle_canvas = TCanvas(angle_histogram,"Canvas of Angles",600,600)
  vars()[angle_histogram] = TH1F()
  angle_histogram = TH1F("angle_histogram","Plots",angle_nbins,angle_xmin,angle_xmax)
  angle_ytitle = "Number of Events"

  angle_histogram.SetXTitle(reference_frame[nframe])

  angle_histogram.SetYTitle(angle_ytitle)
  angle_histogram.GetYaxis().SetTitleOffset(1.4)
  angle_histogram.GetYaxis().CenterTitle()
  angle_histogram.GetXaxis().CenterTitle()
##########################################################histogram for angles###########################


#############################################angle for corrected ##################################
  angle_hist_name_corrected = "angle_histname_corrected_{}".format(reference_frame[nframe])
  #angle_nbins = len(cut)
  angle_histogram_corrected = TString()
  angle_histogram_corrected = "{}".format(angle_hist_name_corrected)
  angle_canvas_corrected = TCanvas(angle_histogram_corrected,"Canvas of Angles",600,600)
  vars()[angle_histogram_corrected] = TH1F()
  angle_histogram_corrected = TH1F("angle_histogram_corrected","Corrected A #times #epsilon",angle_nbins,angle_xmin,angle_xmax)
  angle_ytitle_corrected = "Number of Events / A #times E (Corrected)"

  angle_histogram_corrected.SetXTitle(reference_frame[nframe])

  angle_histogram_corrected.SetYTitle(angle_ytitle)
  angle_histogram_corrected.GetYaxis().SetTitleOffset(1.4)
  angle_histogram_corrected.GetYaxis().CenterTitle()
  angle_histogram_corrected.GetXaxis().CenterTitle()

##################################################
  angle_hist_name_gen = "angle_histname_gen_{}".format(reference_frame[nframe])
  angle_histogram_gen = TString()
  angle_histogram_gen = "{}".format(angle_hist_name_gen)
  angle_canvas_gen = TCanvas(angle_histogram_gen,"canvas",600,300)
  vars() [angle_histogram_gen] = TH1F()
  angle_histogram_gen = TH1F("angle_histogram_gen","Generated Angle Distribution",angle_nbins,angle_xmin,angle_xmax)
########################################################################################################################

##################################################
  angle_hist_name_rec = "angle_histname_rec_{}".format(reference_frame[nframe])
  angle_histogram_rec = TString()
  angle_histogram_rec = "{}".format(angle_hist_name_rec)

  angle_canvas_rec = TCanvas(angle_histogram_rec,"canvas",600,300)
  vars() [angle_histogram_rec] = TH1F()
  angle_histogram_rec = TH1F("angle_histogram_rec","Generated Angle Distribution",angle_nbins,angle_xmin,angle_xmax)
########################################################################################################################


##################################################
  angle_hist_name_axe = "angle_histname_axe_{}".format(reference_frame[nframe])
  angle_histogram_axe = TString()
  angle_histogram_axe = "{}".format(angle_hist_name_axe)

  angle_canvas_axe = TCanvas(angle_histogram_axe,"canvas",600,300)
  vars() [angle_histogram_axe] = TH1F()
  angle_histogram_axe = TH1F("angle_histogram_axe","A #times E",angle_nbins,angle_xmin,angle_xmax)
  #angle_ytitle_corrected = "Number of Events / A #times E (Corrected)"

  angle_histogram_axe.SetXTitle(reference_frame[nframe])

  angle_histogram_axe.SetYTitle("A #times E")
  angle_histogram_axe.GetYaxis().SetTitleOffset(1.4)
  angle_histogram_axe.GetYaxis().CenterTitle()
  angle_histogram_axe.GetXaxis().CenterTitle()
  gStyle.SetOptStat("")
########################################################################################################################
  angle_canvas_rec.cd()
  mcrectree_jpsi.Draw(branchname_rec[nframe]+">>angle_histogram_rec", angle_cut+ "&&"+ cut_add,"e")
  angle_histogram_rec.SetDirectory(0)
  angle_histogram_rec.Sumw2()
  angle_canvas_gen.cd()
  mcgentree_jpsi.Draw(branchname_gen[nframe] + ">>angle_histogram_gen","","e")
  angle_histogram_gen.SetDirectory(0)
  angle_histogram_gen.Sumw2()

  angle_canvas_axe.cd()
  angle_histogram_axe.Divide(angle_histogram_rec,angle_histogram_gen)

  angle_histogram_axe.SetDirectory(0)
  angle_histogram_axe.Draw()
  angle_histogram_axe.Sumw2()
  angle_histogram_axe.Write()
  #angle_histogram_axe.SaveAs(angle_hist_name_axe+"test.pdf")













  #print cutlist_name

  #hist_name = "histname_"+reference_frame[nframe]
  hist_name = "histname_{}".format(reference_frame[nframe])

  #cutlist_name = [] #char[15]



  #nbins = 80
  #nfiles = len(hist_name)
  nfiles = len(cut)

  xmin=2.0
  xmax=6.0
  #n_bin = 50 #working bin with bin width 0.03
  n_bin = 80 # bind width in AN plots 0.05
  i =0

  #print "length of the cut parameter list " , len(cut), reference_frame[nframe]



  #print vars()

  while i<nfiles:



    #print "cut parameters" , cut[i]
    histogram = TString()
  #  hist = hist_name + "_"+ str(i)
    histogram = "{}_{}".format(hist_name,i)
    #print i
    #print hist]
    #combine_histogram = "{}_{}".format(hist_name,i)
    #combine_canvas = TCanvas(combine_histogram,)

   # i=i+1
    #canvas2 = TCanvas(","Canvas of Mass",600,600)
    canvas = TCanvas(histogram,"Canvas of Mass",600,600)
    vars()[histogram] = TH1F()
    histogram = TH1F("histogram","Mass Plots",n_bin,xmin,xmax)
    #print hist


    bin_width = (xmax-xmin)/n_bin



    #ytitle = "Number of Events/"+ str(bin_width) + " GeV/C #rightarrow"
    ytitle = "Number of Events/{}GeV/C #rightarrow".format(bin_width)

    histogram.SetXTitle("Invariant mass of #mu^{+}#mu^{-} pair(GeV/C^{2})#rightarrow")

    histogram.SetYTitle(ytitle)
    histogram.GetYaxis().SetTitleOffset(1.4)
    histogram.GetYaxis().CenterTitle()
    histogram.GetXaxis().CenterTitle()










   # master_canvas.append(canvas)
    #histograms.append(histogram)


    #master_canvas[i].cd()

    canvas.cd()
    #tree.Draw("fRecPair_ParentMass>>histogram",cut[i]+ "&&" + angle_cut[nframe],"e0") #this is to check if my selection are similar as simone's results
    tree.Draw("fRecPair_ParentMass>>histogram",cut[i]+"&&"+cut_add+"&&"+ angle_cut,"e")  #need to define the cut parameter which will be on cos theta
    #tree.Draw("fRecPair_ParentMass>>histogram","","e")
    #histogram.Write()

    #
    histogram.SetDirectory(0)
    #while i<100:
        #print "to check the histogram is empty or not using the bin center = ", histogram.GetBinContent(i)
    #    i = i+1

    #histogram.Fit("gaus","R","",2,3)
    #gaus.Draw("SAME")
    #histogram.DrawCopy()
    #tail_func.FixParameter(1,tail_func_parammeters[1])
    #tail_func.FixParameter(2,tail_func_parammeters[2])
    #tail_func.FixParameter(3,tail_func_parammeters[3])
    #par 3 = jpsi n  and par 9 = psin
    #par
    #sig_func.FixParameter()

    #histogram.Fit(ft.tail_func,"R+")
    #histogram.Fit(ft.sig_func,"NQR+")
    #ft.comb_func.SetParameters(ft.sig_func.GetParameter(0),ft.sig_func.GetParameter(1),ft.sig_func.GetParameter(2),ft.sig_func.GetParameter(3),ft.tail_func.GetParameter(0),ft.tail_func.GetParameter(1),ft.tail_func.GetParameter(6),ft.tail_func.GetParameter(3))
    # for comb function n1 = par3 +n2 = par9 a1 = par 2 a2 = par 10
                                    # for sig func par n = par3 a = par 2
                                    #tail = and sig par5--->1 par6--->2 par7----3

    #signal_func_psi_parameters= []
    #signal_func_jpsi_parameters= []
    #tail_func_parammeters = []
    #print "this line is running"

     #crystalball function order "constant , mean , sigma , alpha , N"""
     #                                 0      1       2      3      4
     #                                 5      6       7      8      9
     #                     ( "GammaGammaFit","[0]*TMath::Exp(-[1]*x)*( (x < [2]) ? 1 : 1 + [3]*(x-[2])*(x-[2]) + [4]*(x-[2])*(x-[2])*(x-[2]) +[5]*(x-[2])*(x-[2])*(x-[2])*(x-[2]))",2,5)
     #                                 const 10 ,    b  11, mth 12 , a1 13, a2 14 , a3 15
    #ft.sig_func_jpsi_data.SetParameters(1,3.12,0.090,1.08,115)
    #ft.sig_func_jpsi_data.SetParLimits(1,3.113,3.17)
    ft.sig_func_jpsi_data.FixParameter(3,ft.sig_func_jpsi.GetParameter(3))
    ft.sig_func_jpsi_data.FixParameter(4,ft.sig_func_jpsi.GetParameter(4))

    histogram.Fit(ft.sig_func_jpsi_data,"NQR","",2.95,3.25)
    sig_func_jpsi_data_clone = ft.sig_func_jpsi_data.Clone("sig_func_jpsi_data_clone")
    sig_func_jpsi_data_clone.SetLineColor(rt.kBlue+2)

    #print "############################", ft.sig_func_psi.GetParameter(2)/ft.sig_func_jpsi.GetParameter(2), "#########################"
    sigma_for_psi2s =  (ft.sig_func_psi.GetParameter(2)/ft.sig_func_jpsi.GetParameter(2)) *ft.sig_func_jpsi_data.GetParameter(2)

    ft.sig_func_psi_data.FixParameter(3,ft.sig_func_psi.GetParameter(3))
    ft.sig_func_psi_data.FixParameter(4,ft.sig_func_psi.GetParameter(4))
    ft.sig_func_psi_data.FixParameter(2,sigma_for_psi2s)



    histogram.Fit(ft.sig_func_psi_data,"NQR+","",3.5,3.8)
    sig_func_psi_data_clone = ft.sig_func_psi_data.Clone("sig_func_psi_data_clone")
    sig_func_psi_data_clone.SetLineColor(rt.kYellow+2)

    #histogram.Fit(ft.expo_tail,"QR+","",4,6)







    #expo_func=TF1("expo_func","expo",2,5)
    #histogram.Fit(expo_func,"NQR+","",4,5)


    #crystalball function order "constant , mean , sigma , alpha , N"""
    #                                 0      1       2      3      4
    #                                 5      6       7      8      9
    #                     ( "GammaGammaFit","[0]*TMath::Exp(-[1]*x)*( (x < [2]) ? 1 : 1 + [3]*(x-[2])*(x-[2]) + [4]*(x-[2])*(x-[2])*(x-[2]) +[5]*(x-[2])*(x-[2])*(x-[2])*(x-[2]))",2,5)
    #                                 const 10 ,    b  11, mth 12 , a1 13, a2 14 , a3 15


   #ft.comb_func.FixParameter(0,ft.sig_func_jpsi_data.GetParameter(0))

    #sig_func_psi.SetParameters(1,3.67,0.070,1.08,20)
    #sig_func_jpsi.SetParameters(1,3.1,0.090,1,115)

    """ft.comb_func.FixParameter(3,ft.sig_func_jpsi_data.GetParameter(3))
    ft.comb_func.FixParameter(4,ft.sig_func_jpsi_data.GetParameter(4))
    ft.comb_func.FixParameter(1,ft.sig_func_jpsi_data.GetParameter(1))
    ft.comb_func.FixParameter(2,ft.sig_func_jpsi_data.GetParameter(2))
    #ft.comb_func.FixParameter(0,ft.sig_func_jpsi_data.GetParameter(0))"""
    #sigma_for_psi2s =  ft.sig_func_jpsi.GetParameter(2) *1.09
    #sigma_for_psi2s = 1.09





    ft.comb_func.FixParameter(3,ft.sig_func_jpsi.GetParameter(3))
    ft.comb_func.FixParameter(4,ft.sig_func_jpsi.GetParameter(4))
    #ft.comb_func.FixParameter(1,ft.sig_func_jpsi.GetParameter(1))
    #ft.comb_func.FixParameter(2,ft.sig_func_jpsi.GetParameter(2))
    #ft.comb_func.FixParameter(0,ft.sig_func_jpsi_data.GetParameter(0))

    #ft.comb_func.FixParameter(6,ft.sig_func_psi_data.GetParameter(1))
    #ft.comb_func.SetParLimits(6,psi_mean_limitdown,psi_mean_limitup)
    ft.comb_func.FixParameter(7,sigma_for_psi2s)
    ft.comb_func.FixParameter(8,ft.sig_func_psi.GetParameter(3))
    ft.comb_func.FixParameter(9,ft.sig_func_psi.GetParameter(4))
    ft.comb_func.FixParameter(6,ft.sig_func_psi_data.GetParameter(1))


    #ft.comb_func.SetParLimits(12,1,3)
    #ft.comb_func.FixParameter(11,ft.expo_tail.GetParameter(1))
    ft.comb_func.FixParameter(12,ft.GammaGammaFit.GetParameter(2))
    #ft.comb_func.SetParLimits(13,ft.GammaGammaFit.GetParameter(3)-0.2*ft.GammaGammaFit.GetParameter(3),ft.GammaGammaFit.GetParameter(3)+0.2*ft.GammaGammaFit.GetParameter(3))
    ft.comb_func.FixParameter(13,ft.GammaGammaFit.GetParameter(3))
    ft.comb_func.FixParameter(14,ft.GammaGammaFit.GetParameter(4))
    #ft.comb_func.SetParLimits(14,ft.GammaGammaFit.GetParameter(4)-0.2*ft.GammaGammaFit.GetParameter(4),ft.GammaGammaFit.GetParameter(4)+0.2*ft.GammaGammaFit.GetParameter(4))
    ft.comb_func.FixParameter(15,ft.GammaGammaFit.GetParameter(5))
    #ft.comb_func.SetParLimits(15,ft.GammaGammaFit.GetParameter(5)-0.2*ft.GammaGammaFit.GetParameter(5),ft.GammaGammaFit.GetParameter(5)+0.2*ft.GammaGammaFit.GetParameter(5))

    ft.comb_func.SetLineColor(rt.kBlack)

    histogram.Fit(ft.comb_func,"R+","",2,5) # good with no gamma gamma parameter
    Gammalow = ft.GammaGammaFit.Clone("Gammalow")
    Gammalow.SetLineColor(rt.kBlack+2)
    Gammalow.SetParameters(19,1.73,1.51,5881,255,-170)
    Gammahigh = ft.GammaGammaFit.Clone("Gammahigh")
    Gammahigh.SetLineColor(rt.kGreen+3)
    Gammahigh.SetParameters(19,1.73,1.51,5881,255,-170)
    #histogram.Fit(Gammalow,"R+","",2,3)

    #histogram.Fit(Gammahigh,"R+","",4,6)


    GammaGammaFit_Clone = ft.GammaGammaFit.Clone()

    GammaGammaFit_Clone.SetParameters(ft.comb_func.GetParameter(10),ft.comb_func.GetParameter(11),ft.comb_func.GetParameter(12),ft.comb_func.GetParameter(13),ft.comb_func.GetParameter(14),ft.comb_func.GetParameter(15))
    GammaGammaFit_Clone.SetLineColor(rt.kGreen)
    GammaGammaFit_Clone.Draw("SAME")


    nparameter = 0
    while(nparameter<5):
        #print "this is running and filling "   , nparameter ,"parameter for jpsi with data fit" , ft.sig_func_jpsi_data.GetParameter(nparameter)
        sig_func_jpsi_data_clone.FixParameter(nparameter,ft.comb_func.GetParameter(nparameter))
        sig_func_psi_data_clone.FixParameter(nparameter,ft.comb_func.GetParameter(nparameter+5))

        nparameter = nparameter+1
    sig_func_psi_data_clone.Draw("SAME")
    sig_func_jpsi_data_clone.Draw("SAME")


    sig_func_jpsi_data_clone.SetLineColor(rt.kRed+2)

    sig_func_psi_data_clone.SetLineColor(rt.kBlue+1)



#crystalball function order "constant , mean , sigma , alpha , N"""
#                                 0      1       2      3      4
#                                 5      6       7      8      9
#                     ( "GammaGammaFit","[0]*TMath::Exp(-[1]*x)*( (x < [2]) ? 1 : 1 + [3]*(x-[2])*(x-[2]) + [4]*(x-[2])*(x-[2])*(x-[2]) +[5]*(x-[2])*(x-[2])*(x-[2])*(x-[2]))",2,5)
#                                 const 10 ,    b  11, mth 12 , a1 13, a2 14 , a3 15

# this line calculate the yeild and Background
    sigma_jpsi = ft.comb_func.GetParameter(2)
    mean_jpsi = ft.comb_func.GetParameter(1)
    range_high_jpsi = 6#mean_jpsi+2*sigma_jpsi
    range_low_jpsi = 2.2#mean_jpsi-2*sigma_jpsi
    #range_high_jpsi = mean_jpsi+3*sigma_jpsi
    #range_low_jpsi = mean_jpsi-3*sigma_jpsi


    sigma_psi =  ft.comb_func.GetParameter(7)
    mean_psi = ft.comb_func.GetParameter(6)
    range_high_psi = 6#mean_psi+2*sigma_psi
    range_low_psi = 2.2#mean_psi-2*sigma_psi

    #range_high_psi = mean_psi+sigma_psi
    #range_low_psi = mean_psi-sigma_psi
    psi_under_jpsi = sig_func_psi_data_clone.Integral(range_low_jpsi,range_high_jpsi)
    jpsi_under_psi = sig_func_jpsi_data_clone.Integral(range_low_jpsi,range_high_jpsi)

    yeild_psi =(ft.comb_func.Integral(range_low_psi,range_high_psi)-GammaGammaFit_Clone.Integral(range_low_psi,range_high_psi)-jpsi_under_psi)/bin_width  #this is my actual calculation
    #yeild_psi = sig_func_psi_data_clone.Integral(range_low_psi,range_high_psi)/bin_width #trying to get simone's result
    error_psi = (yeild_psi * ft.comb_func.GetParError(5))/ft.comb_func.GetParameter(5)

    yeild_psi_str = "{:.0f}".format(yeild_psi)
    error_psi_str = "{:.0f}".format(error_psi)

    yeild_jpsi = (ft.comb_func.Integral(range_low_jpsi,range_high_jpsi)-GammaGammaFit_Clone.Integral(range_low_jpsi,range_high_jpsi)-psi_under_jpsi)/bin_width #this is my actual calculation
    #yeild_jpsi = sig_func_jpsi_data_clone.Integral(range_low_jpsi,range_high_jpsi)/bin_width  #trying to get simone's result

    yeild_gammagamma = GammaGammaFit_Clone.Integral(range_low_jpsi,range_high_jpsi)/bin_width #this is my actual calculation
    #yeild_gammagamma = GammaGammaFit_Clone.Integral(2.2,6)/bin_width  #trying to get simone's result
    error_gammagamma = (yeild_gammagamma * ft.comb_func.GetParError(10))/ft.comb_func.GetParameter(10)

    error_jpsi = (yeild_jpsi * ft.comb_func.GetParError(0))/ft.comb_func.GetParameter(0) #+ error_gammagamma


#    if(reference_frame[nframe] == "colinsoper_tilde{#phi}" and i ==23):
#        print "this is the causing error for tildephi to explode on 24th bin" ft.comb_func.GetParError(0)


    yeild_jpsi_str = "{:.0f}".format(yeild_jpsi)
    error_jpsi_str = "{:.0f}".format(error_jpsi)

    yeild_gammagamma_str = "{:.0f}".format(yeild_gammagamma)
    error_gammagamma_str = "{:.0f}".format(error_gammagamma)
    #print "########################j" , jpsi_under_psi/0.05
    #print "########################", psi_under_jpsi/0.05

    #chisquare/ndf

    #chisq_ndf = ft.comb_func.GetChisquare()/ft.comb_func.GetNDF()
    chisq_ndf = ft.comb_func.GetChisquare()/ft.comb_func.GetNDF()

    chisq_ndf_str = "{:4.2f} / {:2d} = {:4.2f}".format(ft.comb_func.GetChisquare(),ft.comb_func.GetNDF(),chisq_ndf)

    #print "this line is also running #####################",yeild_jpsi , yeild_psi

    #histogram.Fit(ft.comb_func,"LR","",2,2.9)
    #tailclone = ft.tail_func.Clone("tailclone")
    #sigclone_psi  = ft.sig_func.Clone("sigclone_psi")
    #sigclone_jpsi  = ft.sig_func.Clone("sigclone_jpsi")



    #combclone = ft.comb_func.Clone("combclone")




    #tailclone.FixParameter(0,tail_func_parammeters[0])
    #tailclone.FixParameter(1,tail_func_parammeters[1])
    #tailclone.FixParameter(2,tail_func_parammeters[2])
    #tailclone.FixParameter(3,tail_func_parammeters[3])


    #sigclone_psi.FixParameter(0,ft.comb_func.GetParameter(0))
    #sigclone_psi.FixParameter(1,ft.sig_func.GetParameter(1))
    #sigclone_psi.FixParameter(2,ft.sig_func.GetParameter(2))
    #sigclone_psi.FixParameter(3,ft.sig_func.GetParameter(3))


    #combclone.FixParameter(0,ft.comb_func.GetParameter(0))
    #combclone.FixParameter(1,ft.comb_func.GetParameter(1))
    #combclone.FixParameter(2,ft.comb_func.GetParameter(2))
    #combclone.FixParameter(3,ft.comb_func.GetParameter(3))
    #combclone.FixParameter(4,ft.comb_func.GetParameter(4))
    #combclone.FixParameter(5,ft.comb_func.GetParameter(5))
    #combclone.FixParameter(6,ft.comb_func.GetParameter(6))
    #combclone.FixParameter(7,ft.comb_func.GetParameter(7))"""

    #tailclone.SetLineColor(rt.kRed)
    #sigclone_psi.SetLineColor(rt.kGreen)
    #combclone.SetLineColor(rt.kBlue)
    #tailclone.Draw("SAME")
    #sigclone_psi.Draw("SAME")
    #combclone.Draw("SAME")






    result=[]
    cut_clone = list(cut)
    for word in cut_clone[i].split("<"):
        #if word.isnumber():
        result.append(word)
        #print word
    #result = [int(d) for d in re.findall(r'-?\d+',cut_clone[i])]
    #print len(result)
    cut_high =result[2] #[-6:]
    cut_low =result[0]
    frame_name = []
    for frame_name_i in reference_frame[nframe].split("_"):
        #if word.isnumber():
        frame_name.append(frame_name_i)
        #print frame_name_i
        #framename_i
    #print "####################################################", result[1],result[2],result[3]
    #frame_name1 =
    #frame_name= "#phi_{{}}".format(reference_frame[nframe])
    #angle_frame_name =
    #cut_editor = "{}< #{}({})<{}".format(cut_low,frame_name[1],frame_name[0],cut_high) #this is to edit cut so that it appear nice on histogram
    func = TF1()
    filename_angle = TString()
    if (reference_frame[nframe] == "helicity_theta"):
        list_yeild_helicity_theta.append(yeild_jpsi)
        func = ft.wtheta.Clone("func")
        filename_angle = "helicity_theta"

    elif (reference_frame[nframe] == "helicity_phi"):
        list_yeild_helicity_phi.append(yeild_jpsi)
        func = ft.wphi.Clone("func")
        filename_angle = "helicity_phi"

    elif(reference_frame[nframe] == "colinsoper_phi"):
        list_yeild_colinsoper_phi.append(yeild_jpsi)
        func = ft.wphi.Clone("func")
        filename_angle = "colinsoper_phi"
     # list_angle_colinsoper_phi.append()
    elif(reference_frame[nframe] == "collinsoper_theta"):
        list_yeild_collinsoper_theta.append(yeild_jpsi)
        func = ft.wtheta.Clone("func")
        filename_angle = "collinsoper_theta"
      #list_angle_collinsoper_theta.append()
    elif(reference_frame[nframe] == "colinsoper_tilde{#phi}"):

        list_yeild_colinsoper_tildephi.append(yeild_jpsi)
        func = ft.wtildetheta.Clone("func")
        filename_angle = "colinsoper_tilde"
    elif(reference_frame[nframe] == "helicity_tilde{#phi}"):
        list_yeild_helicity_tilde.append(yeild_jpsi)
        func = ft.wtildetheta.Clone("func")
        filename_angle = "helicity_tilde"






    """
    list_angle_helicity_phi.append
    list_angle_helicity_theta.append
    list_angle_colinsoper_tildephi.append
    list_angle_helicity_tilde.append"""









    legend.SetHeader("UPC Run2 Dataset","C") # option "C" allows to center the header
    #legend.AddEntry(0,cut[i],"")

    #print error_jpsi_str
    print  yeild_jpsi_str
    new.write(0,0,"jpsi_yeild")
    new.write(0,1,"yeild_error")
    new.write(0,3,"bin")
    new.write(0,2,"chisq/ndf")
    new.write(i+1,3,cut[i])
    new.write(i+1,1,error_jpsi)
    new.write(i+1,0,yeild_jpsi)
    new.write(i+1,2,chisq_ndf)

    if(frame_name[1]=="theta"):
        cut_editor = "{}< cos#{}({})<{}".format(cut_low,frame_name[1],frame_name[0],cut_high) #this is to edit cut so that it appear nice on histogram
    else:
        cut_editor = "{}< #{}({})<{}".format(cut_low,frame_name[1],frame_name[0],cut_high) #this is to edit cut so that it appear nice on histogram

    legend.AddEntry(0,cut_editor,"")
    #legend.AddEntry(0,cut_editor,"")
    legend.AddEntry(0,"N_{j/\Psi}="+yeild_jpsi_str+" \pm "+error_jpsi_str ,"")
    legend.AddEntry(0,"N_{\Psi(2s)}="+yeild_psi_str+" \pm "+error_psi_str,"")
    legend.AddEntry(0,"N_{\gamma \gamma}="+yeild_gammagamma_str+" \pm "+error_gammagamma_str,"")
    legend.AddEntry(0,"#tilde{#chi}^{2} ="+chisq_ndf_str,"")
    print cut_editor
    #legend.AddEntry("tp","Gaussian with math.exponential and Polynomical background","P")
    #legend.AddEntry("HighPt_Mass",MassCut[0:16],"e2p")
    #cryst.SetParameter(0,const)
    legend.SetLineColor(0)
    legend.SetTextSize(0.025)
    legend.Draw("SAME")
    canvas.SaveAs("histo_test.pdf")
    canvas.Write()
    legend.Clear()



    nbin = angle_xmin+((angle_xmax-angle_xmin)*0.5)/angle_nbins + (i * (angle_xmax-angle_xmin))/angle_nbins
    #nbin = (i * (angle_xmax-angle_xmin))/angle_nbins
    angle_histogram.Fill(nbin,yeild_jpsi)
    angle_histogram.SetBinError(i+1,error_jpsi)


    #histogram.Write()

    #histogram.clear()
    #canvas.clear()
    print "checking if the parameters are set correctly"
    j = 0


    while j<16:
      ft.comb_func.SetParameter(j,ft.partest[j])
      print ft.comb_func.GetParameter(j), ft.partest[j]
      #if ft.comb_func.GetParameter(j) != partest[j]:
    #    print "parameter need to be set here" ,ft.comb_func.GetParameter(i),partest[i]


     # else:
    #    print "parameters donot need to be set"
      j = j+1

    #canvas.Clear()
    i = i+1
  #  if (i == len(cut)-1):
   #   break
  ##this is the best place to work on creating histograms for the angles
  #angle_bins= len(cut)
  angle_canvas.cd()
  angle_histogram.Draw()
  angle_histogram.SetDirectory(0)
  angle_histogram.Sumw2()



  #angle_canvas.SaveAs("angle.pdf")

  angle_canvas.Write()


  angle_canvas_corrected.cd()
  angle_histogram_corrected.Divide(angle_histogram,angle_histogram_axe)
  angle_histogram_corrected.SetDirectory(0)

  #if(reference_frame[nrame]=="collinsoper_phi")

  angle_histogram_corrected.Fit(func,"NRQM")


  angle_histogram_corrected.Draw("SAME")

  #par_1 = str(func.GetParameter(1))
  #par_2 = str(func.GetParameter(2))


 # chi_ndf_angle = str(func.GetChisquare()/func.GetNDF())


  #legend_angle.AddEntry(0,"#lambda_{#theta} "+ par_1,"")
  #legend_angle.AddEntry(0,"#lambda_{#phi} "+ par_2,"")


  #legend_angle.AddEntry(0,"#tilde{#chi}^{2}"+chi_ndf_angle,"")

  #legend_angle.Draw("SAME")

  angle_histogram_corrected.Write()
  angle_canvas_corrected.Write()
  angle_canvas_axe.Write()
  angle_canvas_rec.Write()
  angle_canvas_gen.Write()
  legend_angle.Clear()
  angle_canvas_corrected.SaveAs("{}_{}.pdf".format(filename_angle,i))



  folder.cd("../")



  #if(reference_frame[nframe] == "colinsoper_phi"):


      #angle_histogram.Sumw2()

      #angle_canvas_clone = TCanvas("angle_canvas_clone","angle_canvas_clone",600,300)
      #angle_histogram_clone = TH1F("angle_histogram_clone","angle_histogram_clone",angle_nbins,angle_xmin,angle_xmax)
      #angle_histogram_clone.clear()
      #angle_canvas_clone.clear()




  nframe = nframe+1
  #histogram.Draw()
  #canvas.Write()
  #cos phi





wk.save("xlwt data.xlsx")
file2.Write()
#tree.delete()

file2.Close()

# Mass

#The lines below are so that pyroot do not exit on completing the analysis
vars = globals()
vars.update(locals())
shell = code.InteractiveConsole(vars)
shell.interact()
