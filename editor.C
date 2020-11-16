#include <iostream>
#include "TMath.h"
#include "TH1F.h"
using namespace std;
void editor()
{
  TLorentzVector *fRecPair_Parent;
  Float_t fRecCollinPhi;
  Float_t fRecHelicityPhi;
  Float_t fRecCollinTheta;
  Float_t fRecHelicityTheta;
  Float_t fRecHelicityTildePhi;
  Float_t fRecCollinTildePhi;
  //TFile *file = new TFile("/home/amrit/Analysis/MyTestCode2/Data/combinedata/AnalysisResults_combined_AllTrigger.root");
  TFile *file = new TFile("/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults_Simulated_JPsi.root");
  TTree *tree = (TTree*)file->Get("PolarizationJP/fRecTree");
  TH1F *histogram = new TH1F("histogram","histogram",1000,0,7);
  TCanvas *canvas = new TCanvas();

//  tree->SetBranchAddress("fRecCollinTildePhi",&fRecCollinTildePhi);
  //tree->SetBranchAddress("fRecHelicityTildePhi",&fRecHelicityTildePhi);
//  tree->SetBranchAddress("fRecPair_Parent",&fRecPair_Parent);
 tree->SetBranchAddress("fRecPair_Parent",&fRecPair_Parent);
 tree->SetBranchAddress("fRecCollinPhi",&fRecCollinPhi);
 tree->SetBranchAddress("fRecCollinTheta",&fRecCollinTheta);
 tree->SetBranchAddress("fRecHelicityPhi",&fRecHelicityPhi);
 tree->SetBranchAddress("fRecHelicityTheta",&fRecHelicityTheta);
 tree->SetBranchAddress("fRecHelicityTildePhi",&fRecHelicityTildePhi);
 tree->SetBranchAddress("fRecCollinTildePhi",&fRecCollinTildePhi);



  //tree->SetBranchAddress("fRecPair_Parent",&fRecPair_Parent);


  Double_t entries = tree->GetEntries();
  cout <<entries<<endl;

//  Double_t fRecCollinTildePhi;
  //Double_t fRecHelicityTildePhi;
  //TFile *TildePhi = new TFile("TildePhi.root","RECREATE");
  TFile *TildePhiMC = new TFile("TildePhiMC.root","RECREATE");
  TTree *tildephi = new TTree("tildephi","tildephi");
  Float_t fRecCollinTildePhi_corrected;
  Float_t fRecHelicityTildePhi_corrected;
  tildephi->Branch("fRecCollinTildePhi_corrected",&fRecCollinTildePhi_corrected,"fRecCollinTildePhi_corrected/f");
  tildephi->Branch("fRecHelicityTildePhi_corrected",&fRecHelicityTildePhi_corrected,"fRecHelicityTildePhi_corrected/f");
  //tildephi->Branch("fRecPair_Parent_daughter")
  //TildePhi->Write();

  for(int i=0;i<entries;i++)
    {
    tree->GetEntry(i);
    //cout<<i<<"TildePhi values" << fRecCollinTildePhi << endl;

    //cout<<"tildephi values"<< fRecCollinTildePhi <<endl;
    if(fRecCollinTheta<0)
      {
      fRecCollinTildePhi_corrected = fRecCollinPhi- 0.75* TMath::Pi();
      }
    else
      {
      fRecCollinTildePhi_corrected = fRecCollinPhi- 0.25* TMath::Pi();
      }
  if (fRecCollinTildePhi_corrected<0){
    fRecCollinTildePhi_corrected = fRecCollinTildePhi_corrected+ 2*TMath::Pi();

   }

    if (fRecHelicityTheta<0)
      {
      fRecHelicityTildePhi_corrected = fRecHelicityPhi- 0.75* TMath::Pi();
      }




    else
      {
      fRecHelicityTildePhi_corrected = fRecHelicityPhi- 0.25* TMath::Pi();
      }

  if(fRecHelicityTildePhi_corrected<0){

      fRecHelicityTildePhi_corrected = fRecHelicityTildePhi_corrected + 2* TMath::Pi();


  }

      cout<< "costheta is" <<fRecCollinTheta<<","<<"phi is"<<fRecCollinPhi<<endl;
      cout<<  fRecCollinTildePhi_corrected<<","<<fRecCollinTildePhi<<endl;

      histogram->Fill(fRecCollinTildePhi_corrected);
      tildephi->Fill();
    //TildePhi->Write();

    }

  canvas->cd();
  histogram->Draw("e");
  canvas->SaveAs("tildephi_test.pdf");
  //tildephi->Write();
  TildePhiMC->Write();
//  TildePhi->Close();




  }
