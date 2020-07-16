# Learning by Cheating and Adversarial Robustness Toolbox
This repo is a custom version of the [LearningByCheating](https://github.com/dianchen96/LearningByCheating) autonomous driving agent and related suite, which has been integrated with the IBM Adversarial Robustness Toolbox ([ART](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/)) for the injection of 4 attacks on the RGB camera:

• Spatial Transformation ([STA](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks/evasion.html#spatial-transformations-attack)),

• HopSkipJump ([HSJ](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks/evasion.html#hopskipjump-attack)),

• Basic Iterative Method ([BIM](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks/evasion.html#basic-iterative-method-bim)),

• NewtonFool ([NF](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/modules/attacks/evasion.html#newtonfool)).


# Summary 
For my Bachelor Thesis in Computer Science at the University of Florence, I injected some adversarial attacks inside the images extracted by the RGB camera, before these are fed to the Learning By Cheating trained agent. The objective is to visualize theeffects of these attacks on the trained agents. 

The attacks injected were provided by the Adversarial Robustness Toolbox ([ART](https://adversarial-robustness-toolbox.readthedocs.io/en/latest/)) library (version 1.2.0). This repo contains the modified LbC agent that I used to test the attacks. You can see the tests results and the videos recorded for the various runs [here](https://drive.google.com/drive/folders/1tTEAQSK2XAK_sdmuWo80Bd-58_pkiK3h?usp=sharing).

The following table summarizes results.


|Attack |Completed Runs| Ignored Semaphores| Collisions| Timeouts|
|---|---|---|---|---|
|Golden runs (no Attack) | 12/12 |0 |0 |0|
|HSJ |6/12 |9| 6| 0|
|STA |7/12| 0 |4| 1|
|BIM |0/12 | N/A| 12| 0|
|NF |3/12| 13| 9| 0|

# Installation
The installation guide can be found in [HERE](https://github.com/dianchen96/LearningByCheating/blob/release-0.9.6/INSTALL.md). The process to install and use the software is pretty much the same, just remember to clone this modified repo instead of the original. If you want to skip compiling, use [this](quick_start.sh) script. I changed it to actually install this version.

To select which attack to be injected during a run, it is required:
- TO BE COMPLETED!!!


# Changes
 
The code changes can be found in the subfolder bird_view/models. I added the module [attack](bird_view/models/attack.py) and modified some part of the [image](bird_view/models/image.py) module.

# Reference

Niccolò Piazzesi, "Attacchi verso sistemi di apprendimento in ambito autonomous driving: studio e implementazione in ambienti simulati (in Italian)", Bachelor Thesis at the University of Florence. Supervisor: Andrea Ceccarelli.

Link to the Thesis: http://rcl.dsi.unifi.it/administrator/components/com_jresearch/files/publications/PiazzesiNiccol%C3%B2.pdf


