#!/bin/bash

#Install dependencies
pip install -r requirement.txt

#Run the test
pytest test_sentiment.py