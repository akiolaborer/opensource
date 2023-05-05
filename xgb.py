import xgboost
import numpy
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

#訓練データ　train
dataset = datasets.load_breast_cancer()
x, y = dataset.data, dataset.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3,
                                                            shuffle = True, 
                                                       random_state = 42, 
                                                         stratify = y)

dtrain = xgboost.DMatrix(x_train, label = y_train)
dtest = xgboost.DMatrix(x_test, label = y_test)

#テストデータ test
xgboost_params = {
    'objective': 'binary:logistic',

    'eval_metric': 'logloss',
}
evals = [(dtrain, 'train'), (dtest, 'eval')]
result = {}
bst = xgboost.train(xgboost_params,
                    dtrain,
                    num_boost_round = 1000,
                    evals = evals,
                    evals_result = result,
                    )

y_pred_proba = bst.predict(dtest)
y_pred = numpy.where(y_pred_proba > 0.5, 1, 0)
acc = accuracy_score(y_test, y_pred)
print('Accuracy:', acc)

train_metric = result['train']['logloss']
pyplot.plot(train_metric, label='train logloss')
eval_metric = result['eval']['logloss']
pyplot.plot(eval_metric, label='eval logloss')
pyplot.grid()
pyplot.legend()
pyplot.xlabel('rounds')
pyplot.ylabel('logloss')
pyplot.show()


