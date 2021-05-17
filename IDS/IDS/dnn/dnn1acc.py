import pandas as pd
from sklearn.metrics import (precision_score, recall_score,f1_score, accuracy_score,mean_squared_error,mean_absolute_error, roc_curve, classification_report,auc)


testdata = pd.read_csv('dnnres/dnn1predicted.txt', header=None)
traindata = pd.read_csv('dnnres/expected.txt', header=None)


y_train1 = traindata
y_pred = testdata
accuracy = accuracy_score(y_train1, y_pred)
recall = recall_score(y_train1, y_pred , average="binary")
precision = precision_score(y_train1, y_pred , average="binary")
f1 = f1_score(y_train1, y_pred, average="binary")

print("DOS:")
print("\tAccuracy")
print("\t%.3f\n" %accuracy)
print("\tPrecision")
print("\t%.3f\n" %precision)
print("\tRecall")
print("\t%.3f\n" %recall)
print("\tF1 score")
print("\t%.3f" %f1)

print('\n')

testdata = pd.read_csv('dnnres/dnn2predicted.txt', header=None)
traindata = pd.read_csv('dnnres/expected.txt', header=None)


y_train1 = traindata
y_pred = testdata
accuracy = accuracy_score(y_train1, y_pred)
recall = recall_score(y_train1, y_pred , average="binary")
precision = precision_score(y_train1, y_pred , average="binary")
f1 = f1_score(y_train1, y_pred, average="binary")

print("U2R:")
print("\tAccuracy")
print("\t%.3f\n" %accuracy)
print("\tPrecision")
print("\t%.3f\n" %precision)
print("\tRecall")
print("\t%.3f\n" %recall)
print("\tF1 score")
print("\t%.3f" %f1)
print("\n" )


testdata = pd.read_csv('dnnres/dnn3predicted.txt', header=None)
traindata = pd.read_csv('dnnres/expected.txt', header=None)


y_train1 = traindata
y_pred = testdata
accuracy = accuracy_score(y_train1, y_pred)
recall = recall_score(y_train1, y_pred , average="binary")
precision = precision_score(y_train1, y_pred , average="binary")
f1 = f1_score(y_train1, y_pred, average="binary")

print("PROBE:")
print("\tAccuracy")
print("\t%.3f\n" %accuracy)
print("\tPrecision")
print("\t%.3f\n" %precision)
print("\tRecall")
print("\t%.3f\n" %recall)
print("\tF1 score")
print("\t%.3f" %f1)
print("\n" )


testdata = pd.read_csv('dnnres/dnn4predicted.txt', header=None)
traindata = pd.read_csv('dnnres/expected.txt', header=None)


y_train1 = traindata
y_pred = testdata
accuracy = accuracy_score(y_train1, y_pred)
recall = recall_score(y_train1, y_pred , average="binary")
precision = precision_score(y_train1, y_pred , average="binary")
f1 = f1_score(y_train1, y_pred, average="binary")

print("R2L:")
print("\tAccuracy")
print("\t%.3f\n" %accuracy)
print("\tPrecision")
print("\t%.3f\n" %precision)
print("\tRecall")
print("\t%.3f\n" %recall)
print("\tF1 score")
print("\t%.3f" %f1)
print("\n" )

testdata = pd.read_csv('dnnres/dnn5predicted.txt', header=None)
traindata = pd.read_csv('dnnres/expected.txt', header=None)


