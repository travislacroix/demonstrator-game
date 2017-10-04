import numpy as np
import random
import util

from sender import Sender, Demonstrator
from receiver import *

class Game(object):

	def __init__(self, sender, receiver, states, signals, actions, payoffs=[], stateProbs=[], recordHist=True):
		self.sender = sender
		self.receiver = receiver
		self.states = states
		self.signals = signals
		self.actions = actions
		self.payoffs = payoffs
		self.stateProbs = util.normalize(np.ones(len(self.states)))
		self._recordHist = recordHist
		self._payHistory = []
		self._maxPossPay = sum([self.stateProbs[i]*self.payoffs[i, i] for i in self.states])

	def onePlay(self):
		theState = np.random.choice(self.states, p=self.stateProbs)
		selector = random.random()
		theSignal = self.sender.getSignal(theState, selector)
		theAct = self.receiver.getAction(theSignal,selector,theState)
		thePayoff = self.payoffs[theState, theAct]
		self.sender.getPaid(thePayoff)
		self.receiver.getPaid(thePayoff)
		if self._recordHist:
			self._payHistory.append(self.getExpectedPayoff())

	def getExpectedPayoff(self):
		theSum = 0.0
		for s in self.states:
			theSum += sum([self.sender.getProb(sig, s)*self.receiver.getProb(s, sig) for sig in self.signals])

		return theSum / len(self.states)

	def recordPayoff(self):
		self._payHistory.append(self.getExpectedPayoff())

class NGame(Game):

	def __init__(self, N, payoffs=[], stateProbs=[]):
		realN = N
		states = range(realN)
		actions = range(realN)
		signals = [[i] for i in range(N)]
		if payoffs == []:
			payoffs = np.identity(realN)
		sender = Sender(states, signals, np.ones((len(states),len(signals))))
		receiver = AtomicReceiver(signals, actions, np.ones((len(signals),len(actions))))
		Game.__init__(self, sender, receiver, states, signals, actions, payoffs)

class DemoGame(Game):

	def __init__(self, N, payoffs=[], stateProbs=[]):
		realN = N
		states = range(realN)
		actions = range(realN)
		signals = [[i] for i in range(N)]
		if payoffs == []:
			payoffs = np.identity(realN)
		sender = Demonstrator(states, signals, np.ones((len(signals), len(actions))))
		receiver = Observer(signals, actions, np.ones((len(signals),len(actions))))
		Game.__init__(self, sender, receiver, states, signals, actions, payoffs)
