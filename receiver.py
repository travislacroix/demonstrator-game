import numpy as np
import random
import util

class Receiver(object):
    def __init__(self, signals, actions, strategy, recordChoices=True, recordStrats=True):
        self.signals = signals
        self.actions = actions
        self.strategy = strategy
        self._recordChoices = recordChoices
        self._recordStrats = recordStrats
        self._choiceHistory = []
        self._stratHistory = np.array([util.matNormalize(self.strategy)])

    def getAction(self, signal, selector, state):
        raise NotImplementedError

    def getPaid(self, amount):
        raise NotImplementedError

    def getNormalizedStrategy(self):
        return util.matNormalize(self.strategy)

    def getChoiceHistory(self):
        return self._choiceHistory

    def getStratHistory(self):
        return self._stratHistory

    def getProb(self, act, sig):
        raise NotImplementedError

    def recordStrategy(self):
        self._stratHistory = np.concatenate((self._stratHistory, [self.getNormalizedStrategy()]))


class AtomicReceiver(Receiver):
    def getAction(self, signal, selector, state):
        theAct = util.weighted_choice(zip(self.actions, self.strategy[sum(signal)]))
        if self._recordChoices:
            self._choiceHistory.append((signal, theAct))
        return theAct

    def getPaid(self, amount):
        prevChoice = self._choiceHistory[-1]
        if self.strategy[sum(prevChoice[0]), prevChoice[1]] + amount > 0:
            self.strategy[sum(prevChoice[0]), prevChoice[1]] += amount
        if self._recordStrats:
            self.recordStrategy()

    def getProb(self, act, sig):
        return self.getNormalizedStrategy()[sum(sig), act]


class Observer(AtomicReceiver):

    def getAction(self, signal, selector, state):
        if selector > 0.10:
            return AtomicReceiver.getAction(self, signal, selector, state)
        indices = np.where(self.getNormalizedStrategy()[signal[0]] == self.getNormalizedStrategy()[signal[0]].max())
        newActs = indices[0]
        theAct = util.weighted_choice(zip(newActs, self.strategy[sum(signal)]))
        if self._recordChoices:
            self._choiceHistory.append((signal, theAct))
        return theAct

#    def getPaid(self, amount):
#        prevChoice = self._choiceHistory[-1]
#        if self.strategy[sum(prevChoice[0]), prevChoice[1]] + amount > 0:
#            self.strategy[sum(prevChoice[0]), prevChoice[1]] += amount
#        if self._recordStrats:
#            self.recordStrategy()

#    def getProb(self, act, sig):
#        return self.getNormalizedStrategy()[sum(sig), act]

#    def getAction(self, signal, selector):
#        if selector > 1:
#            return AtomicReceiver.getAction(self, signal, selector)
#        indices = np.where(self.getNormalizedStrategy()[signal] == self.getNormalizedStrategy()[signal].max())
#        if len(indices[0]) > 1:
#            return AtomicReceiver.getAction(self, signal, selector)
#        theAct = indices[0]
#        if self._recordChoices:
#            self._choiceHistory.append((signal, theAct))
#        return theAct
