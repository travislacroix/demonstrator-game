import numpy as np
import random
import util

class Sender(object):

	def __init__(self, states, signals, strategy, recordChoices=True, recordStrats=True):
		self.states = states
		self.signals = signals
		self.strategy = strategy
		self._recordChoices = recordChoices
		self._recordStrats = recordStrats
		self._choiceHistory = []
		self._stratHistory = np.array([util.matNormalize(self.strategy)])

	def getSignal(self, state, selector):
		theSig = util.weighted_choice(zip(self.signals, self.strategy[state]))
		if self._recordChoices:
			self._choiceHistory.append((state, theSig))
		return theSig

	def getPaid(self, amount):
		prevChoice = self._choiceHistory[-1]
		if self.strategy[prevChoice[0], sum(prevChoice[1])] + amount > 0:
			self.strategy[prevChoice[0], sum(prevChoice[1])] += amount
			if self._recordStrats:
				self.recordStrategy()

	def getNormalizedStrategy(self):
		return util.matNormalize(self.strategy)

	def getChoiceHistory(self):
		return self._choiceHistory

	def getStratHistory(self):
		return self._stratHistory

	def getProb(self, sig, state):
		return self.getNormalizedStrategy()[state, sum(sig)]

	def recordStrategy(self):
		self._stratHistory = np.concatenate((self._stratHistory, [self.getNormalizedStrategy()]))

class Demonstrator(Sender):

	#Gets rid of the least likely options
	def getSignal(self, state, selector):
		#selector = random.random()
		if selector > 0.10:
			return Sender.getSignal(self, state, selector)
		indices = np.where(self.getNormalizedStrategy()[state] == self.getNormalizedStrategy()[state].max())
		newSignals = [[i] for i in indices[0]]
		theSig = util.weighted_choice(zip(newSignals, self.strategy[state]))
		if self._recordChoices:
			self._choiceHistory.append((state, theSig))
		return theSig

	# #NEW GetSignal is supposed to randomize over the most likely option.
	# def getSignal(self, state, selector):
	# 	if selector > 1:
	# 		return Sender,getSignal(self, state, selector)
	# 	indices = np.where(self.getNormalizedStrategy()[state] == self.getNormalizedStrategy()[state].max())
	# 	likelySignals = [[i] for i in indices[0]]
	# 	theSig = util.weighted_choice(zip(likelySignals, self.strategy[state]))
	# 	if self._recordChoices:
	# 		self._choiceHistory.append((state,theSig))
	# 	return theSig

 #	def getProb(self, sig, state):
 #		return self.getNormalizedStrategy()[state, sum(sig)]
