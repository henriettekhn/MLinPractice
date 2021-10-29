# Documentation

This is a program that predicts if a tweet will go viral or not. For this, the
user needs to enter a tweet and will then receive the prediction and how 
certain this prediction is. 
A tweet counts as being "viral" when the number of likes and retweets added up 
is higher than 30.
The data set used to train the program can be found here: 
https://kaggle.com/ruchi798/data-science-tweets .

This is a documentation of the changes we made to the code that was provided
(https://github.com/lbechberger/MLinPractice) . This means there will not be 
documentation of every file or step, but only of the ones we added or changed.



## Evaluation

### Design Decisions

As evaluation metrics we implemented precision, recall, f1-score, accuracy and
Cohen's kappa.

For the final application we decided to use only f1-score and Cohen's kappa (see
`script/classification.sh`). We came to this decision because the hyperparameter 
search suggested very high accuracy for all parameter configurations, so this 
did not seem very meaningful. We related this back to the data being unbalanced.
We also decided to finally not use precision and recall since they are somehow 
embedded in the f1-score.
For all hyperparameter settings that we tried in our grid search, we received 
very low results for Cohen's kappa and f1-score. This is probably due to the
fact that we only implemented two extra meaningful features (apart from character 
length).

As baselines we implemented the majority, label frequency, always true and 
always false classifier. We chose those because they are the most basic classifiers 
we could think of and do not rely on any elaborated classification. That means
that they are a good baselines to compare to our supposedly better/real classifiers.
 
The implementation of our evaluation metrics and baselines can be 
found under `script/classification/run_classifier.py`

### Results

The majority vote classifier, as well as the always false classifier, performed 
extremly poor. For f1-score and Cohen's kappa they both resulted in 0.

The always true classifier performed slightly better. It also scored a Cohen's 
kappa of 0, but an f1-score of 0.1177 (on the training  and validation set).

The label frequency classifier performed also better: It led to an f1-score of
0.06 ans a Cohen's kappa of 0.001/0.006 (training/validation set).

### Interpretation

None of these basic classifiers seems to be a good choice. We should definitly 
consider using a more elaborated classifier.

## Preprocessing

### Design Decisions

Under `script/preprocessing/create_labels.py` labels are created for the data in 
the test and validation set according to the definition of viral. We tried out 
different definitions for this (higher/lower threshold, different weights) and 
finally decided to lower the threshold to 30 but leave the weights (default = 1).
We chose to lower the threshold to have more positively classified examples 
hoping to be able to receive a positive classification during application.


### Results

Maybe show a short example what your preprocessing does.

### Interpretation

Probably, no real interpretation possible, so feel free to leave this section out.

## Feature Extraction

### Design Decisions

Which features did you implement? What's their motivation and how are they computed?
We implemented two new features, a hashtag count and an exclamation mark count.

In `script/feature_extraction/number_hashtags.py` , the hashtag count is implemented.
It determines the importance of the number of hashtags used in a tweet for it
to go viral. In our opinion, this is an important feature because hashtags are
a huge part of the tweeting culture.
 
In `script/feature_extraction/exclamation_count.py` , the exclamation count is implemented.
It determines the importance of the number of exclamation marks used in a tweet for it
to go viral. In our opinion, this is an important feature because the number of
exclamation marks in a tweet migth indicate the mood of the tweet which could 
influence the popularity of the tweet.


## Dimensionality Reduction

### Design Decisions

We decided not to reduce our dimensionality, but in order to still get some
information about the usefulness of the features we decided to use SelectKBest
with Mutual Information and k = all (= 3). As we only had three features in total,
we did not want to reduce them further because that would have led to even 
less information for classification. 

### Results

We selected all our features (character length, exclamation count, hashtag count).
The scores that were given to us in script/dimensionality_reduction/reduce_dimensionality.py
indicated that the character length of a tweet is the most important feature (0.0098),
followed by the number of hashtags (0.0057) and the exclamation count (0.001).

### Interpretation

The generally low scores indicate that we did not use very informative features,
which is also reflected in our classification-evaluation results.

## Classification

### Design Decisions

As more elaborated classifiers, we have chosen the k nearest neighbors, random 
forest and support vector machine classifier.
We performed hyperparameter optimization using grid search in order to find 
the best parameter configuration for the best suited classifier. 
For the k nearest neighbors classifier, we tried out different values for k in 
a range from 1 to 10. 
For the random forest classifier, we tried out a differend amout of trees 
(50, 100, 150).
For the support vector machine classifiers we tried out the two penalties l1 
and l2.
We stored all the outcomes using mlflow.

In the end, we decided to use the k nearest neighbors classifier with k = 3 
because it led to the best results concerning f1-score and Cohen's kappa.

### Results

For all the different settings we tried out, we received a relatively high 
accuracy and low f1-score and Cohen's kappa.

For the support vector machine classifier, we continuously received 0 for 
f1-score and Cohen's kappa. The accuracy was always at 0.937.

For the random forest classifier, our results varied between 0.004 (150 trees, 
validation set) and 0.037 (50 trees, training set) for Cohen's kappa. The f1-
score varies between 0.07 (150 trees, validatin set) and 0.04 (50/100 trees, 
training set).

For the k nearest neighbors classifier, our results varied for Cohen's kappa
between 0.072 (k = 1, training set) and 0.003 (k = 10, validation set). The 
f1-score varied between 0.093 (k = 3, training set) and 0.004 (k = 10, validation
set).

When looking at these results, we conclude that the classifiers perform worse on
the validation set. This means that our classifier is slightly overfitting.

When performing classification on the test set using our best settings (k = 3),
we get a score of 0.0945 for Cohen's kappa and 0.1192 for f1-score (see 
`script/classification.sh`).


### Interpretation

It looks like the hyperparameter "penalty" for the support vector machine does 
not make a difference for our application. 

The number of trees in the random forest classifier seems to not have the biggest 
effect in the evaluation metrics as there is no remarkable difference in the
between the respective results. However, there is always a strong difference 
between the training and validation set. This means that they are overfitting.

For k nearest neighbors, the setting for k seems to be rather important. For the 
different values of k we received a wide range of results for the evaluation metrics.


### Conclusion

All in all, our program does not seem to be working very good. It cannot  be used 
in practice yet - at least if you want to have reliable results ;-) . To improve,
we would have to implement more meaningful features. Also, a better training 
set might help. Based on those, we would then need to do a hyperparameter 
optimization again that could lead to more meaningful hyperparameter settings
and a better classification.

Remark: When running `script/application.sh` we always get the Prediction  "False"
with confidence "[1. 0.]". This does not seem right to us, but could be 
explained by the extremely bad scores our classifier results in.