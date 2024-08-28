
HackerNews API Acceptance Tests

    This directory contains acceptance tests for the HackerNews API. These tests
    are designed to ensure that the API is functioning correctly and returns the 
    expected data.

Getting Started:
    
    Prerequisites:
        
        python == 3.12.4
        requests==2.32.3    
        pytest==7.4.4

    1. Manual Installation and test run

        a. Ensure python version 3.x: check your python version using 
            python --version
        b. pip install requests==2.32.3 pytest==7.4.4
        c. pytest -v -s test_hn_app.py

    2. Conda for package environment management and test run
    
        a. Download and install Anaconda distribution from 
                    https://docs.anaconda.com/anaconda/install/
        b. conda env create -f environment.yml
        c. conda activate bindu_take_home
        d. pytest -v -s test_hn_app.py
        e. conda deactivate

    3. Run Script (Automatic Conda environment setup and test run) (Recommended)

        a. Download and install Anaconda distribution from 
                    https://docs.anaconda.com/anaconda/install/
        b. ./run.sh 

Test Run Options:

    pytest -s               console output
           -v               verbose
           -m  "burst"      run test tagged with "burst"
           -m  "not burst"  do not run test tagged with "burst"
