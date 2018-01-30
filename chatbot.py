from textblob.classifiers import NaiveBayesClassifier
train =[("hello",'gre'),("how are you",'gre'),("how do you do",'gre'),
        ("hi I'm nada",'gre'),("do you know this song",'music'),("I need to listen to some good music",'music'),
        ("who's the singer",'music'),("give me the top hits",'music'),("i'm sad play me some music",'music'),
        ("listen to this",'music'),("how do you do?",'gre'),("howdie",'gre'),("what's up",'gre')     
     ]

cl = NaiveBayesClassifier(train) 
 


while True:
	userInput = raw_input(">>> ")
	if cl.classify(userInput) == 'gre':
		print('hello, nice to meet you')
	elif cl.classify(userInput) == 'music':
		print('Lets listen to some music')
	else:
		print("I did not understand what you said")   