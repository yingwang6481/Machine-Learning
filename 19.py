# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:41:03 2017

@author: wangying
"""

import tensorflow as tf
import numpy as np

#Save to file
#remember to define the same dtype and shape when restore
#W=tf.Variable([[1,2,3],[3,4,5]],dtype=tf.float32,name='weights')
#b=tf.Variable([[1,2,3]],dtype=tf.float32,name='biases')
#
#init=tf.initialize_all_variables()
#
#
#saver=tf.train.Saver()
#
#sess=tf.Session()
#sess.run(init)
#save_path=saver.save(sess,"C:/l/my_net/save_net.ckpt")
#print("Save to path:",save_path)
#print("W :",sess.run(W))
#print("b: ",sess.run(b))

#restore variables
#redefine teh same shape and same type for your variables

W=tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name="weights")
b=tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name="biases")


#not need init step

saver =tf.train.Saver()
sess=tf.Session()
saver.restore(sess,"C:/l/my_net/save_net.ckpt")
print("weights: ",sess.run(W))
print("biases",sess.run(b))