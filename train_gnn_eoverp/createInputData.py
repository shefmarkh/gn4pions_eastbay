import uproot
import numpy as np

if __name__ == '__main__':

    testFile="/Users/markhodgkinson/user.mhodgkin.33549591._000002.mltree.root"

    clusterVariables = ['cluster_cell_E', 'cluster_cell_ID',             
                         'nCluster','truthPartE', 'truthPartPt',
                        'cluster_ENG_CALIB_TOT','cluster_E','cluster_Eta','cluster_Phi',
                         'cluster_EM_PROBABILITY','cluster_E_LCCalib','cluster_HAD_WEIGHT', 'cluster_OOC_WEIGHT',
                         'cluster_DM_WEIGHT', 'cluster_CENTER_MAG', 'cluster_FIRST_ENG_DENS', 
                         'cluster_CENTER_LAMBDA', 'cluster_ISOLATION'          
                        ]

    trackVariables = ['trackPt','trackD0','trackZ0',
                 'trackEta_EMB2','trackPhi_EMB2',
                 'trackEta_EME2','trackPhi_EME2',
                 'trackEta','trackPhi',
                 'nTrack','trackNumberOfPixelHits',
                 'trackNumberOfSCTHits',
                 'trackNumberOfPixelDeadSensors',
                 'trackNumberOfSCTDeadSensors',
                 'trackNumberOfInnermostPixelLayerHits',
                 'trackNumberOfNextToInnermostPixelLayerHits',
                 'trackExpectInnermostPixelLayerHit',
                 'trackExpectNextToInnermostPixelLayerHit',
                 'trackNumberOfTRTHits',
                 'trackNumberOfTRTOutliers',
                 'trackChiSquared',
                 'trackNumberDOF',
                 'trackD0',
                 'trackZ0'
                ]

    truthVariables = ['truthPartE', 'truthPartPt']
             
    variables = clusterVariables + trackVariables + truthVariables


    theTree = uproot.open(testFile)["EventTree"]
    df = theTree.arrays(variables, library="np")
    np.save("test.npy",df)
