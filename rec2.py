import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#CHALLENGE part 1 of 3 - write your own fetch and format method for a different recommendation
#dataset. Here a good few https://gist.github.com/entaroadun/1653794 
#And take a look at the fetch_movielens method to see what it's doing 
#

#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
#create loss means our loss function measures diff between models prediction and 
#desired output. to minimize during training to make more accurate over time
# WARP weighted approximate rank pairwise we can choose several
#looks at existing user raiting pairs and predicts rankings for each
#gradient descent algorythm that predicts better over time 
#past, content base and similar user ratings are considered



#create model
model = LightFM(loss='warp')
#train model
model.fit(data['train'], epochs=30, num_threads=2)


#CHALLENGE part 3 of 3 - Modify this function so that it parses your dataset correctly to retrieve
#the necessary variables (products, songs, tv shows, etc.)
#then print out the recommended results 

def sample_recommendation(model, data, user_ids):

    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        
			#generate rec and store in score predict method of our model 
			#user id as first parm, then list of each movie the a range of numpy will give us every number from 0 - num of items 
			#then sort in order of score 
        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)
            
sample_recommendation(model, data, [3, 25, 450])