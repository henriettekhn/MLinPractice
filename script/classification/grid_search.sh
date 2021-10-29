#!/bin/bash

mkdir -p data/classification

# specify hyperparameter values
values_of_k=("1 2 3 4 5 6 7 8 9 10")
number_of_trees=("50 100 150")
penalties_for_svm=("l1 l2")


# different execution modes
if [ $1 = local ]
then
    echo "[local execution]"
    cmd="script/classification/classifier.sge"
elif [ $1 = grid ]
then
    echo "[grid execution]"
    cmd="qsub script/classification/classifier.sge"
else
    echo "[ERROR! Argument not supported!]"
    exit 1
fi

# do the grid search for hyperparameters of KNeighbors classifier
for k in $values_of_k
do
    echo $k
    $cmd 'data/classification/clf_'"$k"'.pickle' --knn $k -s 42 --accuracy --kappa --f1_score
done


# do grid search for hyperparameters of RandomForest classifier
for t in $number_of_trees
do
    echo $t
    $cmd 'data/classification/rf_clf_'"$t"'.pickle' --rf $t -s 42 --accuracy --kappa --f1_score
done 


# do grid search for hyperparameters of support vector machine
for p in $penalties_for_svm
do 
    echo $p
    $cmd 'data/classification/svm_clf_'"$p"'.pickle' --svm $p -s 42 --accuracy --kappa --f1_score
done