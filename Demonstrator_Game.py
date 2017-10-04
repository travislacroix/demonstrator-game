import numpy as np
import itertools as it
import random
import matplotlib.pyplot as plt

from gameObject import Game, NGame, DemoGame

def writeList(theList, fn):
	thefile = open(fn, 'w')
	for item in theList:
		print>>thefile, item

def runExperiment(gameTypes, reinforcementValues, numtrials, numiters, Nvals, outroot, recordPayoff=200):

	for N in Nvals:

		print 'MOVING TO N = ' + str(N)

		for gameType in gameTypes:

			print 'MOVING TO GAMETYPE: ' + gameType
			print 'DEMO PROB: ' + str(0.10) #CHANGE THIS FOR DIFFERENT PROBS

			for i in range(numtrials):

				#print 'MOVING TO TRIAL ' + str(i)

				fulloutroot = outroot+'N'+str(N)+'_'+gameType+'_'+str(reinforcementValues)[1:-1].replace(' ','')+'_trial'+str(i)
				outpay = fulloutroot+'_exppay.txt'
				outsend = fulloutroot+'_sendstrat'
				outrec = fulloutroot+'_recstrat'

				payoffs = np.identity(N)*reinforcementValues[0]

				if reinforcementValues[1] != 0:
					for row in range(len(payoffs)):
						for col in range(len(payoffs[0])):
							if row != col:
								payoffs[row][col] += reinforcementValues[1]

				if gameType == 'atomic':
					game = NGame(N, payoffs)
				elif gameType == 'demo':
					game = DemoGame(N, payoffs)
				else:
					assert False, "Invalid game type specified"
				for j in range(numiters):

					#print 'MOVING TO ITER ' + str(j)

					game.onePlay()

					if j % recordPayoff == 0:
						game.recordPayoff()

				print game._payHistory[-1]
				writeList(game._payHistory, outpay)
				np.save(outsend, game.sender._stratHistory[-1])
				np.save(outrec, game.receiver._stratHistory[-1])

#For actual experiment, parameters should be:
#	runExperiment(['atomic','demo'], [1,0], 1000, 10000000, [2, 3, 4, 5, 6], 'data/exp_')
runExperiment(['demo'], [1, 0], 1000, 10000, [7,8], 'data/Ten_Percent_Data/exp1_')
