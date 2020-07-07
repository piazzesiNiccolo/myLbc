this repo is a custom version of [LearningByCheating](https://github.com/dianchen96/LearningByCheating) that i used for my Bachelor thesis. 

# Summary 
For my thesis i injected some adversarial attacks inside LbC to see the effects of these attacks on autonomous driving. The attacks injected were provided by the Adversarial Robustness Toolbox ([ART](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/)) library (version 1.2.0). This repo contains the modified LbC agent that i used to test the attacks. You can see the tests results and the videos recorded [here](https://drive.google.com/drive/folders/1tTEAQSK2XAK_sdmuWo80Bd-58_pkiK3h?usp=sharing).

# Installation
The installation guide can be found in [HERE](https://github.com/dianchen96/LearningByCheating/blob/release-0.9.6/INSTALL.md). The process is pretty much the same, just remember to clone this modified repo instead of the original. If you want to skip compiling, use [this](quick_start.sh) script. I changed it to actually install this version.


# Changes
 
The code changes can be found in the subfolder bird_view/models. I added the module [attack](bird_view/models/attack.py) and modified some part of the [image](bird_view/models/image.py) module.


