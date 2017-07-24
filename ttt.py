import tensorflow as tf 
import numpy as np 

TRAINING = "train.csv"
TESTING = "test.csv"

training = tf.contrib.learn.datasets.base.load_csv_with_header(filename = TRAINING,target_dtype = np.int , features_dtype = np.int)
testing = tf.contrib.learn.datasets.base.load_csv_with_header(filename = TESTING,target_dtype = np.int , features_dtype = np.int)

feature_columns = [tf.contrib.layers.real_valued_column("",dimension = 9)]
classifier = tf.contrib.learn.DNNClassifier(feature_columns = feature_columns ,hidden_units = [10,20,40,20,10] ,n_classes = 5 ,model_dir = "/home/israel/icog/tic tac toe/data")


def get_train_inputs():
    x = tf.constant(training.data)
    y = tf.constant(training.target)
    return x,y

def get_test_inputs():
    x = tf.constant(testing.data)
    y = tf.constant(testing.target)
    return x,y


# fit model
classifier.fit(input_fn= get_train_inputs,steps= 2000)
accuracy_score = classifier.evaluate(input_fn = get_test_inputs , steps = 1)["accuracy"]
print ("\n Test Accuracy :  \n",accuracy_score)