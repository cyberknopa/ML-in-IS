## Spam-filters

### Iterative approach
The dataset used for training [2007 TREC Public Spam Corpus](https://plg.uwaterloo.ca/~gvcormac/treccorpus07/)
A conditional validation process was used to evaluate the effectiveness of the work. The main data set is divided into a training set (50%) and a test set (50%). The Natural language toolkit package was used for stemming.

Classification accuracy: 71.9%

### MinHash+LSH algorithm
To perform a string comparison operation with an estimate of the costs of a sublinear query. MinHash converts sets of string tokens into short signatures, then LSH is applied

Classification accuracy: 87.7%

### Naive Bayes classifer
A classifier is a machine learning model that is used to discriminate different objects based on certain features. A Naive Bayes classifier is a probabilistic machine learning model that’s used for classification task. The crux of the classifier is based on the Bayes theorem.

Classification accuracy: 95.3%
