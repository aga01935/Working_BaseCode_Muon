/************************************************************************** * Copyright(c) 1998-1999, ALICE Experiment at CERN, All rights reserved. *
 *                                                                        *
 * Author: The ALICE Off-line Project.                                    *
 * Contributors are mentioned in the code where appropriate.              *
 *                                                                        *
 * Permission to use, copy, modify and distribute this software and its   *
 * documentation strictly for non-commercial purposes is hereby granted   *
 * without fee, provided that the above copyright notice appears in all   *
 * copies and that both the copyright notice and this permission notice   *
 * appear in the supporting documentation. The authors make no claims     *
 * about the suitability of this software for any purpose. It is          *
 * provided "as is" without express or implied warranty.                  *
 **************************************************************************/

// c++ headers
#include <iostream>
#include <fstream>
#include <map>

// root headers
#include <TMath.h>
#include <TH1I.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TFile.h>
#include <TF2.h>
#include <TF1.h>
#include <TRandom.h>
#include <TGraph.h>
#include <TLegend.h>
#include <TGraphErrors.h>
#include <TPad.h>
#include <TCanvas.h>
#include <TStyle.h>
#include <TTree.h>
#include <TGraph2D.h>
#include <TStopwatch.h>
#include <TMatrixDSym.h>
#include <TFitResult.h>
#include <TLatex.h>
#include <TClonesArray.h>
#include <TDatabasePDG.h>
#include <TLorentzVector.h>
#include <TParticle.h>
#include <TObjString.h>
#include <TList.h>
#include <TChain.h>

// aliroot headers
#include <AliAnalysisTask.h>
#include <AliAnalysisManager.h>
#include <AliAODEvent.h>
#include <AliMCEvent.h>
#include <AliMCParticle.h>
#include <AliAODMCParticle.h>
#include <AliAODInputHandler.h>
#include <AliMuonTrackCuts.h>





// my headers
#include "AliAnalysisTaskPolarizationGeneral.h"
// ----------------------------------------------------------------------------------------------------------------------------------
class AliAnalysisTaskPolarizationGeneral;    // your analysis class

using namespace std;            // std namespace: so you can do things like 'cout'



ClassImp(AliAnalysisTaskPolarizationGeneral) // classimp: necessary for root

// ----------------------------------------------------------------------------------------------------------------------------------
AliAnalysisTaskPolarizationGeneral::AliAnalysisTaskPolarizationGeneral() : AliAnalysisTaskSE(),
  //events
  fAOD(0),fRunNumber(0),fMuonTrackCuts(0x0),fTrgRunNum(0),fMC(0),fTracklets(0)
  //output list
  ,fOutputList(0)


  //trees
  //,fRecTree(0),fGenTree(0),fTrgTree(0)
  //reconstructed lorentz vectors

  //,fRecPosDaughter(0.,0.,0.,0.) ,fRecNegDaughter(0.,0.,0.,0.) ,fRecPair_Parent(0.,0.,0.,0.)
  ,fRecDaughter1(0.,0.,0.,0.) ,fRecDaughter2(0.,0.,0.,0.) ,fRecPair_Parent(0.,0.,0.,0.)
  ,fRecParentMassH(0)
  ,fRecParentPtH(0)
  ,fRecParentRapH(0)
  //mc that corresponds to reconstructed lorentz vectors

  //,fRec_ConnectedMCPosDaughter(0.,0.,0.,0.) ,fRec_ConnectedMCNegDaughter(0.,0.,0.,0.) ,fRec_ConnectedMCPair_Parent(0.,0.,0.,0.)


  //simulated lorentz vectors


  //,fMCPosDaughter(0.,0.,0.,0.), fMCNegDaughter(0.,0.,0.,0.) , fMCPair_Parent(0.,0.,0.,0.)

  //invariant mass of the pairs
//  ,fRecPair_ParentMass(0),fMCPair_ParenttMass(0),fRec_ConnectedMCPair_ParenttMass(0)

  //histograms in outptlist
  ,fCounterH(0)
  ,fNumberofTracks(0)
  ,fPairNumber(0)
  ,fRecRabs(0)
  ,fRecEta(0)
  ,fRecCharge(0)
  //runnumber counter
  , fHistRunCounter(0)
  //trigger histograms
//  ,fHistCMUPTriggers(0),fHistCMUP6Triggers(0),fHistCMUP10Triggers(0),fHistCMUP11Triggers(0),fHistCMUP13Triggers(0),fHistCMUP26Triggers(0)


  //trigger branches
  //,fCMUP(-10),fCMUP6(-10), fCMUP10(-10), fCMUP11(-10),fCMUP13(-10),fCMUP26(-10)
//  ,fCMUPDecision(-10),fCMUP6Decision(-10), fCMUP10Decision(-10), fCMUP11Decision(-10),fCMUP13Decision(-10),fCMUP26Decision(-10)

 //ANGULAR DISTRIBUTIONS
 //,fSimulated_Reconstructed_HelicityTheta(-999),fSimulated_Reconstructed_CollinTheta(-999),fSimulated_Reconstructed_HelicityPhi(-999)
 //,fSimulated_Reconstructed_CollinPhi(-999),fSimulated_Reconstructed_CollinTildePhi(-999),fSimulated_Reconstructed_HelicityTildePhi(-999)

//  ,fMCHelicityTheta(-999),fMCCollinTheta(-999),fMCCollinTildePhi(-999),fMCHelicityPhi(-999),fMCCollinPhi(-999),fMCHelicityTildePhi(-999)
 //,fRecHelicityTheta(-999),fRecCollinTheta(-999),fRecCollinTildePhi(-999),fRecHelicityPhi(0),fRecCollinPhi(-999),fRecHelicityTildePhi(-999)
  //zdc energy storage
 //,fZNCEnergy(0),fZNAEnergy(0)//,fZNATDC(0),fZNCTDC(0)
 //,fLumiPerRun(0)
 ,fV0ADecision(-10)
 ,fV0CDecision(-10)
 ,fADADecision(-10)
 ,fADCDecision(-10)

{
  // default constructor, don't allocate memory here!
  // this is used by root for IO purposes, it needs to remain empty
}
// ----------------------------------------------------------------------------------------------------------------------------------
AliAnalysisTaskPolarizationGeneral::AliAnalysisTaskPolarizationGeneral(const char* name) : AliAnalysisTaskSE(name),

  fAOD(0),fRunNumber(0),fMuonTrackCuts(0x0),fTrgRunNum(0),fMC(0),fTracklets(0)
  //output list
  ,fOutputList(0)
  //trees
  //,fRecTree(0),fGenTree(0),fTrgTree(0)
  //reconstructed lorentz vectors

  //,fRecPosDaughter(0.,0.,0.,0.), fRecNegDaughter(0.,0.,0.,0.) , fRecPair_Parent(0.,0.,0.,0.)
  ,fRecDaughter1(0.,0.,0.,0.) ,fRecDaughter2(0.,0.,0.,0.) ,fRecPair_Parent(0.,0.,0.,0.)
  //simuated particles that corresponds to reconstructed ---> lorentz vectors
  ,fRecParentMassH(0)
  ,fRecParentPtH(0)
  ,fRecParentRapH(0)
  //,fRec_ConnectedMCPosDaughter(0.,0.,0.,0.), fRec_ConnectedMCNegDaughter(0.,0.,0.,0.) , fRec_ConnectedMCPair_Parent(0.,0.,0.,0.)


  //simulated lorentz vectors


//   ,fMCPosDaughter(0.,0.,0.,0.), fMCNegDaughter(0.,0.,0.,0.) , fMCPair_Parent(0.,0.,0.,0.)

   //invariant mass of the pairs
//  ,fRecPair_ParentMass(0),fMCPair_ParenttMass(0),fRec_ConnectedMCPair_ParenttMass(0)




  //histograms in outptlist
  ,fCounterH(0)
  ,fNumberofTracks(0)
  ,fPairNumber(0)
  ,fRecRabs(0)
  ,fRecEta(0)
  ,fRecCharge(0)


  //runcounters
  , fHistRunCounter(0)
  //trigger histograms
  //,fHistCMUPTriggers(0),fHistCMUP6Triggers(0),fHistCMUP10Triggers(0),fHistCMUP11Triggers(0),fHistCMUP13Triggers(0),fHistCMUP26Triggers(0)

  //trigger branches
  //,fCMUP(-10),fCMUP6(-10), fCMUP10(-10), fCMUP11(-10),fCMUP13(-10),fCMUP26(-10)
  //,fCMUPDecision(-10),fCMUP6Decision(-10), fCMUP10Decision(-10), fCMUP11Decision(-10),fCMUP13Decision(-10),fCMUP26Decision(-10)

  //ANGULAR DISTRIBUTIONS
 //,fSimulated_Reconstructed_HelicityTheta(-999),fSimulated_Reconstructed_CollinTheta(-999),fSimulated_Reconstructed_HelicityPhi(-999)
 //,fSimulated_Reconstructed_CollinPhi(-999),fSimulated_Reconstructed_CollinTildePhi(-999),fSimulated_Reconstructed_HelicityTildePhi(-999)

  //,fMCHelicityTheta(-999),fMCCollinTheta(-999),fMCCollinTildePhi(-999),fMCHelicityPhi(-999),fMCCollinPhi(-999),fMCHelicityTildePhi(-999)
 //,fRecHelicityTheta(-999),fRecCollinTheta(-999),fRecCollinTildePhi(-999),fRecHelicityPhi(0),fRecCollinPhi(-999),fRecHelicityTildePhi(-999)


  //zdc energy storage
 //,fZNCEnergy(0),fZNAEnergy(0)//,fZNATDC(0),fZNCTDC(0)
 //,fLumiPerRun(0)
 ,fV0ADecision(-10)
 ,fV0CDecision(-10)
 ,fADADecision(-10)
 ,fADCDecision(-10)



{


// constructor
  DefineInput(0, TChain::Class());
//  DefineOutput(1, TTree::Class());
  DefineOutput(1, TList::Class());
  //DefineOutput(1, TList::Class());
  //DefineOutput(3, TTree::Class());
  //DefineOutput(4, TTree::Class());


}
// ----------------------------------------------------------------------------------------------------------------------------------
AliAnalysisTaskPolarizationGeneral::~AliAnalysisTaskPolarizationGeneral()
{

  // destructor
  // liberate all allocated memory
  if(fOutputList)         {delete fOutputList;}
  if(fMuonTrackCuts)      {delete fMuonTrackCuts;}
//  if(fRecTree)            {delete fRecTree;}
//  if(fGenTree)            {delete fGenTree;}
//  if(fTrgTree)            {delete fTrgTree;}
  if(fCounterH)           {delete fCounterH;}
  if(fHistRunCounter)     {delete fHistRunCounter;}
  if(fNumberofTracks)     {delete fNumberofTracks;}
  if(fRecCharge)           {delete fRecCharge;}
  if(fRecEta)           {delete fRecEta;}
  if(fPairNumber)           {delete fPairNumber;}
  if(fRecRabs)           {delete fRecRabs;}
  //if(fHistCMUPTriggers)   {delete fHistCMUPTriggers;}
  //if(fHistCMUP6Triggers)  {delete fHistCMUP6Triggers;}
  //if(fHistCMUP10Triggers) {delete fHistCMUP10Triggers;}
  //if(fHistCMUP11Triggers) {delete fHistCMUP11Triggers;}
//  if(fHistCMUP13Triggers) {delete fHistCMUP13Triggers;}
//  if(fHistCMUP26Triggers) {delete fHistCMUP26Triggers;}




}
// ----------------------------------------------------------------------------------------------------------------------------------
void AliAnalysisTaskPolarizationGeneral::UserCreateOutputObjects()
{

  /*
  contains muons track cuts

  */

  fMuonTrackCuts = new AliMuonTrackCuts("StdMuonCuts", "StdMuonCuts");
  fMuonTrackCuts->SetFilterMask(AliMuonTrackCuts::kMuEta | AliMuonTrackCuts::kMuPdca | AliMuonTrackCuts::kMuMatchLpt);
  fMuonTrackCuts->SetAllowDefaultParams(kTRUE);
  fMuonTrackCuts->Print("mask");


  /*fRecTree = new TTree("fRecTree", "fRecTree");

  fRecTree->Branch("fRecPosDaughter","TLorentzVector",&fRecPosDaughter);
  fRecTree->Branch("fRecNegDaughter","TLorentzVector",&fRecNegDaughter);
  fRecTree->Branch("fRecPair_Parent","TLorentzVector",&fRecPair_Parent);


  fRecTree ->Branch("fRecCollinTildePhi", &fRecCollinTildePhi, "fRecCollinTildePhi/F");
  fRecTree ->Branch("fRecHelicityTildePhi", &fRecHelicityTildePhi, "fRecHelicityTildePhi/F");

  fRecTree ->Branch("fRecHelicityTheta", &fRecHelicityTheta, "fRecHelicityTheta/F");
  fRecTree ->Branch("fRecHelicityPhi", &fRecHelicityPhi, "fRecHelicityPhi/F");

  fRecTree ->Branch("fRecCollinTheta", &fRecCollinTheta, "fRecCollinTheta/F");
  fRecTree ->Branch("fRecCollinPhi", &fRecCollinPhi, "fRecCollinPhi/F");

  fRecTree ->Branch("fRecPair_ParentMass", &fRecPair_ParentMass, "fRecPair_ParentMass/F");


   fRecTree ->Branch("fZNCEnergy", &fZNCEnergy, "fZNCEnergy/F");
  fRecTree ->Branch("fZNAEnergy", &fZNAEnergy, "fZNAEnergy/F");
  // fRecTree ->Branch("fZPCEnergy", &fZPCEnergy, "fZPCEnergy/D");
  // fRecTree ->Branch("fZPAEnergy", &fZPAEnergy, "fZPAEnergy/D");
  fRecTree ->Branch("fZNATDC", &fZNATDC[0], "fZNATDC[4]/F");
  fRecTree ->Branch("fZNCTDC", &fZNCTDC[0], "fZNCTDC[4]/F");
  // fRecTree ->Branch("fZPATDC", &fZPATDC[0], "fZPATDC[4]/D");



  fGenTree = new TTree("fGenTree", "fGenTree");






  //if(fIsMC){

    fRecTree->Branch("fRec_ConnectedMCPosDaughter","TLorentzVector",&fRec_ConnectedMCPosDaughter);
    fRecTree->Branch("fRec_ConnectedMCNegDaughter","TLorentzVector",&fRec_ConnectedMCNegDaughter);
    fRecTree->Branch("fRec_ConnectedMCPair_Parent","TLorentzVector",&fRec_ConnectedMCPair_Parent);


   fRecTree ->Branch("fSimulated_Reconstructed_CollinTildePhi", &fSimulated_Reconstructed_CollinTildePhi,"fSimulated_Reconstructed_CollinTildePhi/F");

    fRecTree ->Branch("fSimulated_Reconstructed_HelicityTildePhi", &fSimulated_Reconstructed_HelicityTildePhi,"fSimulated_Reconstructed_HelicityTildePhi/F");

    fRecTree ->Branch("fSimulated_Reconstructed_HelicityTheta", &fSimulated_Reconstructed_HelicityTheta,"fSimulated_Reconstructed_HelicityTheta/F");
    fRecTree ->Branch("fSimulated_Reconstructed_HelicityPhi", &fSimulated_Reconstructed_HelicityPhi,"fSimulated_Reconstructed_HelicityPhi/F");

    fRecTree ->Branch("fSimulated_Reconstructed_CollinTheta", &fSimulated_Reconstructed_CollinTheta,"fSimulated_Reconstructed_CollinTheta/F");

    fRecTree ->Branch("fSimulated_Reconstructed_CollinPhi", &fSimulated_Reconstructed_CollinPhi,"fSimulated_Reconstructed_CollinPhi/F");
    fRecTree ->Branch("fRec_ConnectedMCPair_ParenttMass", &fRec_ConnectedMCPair_ParenttMass, "fRec_ConnectedMCPair_ParenttMass/F");




    fGenPart = new TClonesArray("TParticle", 1000);



    fGenTree->Branch("fMCPosDaughter","TLorentzVector",&fMCPosDaughter);
    fGenTree->Branch("fMCNegDaughter","TLorentzVector",&fMCNegDaughter);
    fGenTree->Branch("fMCPair_Parent","TLorentzVector",&fMCPair_Parent);

    fGenTree->Branch("fMCPair_ParenttMass", &fMCPair_ParenttMass, "fMCPair_ParenttMass/F");



    fGenTree ->Branch("fMCHelicityTildePhi", &fMCHelicityTildePhi, "fMCHelicityTildePhi/F");
    fGenTree ->Branch("fMCCollinTildePhi", &fMCCollinTildePhi, "fMCCollinTildePhi/F");
    fGenTree ->Branch("fMCHelicityTheta", &fMCHelicityTheta, "fMCHelicityTheta/F");
    fGenTree ->Branch("fMCHelicityPhi", &fMCHelicityPhi, "fMCHelicityPhi/F");

    fGenTree ->Branch("fMCCollinTheta", &fMCCollinTheta, "fMCCollinTheta/F");
    fGenTree ->Branch("fMCCollinPhi", &fMCCollinPhi, "fMCCollinPhi/F");


//  }

  fTrgTree = new TTree("fTrgTree", "fTrgTree");

//  if(!fIsMC){


    fTrgTree ->Branch("fTrgRunNum", &fTrgRunNum, "fTrgRunNum/I");
    fTrgTree ->Branch("fCMUP", &fCMUP, "fCMUP/I");
    fTrgTree ->Branch("fCMUP6", &fCMUP6, "fCMUP6/I");
    fTrgTree ->Branch("fCMUP10", &fCMUP10, "fCMUP10/I");
    fTrgTree ->Branch("fCMUP11", &fCMUP11, "fCMUP11/I");
    fTrgTree ->Branch("fCMUP13", &fCMUP13, "fCMUP13/I");
    fTrgTree ->Branch("fCMUP26", &fCMUP26, "fCMUP26/I");
//  }
*/





  fOutputList = new TList();          // this is a list which will contain all  histograms
  fOutputList->SetOwner(kTRUE);       // memory stuff: the list is owner of all objects it contains and will delete them


  fCounterH = new TH1F("fCounterH", "fCounterH", 25, 0., 25.);
  fOutputList->Add(fCounterH);
  fRecParentMassH = new TH1F("fRecParentMassH", "Mass", 30, 2.,5.);
  fOutputList->Add(fRecParentMassH);
  fRecParentPtH = new TH1F("fRecParentPtH", "Pt", 30, 0.,1.);
  fOutputList->Add(fRecParentPtH);

  fRecParentRapH = new TH1F("fRecParentRapH", "Rapidity", 50, -5.,5.);
  fOutputList->Add(fRecParentRapH);


  fNumberofTracks = new TH1F("fNumberofTracks","Number of Tracks",5,0,5);
  fOutputList->Add(fNumberofTracks);
  fPairNumber = new TH1F("fPairNumber","Number of Pairs",5,0,5);
  fOutputList->Add(fPairNumber);
  fRecRabs = new  TH1F("fRecRabs","Rabs value",100,0,100);
  fOutputList->Add(fRecRabs);
  fRecEta = new TH1F("fRecEta", "Eata",100,-10,-1);
  fOutputList->Add(fRecEta);
  fRecCharge= new TH1F("fRecCharge","product of charge of pair of tracks",10,-3,3);
  fOutputList->Add(fRecCharge);


  fHistRunCounter = new TH1D("fHistRunCounter","Counter", 70000, 240000.5, 310000.5);
  fOutputList->Add(fHistRunCounter);

  //fHistTriggers= (TH1D*)fHistRunCounter->Clone("fHistTriggers");
/*  fHistCMUPTriggers= (TH1D*)fHistRunCounter->Clone("fHistCMUPTriggers");
  fHistCMUP6Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP6Triggers");
  fHistCMUP10Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP10Triggers");
  fHistCMUP11Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP11Triggers");
  fHistCMUP13Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP13Triggers");
  fHistCMUP26Triggers= (TH1D*)fHistRunCounter->Clone("fHistCMUP26Triggers");
 // fOutputList->Add(fHistTriggers);

  fOutputList->Add(fHistCMUPTriggers);
  fOutputList->Add(fHistCMUP6Triggers);
  fOutputList->Add(fHistCMUP10Triggers);
  fOutputList->Add(fHistCMUP11Triggers);
  fOutputList->Add(fHistCMUP13Triggers);
  fOutputList->Add(fHistCMUP26Triggers);
*/




  PostAllData();
}
// ----------------------------------------------------------------------------------------------------------------------------------
void AliAnalysisTaskPolarizationGeneral::NotifyRun()
{


  /// Set run number for cuts


  fMuonTrackCuts->SetRun(fInputHandler);
}



// ----------------------------------------------------------------------------------------------------------------------------------
void AliAnalysisTaskPolarizationGeneral::PostAllData()
{
  // Post data
//  PostData(1, fRecTree);
  PostData(1, fOutputList);
//  PostData(3, fGenTree);
//  PostData(4, fTrgTree);


}


// ----------------------------------------------------------------------------------------------------------------------------------

// ----------------------------------------------------------------------------------------------------------------------------------
void AliAnalysisTaskPolarizationGeneral::UserExec(Option_t *)
{

  Int_t iSelectionCounter = 0; // no selection applied yet

  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Data");

//  fMC = MCEvent();

  /*if(!fMC) {

    PostAllData();
    return;

  }*/

//  if(!fIsMC) return;

  Bool_t isTriggered = kFALSE;

  fAOD = dynamic_cast<AliAODEvent*>(InputEvent());

  if(!fAOD) {
    cout<< "no aod files found"<<endl;
  //  PostAllData();
    return;

  }
  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Events");

  /*fMC = MCEvent();
  if(!fMC) {
    PostAllData();
    return;
  }*/
  TString trigger = fAOD->GetFiredTriggerClasses();

  if (!trigger.Contains("CMUP6-B-NOPF-MUFAST")) {
    PostAllData();
    return;
  }

  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"cmup6Trigger");





  Int_t nTracks(fAOD->GetNumberOfTracks());
  if(nTracks<1) {
    PostAllData();
    return;
  }
  fNumberofTracks->Fill(nTracks);
  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"nTracks>1");

/*  fCounterH->Fill(iSelectionCounter); // entering UserExec 1/1 (data/MC)
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Data");*/
//##############################333aodanalysissample StartAnalysi


  /*fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Events");*/

  fRunNumber = fAOD->GetRunNumber();
  //cout<<"run number is "<< fRunNumber<< endl;
  fTracklets = fAOD->GetTracklets()->GetNumberOfTracklets();



  AliAODZDC *dataZDC = dynamic_cast<AliAODZDC*>(fAOD->GetZDCData());
  if(!dataZDC) {
   PostAllData();
   return;
  }




  fCounterH->Fill(iSelectionCounter); // ZDC info is present 7/10
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"ZDC_Info");


  /*fZNAEnergy = dataZDC->GetZNATowerEnergy()[0];
  fZNCEnergy = dataZDC->GetZNCTowerEnergy()[0];
  // fZPAEnergy = dataZDC->GetZPATowerEnergy()[0];
  // fZPCEnergy = dataZDC->GetZPCTowerEnergy()[0];

  //fZDCAtime = fZDCdata->GetZNATime();
  //    fZDCCtime = fZDCdata->GetZNCTime();
  for (Int_t i=0;i<4;i++) fZNATDC[i] = dataZDC->GetZNATDCm(i);
  for (Int_t i=0;i<4;i++) fZNCTDC[i] = dataZDC->GetZNCTDCm(i);*/





// in 2018 q,r : CMUP6-B-NOPF-MUFAST = *0VBA 0MUL ,
// in 2018 q,r and 2015 o:  CMUP11-B-NOPF-MUFAST = *0VBA *0UBA *0UBC 0MUL,
// in 2015 o : CMUP10-B-NOPF-MUFAST = = *0VBA *0UBA *0UBC 0MSL ,


//trigger for MonteCarlo


//  if(fIsMC) {

AliVVZERO *dataVZERO = dynamic_cast<AliVVZERO*>(fAOD->GetVZEROData());
if(!dataVZERO) {
PostAllData();
return;
}


fV0ADecision = dataVZERO->GetV0ADecision();
fV0CDecision = dataVZERO->GetV0CDecision();
fCounterH->Fill(iSelectionCounter); // ZDC info is present 7/10
iSelectionCounter++;
fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Vzerodata");



fCounterH->Fill(20);
fCounterH->GetXaxis()->SetBinLabel(21,"fifteenthbineofsimonecode");



//if( fV0Adecision != 0 || fV0Cdecision != 0) return; //not applied in mc analysis

/*fCounterH->Fill(iSelectionCounter);
iSelectionCounter++;
fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"V0Decision");*/

AliVAD *dataAD = dynamic_cast<AliVAD*>(fAOD->GetADData());
if(!dataAD){
PostAllData();
return;
}

fCounterH->Fill(iSelectionCounter);
iSelectionCounter++;
fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"ADInfo");



  fADADecision = dataAD->GetADADecision();
  fADCDecision = dataAD->GetADCDecision();
/*  if( fADAdecision != 0 || fADCdecision != 0) return;
  fCounterH->Fill(iSelectionCounter);
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"AD decision");*/


  Bool_t fV0Hits[64];
  Int_t fV0TotalNCells = 0;
  for(Int_t iV0Hits = 0; iV0Hits < 64; iV0Hits++) {

    fV0Hits[iV0Hits] = dataVZERO->GetBBFlag(iV0Hits);

    if(fV0Hits[iV0Hits] == kTRUE) {
           // if(iV0Hits < 32) fV0TotalNCells += fV0Hits[iV0Hits];
    if(iV0Hits < 32) fV0TotalNCells += 1;
    }
     // std::cout << "fV0Hits[iV0Hits = " << iV0Hits << ", fRunNum=" << fRunNum << "] = " << fV0Hits[iV0Hits] << endl;
     // std::cout << "fV0TotalNCells (fRunNum = " << fRunNum << ") = " << fV0TotalNCells << endl;
   }


  //if(fIsMC)
  //  {

  /*    if(IsTriggered(fAOD)){
  //cout<< "mc trigger is satisfied"<<endl;
        isTriggered = kTRUE; // Defined the trigger conditions
 // fHistTriggers->Fill(fRunNumber);
}*/
//    }

/*  if (trigger.Contains("CMUP6-B-NOPF-MUFAST")) {

  isTriggered = kTRUE;

}*/


  //if(!isTriggered) return;

  /*fCounterH->Fill(iSelectionCounter);
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Triggered");*/





//  }

/*if (trigger.Contains("CMUP")) {
      isTriggered = kTRUE;
      fCMUPDecision = 1;
      fHistCMUPTriggers->Fill(fRunNumber);
      fCMUP = 1;
      fTrgRunNum = fRunNumber;
    } else {
      fCMUPDecision = 0;
      fCMUP = 0;
    }



    if (trigger.Contains("CMUP11-B-NOPF-MUFAST")) {
      isTriggered = kTRUE;
      fCMUP11Decision = 1;
      fHistCMUP11Triggers->Fill(fRunNumber);
      fCMUP11 = 1;
    } else {
      fCMUP11Decision = 0;
      fCMUP11 = 0;
    }



    if (trigger.Contains("CMUP10-B-NOPF-MUFAST")) {
      isTriggered = kTRUE;
      fCMUP10Decision = 1;
      fHistCMUP10Triggers->Fill(fRunNumber);
      fCMUP10 = 1;
    } else {
      fCMUP10Decision = 0;
      fCMUP10 = 0;
    }

  // ###### CMUP6 trigger

    if (trigger.Contains("CMUP6-B-NOPF-MUFAST")) {
      isTriggered = kTRUE;
      fCMUP6Decision = 1;
      fHistCMUP6Triggers->Fill(fRunNumber);
      fCMUP6 = 1;
    } else {
      fCMUP6Decision = 0;
      fCMUP6 = 0;
    }


    if (trigger.Contains("CMUP13-B-NOPF-MUFAST")) {
      isTriggered = kTRUE;
      fCMUP13Decision = 1;
      fHistCMUP13Triggers->Fill(fRunNumber);
      fCMUP13 = 1;
    } else {
      fCMUP13Decision = 0;
      fCMUP13 = 0;
    }



    if (trigger.Contains("CMUP26-B-NOPF-MUFAST")) {
      isTriggered = kTRUE;
      fCMUP26Decision = 1;
      fHistCMUP26Triggers->Fill(fRunNumber);
      fCMUP26 = 1;
    } else {
      fCMUP26Decision = 0;
      fCMUP26 = 0;
    }



if(!isTriggered) {
  PostAllData();
  return;
}*/


if(fV0ADecision != 0) {
     PostAllData();
     return;
}
if(fADADecision != 0) {
     PostAllData();
     return;
}
if(fADCDecision != 0) {
    PostAllData();
     return;
}
if( !(fV0CDecision == 0 || fV0CDecision == 1) ) {
       PostAllData();
       return;
  }

/* - 0 tracklets in SPD
 */
/*if(fTracklets != 0) {
     PostAllData();
     return;
}*/
if( fV0TotalNCells > 2 ) {
     PostAllData();
     return;
}

fCounterH->Fill(iSelectionCounter);
iSelectionCounter++;
fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"fV0andADdecision");




















// cout<<"ntracks"<<nTracks<<endl;


//cout<<"this work fine"<< endl;


AliAODTrack *track[2];
AliAODTrack *singletrack;
track[0] = 0x0;
track[1] = 0x0;
//Int_t goodtrack1 =0;
//Int_t goodtrack2 =0;


Int_t trackcounter = 0;


for(Int_t iTrack = 0; iTrack < nTracks; iTrack++) {

  if(trackcounter>2) {
  PostAllData();
  return;
  }


//cout<<"entering the track loop"<< iTrack<<endl;
  // get track
track[trackcounter] = static_cast<AliAODTrack*>(fAOD->GetTrack(iTrack));
singletrack = static_cast<AliAODTrack*>(fAOD->GetTrack(iTrack));
if(!track[trackcounter]) return;

if(!track[trackcounter]->IsMuonTrack()) {
  //PostAllData();
  continue;
}


if(!fMuonTrackCuts->IsSelected(track[trackcounter])) {
  continue;
}
fRecRabs->Fill(singletrack->GetRAtAbsorberEnd());
fRecEta->Fill(singletrack->Eta());


//  TrackClone = track
//  cout <<"momentum of track"<<track->Pt()<<endl;
 // if(!track) cout<<"thre is no track"<< endl; return;

  // is it a good muon track?




//  cout<<"there are some good muon tracks"<<track->Charge()<<endl;

/*  if (track->Charge() > 0) {
    PosTrack = track;
    goodtrack1++;
  } else  if (track->Charge() < 0) {
    NegTrack = track;
    goodtrack2++;

  }*/
    trackcounter++;

//  cout<< "end of track loop"<<endl;
 }




 /*if(!track->IsMuonTrack())  return;
 fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
 iSelectionCounter++;
 fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"MuonTracksSelection");*/



 /*if(!fMuonTrackCuts->IsSelected(track)) return;
 fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
 iSelectionCounter++;
 fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"GoodMuonTrackSelection");*/
 //if (paircounter>2) return;
 if(trackcounter!=2) {
   PostAllData();
   return;


 }
 fPairNumber->Fill(trackcounter);



 /*fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
 iSelectionCounter++;
 fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"onlytwo muontracks");*/




  /*if(track->Eta()<-4.0 || track->Eta()>-2.5) return;

  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"-4_Eta_2.5");*/
    // cout<< track->Pt() <<endl;
    // cout<< track->Eta() <<endl;
  //   if(track->Pt()>0.25) return;





if((track[0]->Charge()) == (track[1]->Charge())){
  PostAllData();
  return;
}

//fRecCharge->Fill(PosTrack->Charge() *NegTrack->Charge());
  fRecCharge->Fill(singletrack->Charge());
/* if( (track->GetRAtAbsorberEnd() < 17.5) || (track->GetRAtAbsorberEnd() > 89.5) ) return;
 fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
 iSelectionCounter++;
 fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"17.5_Rabs_89.5");*/



// Int_t paircounter = 0;

  /*if (!(nGoodPosMuons == 1 && nGoodNegMuons == 1)) {
//cout<<"there is no good muon pair"<<nGoodPosMuons <<"  ,   "<< nGoodNegMuons <<endl;
    PostAllData();
 //paircounter++;
    return;
  }*/


/*  fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Opposite_Charge");*/

//  if (paircounter>0) fCounterH->Fill(iSelectionCounter); // At least one good muon

  fCounterH->Fill(iSelectionCounter);
  iSelectionCounter++;
  fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Opposite_Charge");



// if(paircounter>1) return;

//  cout<<" good muon pair"<<nGoodPosMuons <<"  ,   "<< nGoodNegMuons <<endl;
//#####################################3twomuon ana_type






  TDatabasePDG *pdgdat = TDatabasePDG::Instance();
  TParticlePDG *partMuon = pdgdat->GetParticle(13);
  Double_t MuonMass = partMuon->Mass();
  fRecDaughter1.SetPtEtaPhiM(track[0]->Pt(), track[0]->Eta(), track[0]->Phi(), MuonMass);
  fRecDaughter2.SetPtEtaPhiM(track[1]->Pt(), track[1]->Eta(), track[1]->Phi(), MuonMass);
  fRecPair_Parent = fRecDaughter1 +fRecDaughter2;

   if(fRecPair_Parent.Pt()>0.25) {
     PostAllData();
     return;
   }
   fCounterH->Fill(iSelectionCounter);
   iSelectionCounter++;
   fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Pt<0.25");
   fRecParentPtH->Fill(fRecPair_Parent.Pt());

   if(fRecPair_Parent.Rapidity()<-4.0|| fRecPair_Parent.Rapidity()>-2.5) {
     PostAllData();
     return;
   }

   fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
   iSelectionCounter++;
   fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"-4_Y_2.5");
   fRecParentRapH->Fill(fRecPair_Parent.Rapidity());

   fRecParentMassH->Fill(fRecPair_Parent.M());



/*
//AliAODTrack *PosTrack = static_cast<AliAODTrack*>(fAOD->GetTrack(idxPosMuons[0]));
fRecPosDaughter.SetPtEtaPhiM(PosTrack->Pt(), PosTrack->Eta(), PosTrack->Phi(), MuonMass);


//AliAODTrack *NegTrack = static_cast<AliAODTrack*>(fAOD->GetTrack(idxNegMuons[0]));
fRecNegDaughter.SetPtEtaPhiM(NegTrack->Pt(), NegTrack->Eta(), NegTrack->Phi(), MuonMass);


fRecPair_Parent= fRecPosDaughter + fRecNegDaughter;


fRecHelicityTheta =  CosThetaHelicityFrame(fRecPosDaughter,fRecNegDaughter,fRecPair_Parent);
fRecCollinTheta   =  CosThetaCollinsSoper(fRecPosDaughter,fRecNegDaughter,fRecPair_Parent);

fRecHelicityPhi   =  CosPhiHelicityFrame(fRecPosDaughter,fRecNegDaughter,fRecPair_Parent);
fRecCollinPhi     =  CosPhiCollinsSoper(fRecPosDaughter,fRecNegDaughter,fRecPair_Parent);


fRecCollinTildePhi = TildePhiCalulator(fRecCollinPhi , fRecCollinTheta);
fRecHelicityTildePhi = TildePhiCalulator(fRecHelicityPhi , fRecHelicityTheta);
fRecPair_ParentMass = fRecPair_Parent.M();





  if(fIsMC) {

  TClonesArray *mcarray = (TClonesArray*) fAOD->GetList()->FindObject(AliAODMCParticle::StdBranchName());
  if(!mcarray) return;

  AliAODMCParticle *mcPostrack1 = (AliAODMCParticle*) mcarray->At(PosTrack->GetLabel());
  fRec_ConnectedMCPosDaughter.SetPtEtaPhiM(mcPostrack1->Pt(), mcPostrack1->Eta(), mcPostrack1->Phi(), MuonMass);

  AliAODMCParticle *mcPostrack2 = (AliAODMCParticle*) mcarray->At(NegTrack->GetLabel());
  fRec_ConnectedMCNegDaughter.SetPtEtaPhiM(mcPostrack2->Pt(), mcPostrack2->Eta(), mcPostrack2->Phi(), MuonMass);


  fRec_ConnectedMCPair_Parent= fRec_ConnectedMCPosDaughter + fRec_ConnectedMCNegDaughter;



  fSimulated_Reconstructed_HelicityTheta= CosThetaHelicityFrame(fRec_ConnectedMCPosDaughter,fRec_ConnectedMCNegDaughter,fRec_ConnectedMCPair_Parent);
  //cout<<"no problamo"<<endl;


  fSimulated_Reconstructed_CollinTheta= CosThetaCollinsSoper(fRec_ConnectedMCPosDaughter,fRec_ConnectedMCNegDaughter,fRec_ConnectedMCPair_Parent);
  //cout<<"yes problamo"<<endl;


  fSimulated_Reconstructed_HelicityPhi= CosPhiHelicityFrame(fRec_ConnectedMCPosDaughter,fRec_ConnectedMCNegDaughter,fRec_ConnectedMCPair_Parent);


  fSimulated_Reconstructed_CollinPhi=  CosPhiCollinsSoper(fRec_ConnectedMCPosDaughter,fRec_ConnectedMCNegDaughter,fRec_ConnectedMCPair_Parent);

  fSimulated_Reconstructed_CollinTildePhi = TildePhiCalulator(fSimulated_Reconstructed_CollinPhi , fSimulated_Reconstructed_CollinTheta);
  fSimulated_Reconstructed_HelicityTildePhi = TildePhiCalulator(fSimulated_Reconstructed_HelicityPhi , fSimulated_Reconstructed_HelicityTheta);


  fRec_ConnectedMCPair_ParenttMass = fRec_ConnectedMCPair_Parent.M();


  }
 */






  /*  if(fRecPair_Parent.Pt()>0.25) return;
    fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
    iSelectionCounter++;
    fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"Pt_{#mu #mu}<0.25");


    if(fRecPair_Parent.Rapidity()<-4.0|| fRecPair_Parent.Rapidity()>-2.5) return;
    fCounterH->Fill(iSelectionCounter); // AOD event found 2/2
    iSelectionCounter++;
    fCounterH->GetXaxis()->SetBinLabel(iSelectionCounter,"-4_Y_2.5");

  fRecTree->Fill();
 */

  PostAllData();

  }



// ----------------------------------------------------------------------------------------------------------------------------------














Bool_t AliAnalysisTaskPolarizationGeneral::IsTriggered(AliVEvent *fAOD){
/*
This is the trigger definition from evgeny's code

*/


  UShort_t fTriggerAD = fAOD->GetADData()->GetTriggerBits();
  UShort_t fTriggerVZERO = fAOD->GetVZEROData()->GetTriggerBits();
  UInt_t fL0inputs = fAOD->GetHeader()->GetL0TriggerInputs();

  //fTriggerInputsMC[0] = fL0inputs & (1 << 9);   //0VBA VZERO A
  //fTriggerInputsMC[1] = fL0inputs & (1 << 10);   //0VBC VZERO C



  Bool_t is0VBAfired = fTriggerVZERO & (1 << 12); //0VBA VZERO A
  Bool_t is0VBCfired = fTriggerVZERO & (1 << 13); //0VBC VZERO C
  Bool_t is0UBAfired = fTriggerAD & (1 << 12);   //0UBA ADA
  Bool_t is0UBCfired = fTriggerAD & (1 << 13);   //0UBC ADC



  if (!is0VBAfired && !is0UBAfired && !is0UBCfired ) return kTRUE;
  else return kFALSE;

}








Double_t AliAnalysisTaskPolarizationGeneral::CosPhiHelicityFrame(TLorentzVector muonPositive,TLorentzVector muonNegative,TLorentzVector possibleJPsi)
{
  /* - This function computes the helicity phi for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
  */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  //
  // --- Determine the z axis for the calculation of the AliAnalysisTaskPolarizationGeneral angle
  // (i.e. the direction of the dimuon in the CM system)
  //
  TVector3 zaxis = (possibleJPsi.Vect()).Unit();
  TVector3 yaxis = ((pProjDimu.Vect()).Cross(pTargDimu.Vect())).Unit();
  TVector3 xaxis = (yaxis.Cross(zaxis)).Unit();
  //
  // --- Calculation of the azimuthal angle (Helicity)
  //
  Double_t phi = TMath::ATan2((pMu1Dimu.Vect()).Dot(yaxis),(pMu1Dimu.Vect()).Dot(xaxis));
  return   phi;
}



Double_t AliAnalysisTaskPolarizationGeneral::CosPhiCollinsSoper( TLorentzVector muonPositive,
                                                        TLorentzVector muonNegative,
                                                        TLorentzVector possibleJPsi )
{
  /* - This function computes the Collins-Soper PHI for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  /* - Determine the z axis for the CS angle.
     -
   */
  TVector3 zaxisCS=(((pProjDimu.Vect()).Unit())-((pTargDimu.Vect()).Unit())).Unit();
  //
  // --- Determine the CS angle (angle between mu+ and the z axis defined above)
  //
  TVector3 yaxisCS=(((pProjDimu.Vect()).Unit()).Cross((pTargDimu.Vect()).Unit())).Unit();
  TVector3 xaxisCS=(yaxisCS.Cross(zaxisCS)).Unit();

  Double_t phi = TMath::ATan2((pMu1Dimu.Vect()).Dot(yaxisCS),((pMu1Dimu.Vect()).Dot(xaxisCS)));
  return   phi;
}



Double_t AliAnalysisTaskPolarizationGeneral::CosThetaCollinsSoper( TLorentzVector muonPositive,
                                                          TLorentzVector muonNegative,
                                                          TLorentzVector possibleJPsi )
{
  /* - This function computes the Collins-Soper cos(theta) for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  /* - Determine the z axis for the CS angle.
     -
   */
  TVector3 zaxisCS=(((pProjDimu.Vect()).Unit())-((pTargDimu.Vect()).Unit())).Unit();
  /* - Determine the CS angle (angle between mu+ and the z axis defined above)
     -
   */
  Double_t CosThetaCS = zaxisCS.Dot((pMu1Dimu.Vect()).Unit());
  return   CosThetaCS;
}


Double_t AliAnalysisTaskPolarizationGeneral::CosThetaHelicityFrame( TLorentzVector muonPositive,
                                                           TLorentzVector muonNegative,
                                                           TLorentzVector possibleJPsi )
{
  /* - This function computes the Helicity cos(theta) for the
     - helicity of the J/Psi.
     - The idea should be to get back to a reference frame where it
     - is easier to compute and to define the proper z-axis.
     -
   */

  /* - Half of the energy per pair of the colliding nucleons.
     -
   */
  Double_t HalfSqrtSnn   = 2510.;
  Double_t MassOfLead208 = 193.6823;
  Double_t MomentumBeam  = TMath::Sqrt( HalfSqrtSnn*HalfSqrtSnn*208*208 - MassOfLead208*MassOfLead208 );
  /* - Fill the Lorentz vector for projectile and target.
     - For the moment we do not consider the crossing angle.
     - Projectile runs towards the MUON arm.
     -
   */
  TLorentzVector pProjCM(0.,0., -MomentumBeam, HalfSqrtSnn*208); // projectile
  TLorentzVector pTargCM(0.,0.,  MomentumBeam, HalfSqrtSnn*208); // target
  /* - Translate the dimuon parameters in the dimuon rest frame
     -
   */
  TVector3       beta      = ( -1./possibleJPsi.E() ) * possibleJPsi.Vect();
  TLorentzVector pMu1Dimu  = muonPositive;
  TLorentzVector pMu2Dimu  = muonNegative;
  TLorentzVector pProjDimu = pProjCM;
  TLorentzVector pTargDimu = pTargCM;
  pMu1Dimu.Boost(beta);
  pMu2Dimu.Boost(beta);
  pProjDimu.Boost(beta);
  pTargDimu.Boost(beta);
  //
  // --- Determine the z axis for the calculation of the AliAnalysisTaskPolarizationGeneral angle
  // (i.e. the direction of the dimuon in the CM system)
  //
  TVector3 zaxis = (possibleJPsi.Vect()).Unit();
  /* - Determine the He angle (angle between mu+ and the z axis defined above)
     -
   */
  Double_t CosThetaHE = zaxis.Dot((pMu1Dimu.Vect()).Unit());
  return   CosThetaHE;

}





// this is tilde phi calculator


Double_t AliAnalysisTaskPolarizationGeneral::TildePhiCalulator(Double_t phi, Double_t costheta){

  Double_t TildePhi;
  if(costheta < 0){

  TildePhi = phi - (3/4) * TMath::Pi();
  }
  else{
  TildePhi = phi- (1/4) * TMath::Pi();

  }
  if(TildePhi <0){
  TildePhi = TildePhi+2*TMath::Pi();

  }
 return TildePhi;
}









void AliAnalysisTaskPolarizationGeneral::Terminate(Option_t *)
{

    // terminate
    // called at the END of the analysis (when all events are processed)
}
// ----------------------------------------------------------------------------------------------------------------------------------
