ReadMe.txt

In order to implement the demonstrator game, open the Demonstrator_Game.py file. 

The line of code at the bottom:

	runExperiment(['demo'], [1, 0], 1000, 10000, [7,8], 'data/Ten_Percent_Data/exp1_')

gives the parameters for a particular run. The parameters are as follows:

	gameTypes, reinforcementValues, numtrials, numiters, Nvals, outroot

The gameTypes options are 'atomic' or 'demo' for an atomic game or a demonstration game.
The reinforcement values are [Success,Failure]. We use [1,0] for positive reinforcement.
The numTrials can be any positive integer. We use 1000 for our averages.
The numIters is the number of times the game is played per trial for reinforcement learning. We look at short term evolution: 10^5 plays.
The Nvals is the dimension of the game in the form [n1,n2,n3,...,ni]. We use [2,3,4,5,6,7,8].