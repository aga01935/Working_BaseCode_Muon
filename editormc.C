#include <iostream>
#include "TMath.h"
#include "TH1F.h"

using namespace std;
void editormc()
{
  TLorentzVector *fRecPair_Parent;
  TLorentzVector *fMCPair_Parent;
  TLorentzVector *fRec_ConnectedMCPair_Parent;
  Float_t fRecCollinPhi;
  Float_t fRecHelicityPhi;
  Float_t fRecCollinTheta;
  Float_t fRecHelicityTheta;
  Float_t fRecHelicityTildePhi;
  Float_t fRecCollinTildePhi;
  Float_t fMCCollinPhi;
  Float_t fMCHelicityPhi;
  Float_t fMCCollinTheta;
  Float_t fMCHelicityTheta;
  Float_t fMCHelicityTildePhi;
  Float_t fMCCollinTildePhi;

  Float_t fSimulated_Reconstructed_CollinPhi;
  Float_t fSimulated_Reconstructed_HelicityPhi;
  Float_t fSimulated_Reconstructed_CollinTheta;
  Float_t fSimulated_Reconstructed_HelicityTheta;
  Float_t fSimulated_Reconstructed_HelicityTildePhi;
  Float_t fSimulated_Reconstructed_CollinTildePhi;


  TFile *file = new TFile("/home/amrit/Analysis/TestCode/nano/CombineData/AnalysisResults_Simulated_JPsi.root");
  if(!file) {cout<<"nofilefound"<<endl;}
  file->ls();
  TTree *tree = (TTree*)file->Get("PolarizationJP/fRecTree");
  if(!tree) {cout<<"no reconstructed tree found"<<endl;}
  TTree *gentree = (TTree*)file->Get("PolarizationJP/fGenTree");
  if(!gentree) {cout<<"no generated tree found"<<endl;}
  TH1F *histogram = new TH1F("histogram","histogram",1000,0,7);
  TCanvas *canvas = new TCanvas();

  Int_t entries = tree->GetEntries();
  cout <<entries<<endl;

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


 //gentree->SetBranchAddress("fMCPair_Parent",&fMCPair_Parent);
 gentree->SetBranchAddress("fMCCollinPhi",&fMCCollinPhi);
 gentree->SetBranchAddress("fMCCollinTheta",&fMCCollinTheta);
 gentree->SetBranchAddress("fMCHelicityPhi",&fMCHelicityPhi);
 gentree->SetBranchAddress("fMCHelicityTheta",&fMCHelicityTheta);
 gentree->SetBranchAddress("fMCHelicityTildePhi",&fMCHelicityTildePhi);
 gentree->SetBranchAddress("fMCCollinTildePhi",&fMCCollinTildePhi);


 //tree->SetBranchAddress("fRec_ConnectedMCPair_Parent",&fRec_ConnectedMCPair_Parent);
 tree->SetBranchAddress("fSimulated_Reconstructed_CollinPhi",&fSimulated_Reconstructed_CollinPhi);
 tree->SetBranchAddress("fSimulated_Reconstructed_CollinTheta",&fSimulated_Reconstructed_CollinTheta);
 tree->SetBranchAddress("fSimulated_Reconstructed_HelicityPhi",&fSimulated_Reconstructed_HelicityPhi);
 tree->SetBranchAddress("fSimulated_Reconstructed_HelicityTheta",&fSimulated_Reconstructed_HelicityTheta);
 tree->SetBranchAddress("fSimulated_Reconstructed_HelicityTildePhi",&fSimulated_Reconstructed_HelicityTildePhi);
 tree->SetBranchAddress("fSimulated_Reconstructed_CollinTildePhi",&fSimulated_Reconstructed_CollinTildePhi);




  //tree->SetBranchAddress("fRecPair_Parent",&fRecPair_Parent);


//cout<< "this is working";

//  Double_t fRecCollinTildePhi;
  //Double_t fRecHelicityTildePhi;
  TFile *TildePhiMC = new TFile("TildePhiMC.root","RECREATE");
  TTree *tildephi = new TTree("tildephi","tildephi");
  TTree *tildephigen = new TTree("tildephigen","tildephigen");
  Float_t fRecCollinTildePhiMC_corrected;
  Float_t fRecHelicityTildePhiMC_corrected;
  Float_t fMCCollinTildePhi_corrected;
  Float_t fMCHelicityTildePhi_corrected;
  Float_t fSimulated_Reconstructed_CollinTildePhi_corrected;
  Float_t fSimulated_Reconstructed_HelicityTildePhi_corrected;

  tildephi->Branch("fRecCollinTildePhiMC_corrected",&fRecCollinTildePhiMC_corrected,"fRecCollinTildePhiMC_corrected/f");
  tildephi->Branch("fRecHelicityTildePhiMC_corrected",&fRecHelicityTildePhiMC_corrected,"fRecHelicityTildePhiMC_corrected/f");
  tildephi->Branch("fSimulated_Reconstructed_CollinTildePhi_corrected",&fSimulated_Reconstructed_CollinTildePhi_corrected,"fSimulated_Reconstructed_CollinTildePhi_corrected/f");
  tildephi->Branch("fSimulated_Reconstructed_HelicityTildePhi_corrected",&fSimulated_Reconstructed_HelicityTildePhi_corrected,"fSimulated_Reconstructed_HelicityTildePhi_corrected/f");


  tildephigen->Branch("fMCCollinTildePhi_corrected",&fMCCollinTildePhi_corrected,"fMCCollinTildePhi_corrected/f");
  tildephigen->Branch("fMCHelicityTildePhi_corrected",&fMCHelicityTildePhi_corrected,"fMCHelicityTildePhi_corrected/f");
  //tildephi->Branch("fRecPair_Parent_daughter")
  //TildePhi->Write();

  for(Int_t i=0;i<entries;i++)
    {
    tree->GetEntry(i);
    //cout<<i<<"TildePhi values" << fRecCollinTildePhi << endl;

    //cout<<"tildephi values"<< endl;



    if(fSimulated_Reconstructed_CollinTheta<0)
      {
      fSimulated_Reconstructed_CollinTildePhi_corrected = fSimulated_Reconstructed_CollinPhi- 0.75* TMath::Pi();
      }
    else
      {
      fSimulated_Reconstructed_CollinTildePhi_corrected = fSimulated_Reconstructed_CollinPhi- 0.25* TMath::Pi();
      }
  if (fSimulated_Reconstructed_CollinTildePhi_corrected<0){
    fSimulated_Reconstructed_CollinTildePhi_corrected = fSimulated_Reconstructed_CollinTildePhi_corrected+ 2*TMath::Pi();

   }

    if (fSimulated_Reconstructed_HelicityTheta<0)
      {
      fSimulated_Reconstructed_HelicityTildePhi_corrected = fSimulated_Reconstructed_HelicityPhi- 0.75* TMath::Pi();
      }



    else
      {
      fSimulated_Reconstructed_HelicityTildePhi_corrected = fSimulated_Reconstructed_HelicityPhi- 0.25* TMath::Pi();
      }

  if(fSimulated_Reconstructed_HelicityTildePhi_corrected<0){

      fSimulated_Reconstructed_HelicityTildePhi_corrected = fSimulated_Reconstructed_HelicityTildePhi_corrected + 2* TMath::Pi();
  }










    if(fRecCollinTheta<0)
      {
      fRecCollinTildePhiMC_corrected = fRecCollinPhi- 0.75* TMath::Pi();
      }


    else
      {
      fRecCollinTildePhiMC_corrected = fRecCollinPhi- 0.25* TMath::Pi();
      }
  if (fRecCollinTildePhiMC_corrected<0){
    fRecCollinTildePhiMC_corrected = fRecCollinTildePhiMC_corrected+ 2*TMath::Pi();

   }

    if (fRecHelicityTheta<0)
      {
      fRecHelicityTildePhiMC_corrected = fRecHelicityPhi- 0.75* TMath::Pi();
      }
    else
      {
      fRecHelicityTildePhiMC_corrected = fRecHelicityPhi- 0.25* TMath::Pi();
      }

  if(fRecHelicityTildePhiMC_corrected<0){

      fRecHelicityTildePhiMC_corrected = fRecHelicityTildePhiMC_corrected + 2* TMath::Pi();


  }

      //cout<< "costheta is" <<fRecCollinTheta<<","<<"phi is"<<fRecCollinPhi<<endl;
    //  cout<<  fRecCollinTildePhi_corrected<<","<<fRecCollinTildePhi<<endl;

      histogram->Fill(fRecCollinTildePhiMC_corrected);
      tildephi->Fill();
    //TildePhi->Write();

    }

//Int_t entries2 = gentree->GetEntries();

    for(Int_t j=0;j<gentree->GetEntries();j++)
        {
        gentree->GetEntry(j);
      //  cout<<j<<"Phi values" << fMCCollinPhi << endl;

        //cout<<"tildephi values"<< fMCCollinTildePhi <<endl;


        if(fMCCollinTheta<0)
          {
          fMCCollinTildePhi_corrected = fMCCollinPhi- 0.75* TMath::Pi();
          }
        else
          {
          fMCCollinTildePhi_corrected = fMCCollinPhi- 0.25* TMath::Pi();
          }
      if (fMCCollinTildePhi_corrected<0){
        fMCCollinTildePhi_corrected = fMCCollinTildePhi_corrected+ 2*TMath::Pi();

       }

       cout<<"corrected values"<<fMCCollinTildePhi_corrected<<endl;




      if (fMCHelicityTheta<0){
          fMCHelicityTildePhi_corrected = fMCHelicityPhi- 0.75* TMath::Pi();
          }


      else
          {
          fMCHelicityTildePhi_corrected = fMCHelicityPhi- 0.25* TMath::Pi();
          }

      if(fMCHelicityTildePhi_corrected<0){

          fMCHelicityTildePhi_corrected = fMCHelicityTildePhi_corrected + 2* TMath::Pi();


      }

        //  cout<< "costheta is" <<fMCCollinTheta<<","<<"phi is"<<fMCCollinPhi<<endl;
          //cout<<  fMCCollinTildePhi_corrected<<","<<fMCCollinTildePhi<<endl;

        //  histogram->Fill(fMCCollinTildePhi_corrected);
          tildephigen->Fill();
        //TildePhi->Write();

      }



  //canvas->cd();
  //histogram->Draw("e");
  //canvas->SaveAs("tildephi_test.pdf");
  //tildephi->Write();
  TildePhiMC->Write();
//  TildePhi->Close();





  }
