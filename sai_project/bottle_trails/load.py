import pickle

random_forest  = pickle.load(open('./public/static/reg.sav','rb'))
res = random_forest.predict([[6,120,0.45,28.56,0.63,1002,27.5,32.6,5.37]])

svm = pickle.load(open('./public/static/class.sav','rb'))
high = svm.predict([[32,6,120,0.45,28.56,0.63,1002,27.5,32.6,5.37]])
print(res)
print(high)