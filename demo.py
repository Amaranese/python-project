from sklearn import	tree
# this is a decision tree  it asks each labelled datapoint
#a yes/no question - does it contain data or not then data moves



#[height, weight, shoe size ]
X = [[181,80,44],[177,70,43],[160,60,38], [154, 54, 37], 
[166,65,40],[190,90,47], [175,64,39],[177,70,40],[159,55,37],
[171,75,42],[181,85,43]]

Y = ['male','female', 'female', 'female', 'male','male',
	 'male', 'female', 'male', 'female', 'male']

#clf = classifier
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[185,90,41]])

print (prediction)