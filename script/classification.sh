#!/bin/bash

# create directory if not yet existing
mkdir -p data/classification/

# run feature extraction on training set (may need to fit extractors)
echo "  training set"
python -m script.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 3 -s 42 --f1_score --kappa

# run feature extraction on validation set (with pre-fit extractors)
echo "  validation set"
python -m script.classification.run_classifier data/dimensionality_reduction/validation.pickle -i data/classification/classifier.pickle --f1_score --kappa

# don't touch the test set, yet, because that would ruin the final generalization experiment!
echo "  test set"
python -m script.classification.run_classifier data/dimensionality_reduction/test.pickle -e data/classification/classifier.pickle --knn 3 -s 42 --f1_score --kappa

