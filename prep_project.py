# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:45:15 2015
Last Edit: Thurs Mar 9 22:54 2017
@author: Christina Van Heer (christinavanheer@gmail.com

# Description: this sets up a file structure like
# Nikolas outline - c.f. http://nikola.me/folder_structure.html

# Directions:
# Terminal setup (Mac) :
#   1. Make sure smart quotes are disabled on your mac - http://www.iclarified.com/38772/how-to-disable-curly-quotes-in-mac-os-x-mavericks
#   2. Open your bash profile: open a terminal e.g. 'sudo open ~/.bash_profile'
#   3. Add an alias for the script e.g. 'alias prep_project="python ~/path_to_file/prep_project.py"
#      This means everytime you type prep_project in the terminal you will start the script
#   4. Close the terminal and open it again - change directory to the place you want to make the project folder (e.g.) cd '/Users/Chris/PhD/'
#   5. Type 'prep_project' and the terminal should ask you for the folder name

# Script setup:
# 1. Change these two lines in the script below under 'if not ask_for_input' :
    - main_dir = '/Users/Chris/Dropbox/PhD/' # where you want to put the new folder
    - project_name = '1.CONFLEARN'
    To whatever you want
# 2. Change ask_for_input to a value of 0 i.e. ask_for_input = 0
# 3. Run the script in python
     E.g. In the terminal (mac): python ~/path_to_file/prep_project.py


##################### The project setup #####################
#Project Management - managing and planning projects - For example: Project Background, Project Proposals and Plans, Funding Applications, Budget, Project Reports.
# Ethics Governance - Applications for Ethical Approval, Insurance, Participant Information Sheets, and Consent Forms.
# ExperimentFolder - contains subfolders called:
        # 'Inputs' = anything related to the task itself - stimuli, code to run experiment etc
        # 'Data' = the raw data
        # 'DataAnalysis' = all intermediate files (data), pre-processed, transformed and analysed data
        # 'Outputs' = stores all of the analysis output - tables, SPSS output, figures, diagrams
# Dissemination - posters, talks, manuscript drafts

"""
#!/usr/bin/python
import os, glob, sys

#######################  USER TO CHANGE #######################################
ask_for_input = 1 # 1 = will ask for project name in terminal
                  # 0 = will use name below under 'not ask_for_input' for statement

custom_sub_folders = 1 # (see subfolders at end you can customise)

if not ask_for_input: # NEED TO CHANGE IF YOU ARE NOT USING TERMINAL
    main_dir = '/Users/Chris/Dropbox/PhD/' # where you want to put the new folder
    project_name = '1.CONFLEARN'
else:
    main_dir = os.getcwd() # get directory you are in

    py3 = sys.version_info[0] > 2 #creates boolean value for test that Python major version > 2
    if py3:
      response = input("Please enter project_name: ")
      project_name = response
    else:
      response = raw_input("Please enter project_name: ")
      project_name = response

############################################################################

dir_struct = dict() # creates
dir_struct.update({
'1.EthicsGovernance': ["1.EthicsApproval","2.ConsentForms"],
'2.Project_Management': ["1.Proposals","2.Finance","3.Reports"],
'3.ExperimentFolder': ["1.Inputs","2.Data","3.DataAnalysis","4.Outputs"],
'4.Dissemination': ["1.Presentations","2.Publications"]
# add anything you want here
}) # where the exp files are stored

############################################################################
project_dir = os.path.join(main_dir,project_name)

if not os.path.exists(project_dir):
    os.mkdir(project_dir)
else:
    raise OSError('This project file is already on your computer at the location you specified, script will not overwrite')

########################## Setup Vukovic Structure #############################
for level1 in dir_struct:

    # If empty, make level1 directory
    if not any(dir_struct[level1]):
        os.mkdir(os.path.join(project_dir,level1)) # if empty make directory

    # If NOT empty, make level1 AND level2 directory after
    else:
        os.mkdir(os.path.join(project_dir,level1))

        for level2 in dir_struct[level1]: # make level 2 directory
            os.mkdir(os.path.join(project_dir,level1,level2))


########################## Custom folders #############################

if custom_sub_folders:

########### Data folder #############
    os.mkdir(os.path.join(project_dir,'3.ExperimentFolder',
    dir_struct['3.ExperimentFolder'][1],'rawData_DONOTTOUCH'))

########### DataAnalysis folder #####
    os.mkdir(os.path.join(project_dir,'3.ExperimentFolder',
    dir_struct['3.ExperimentFolder'][2],'processed_data'))

    os.mkdir(os.path.join(project_dir,'3.ExperimentFolder',
    dir_struct['3.ExperimentFolder'][2],'run_analysis'))

    os.mkdir(os.path.join(project_dir,'3.ExperimentFolder',
    dir_struct['3.ExperimentFolder'][2],'old_code'))
