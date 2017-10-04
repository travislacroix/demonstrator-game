import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# NOTE: Some of these are redundant for the particular implementation of the demonstrator game, but are used for a different implementation.
# In practice, this file was note used, but raw data was analysed manually using matlab.

def writeAverages():

    Apays = [[], [], [], [], [], []]
    Npays = [[], [], [], [], [], []]
    finalA = [[], [], [], [], [], []]
    finalN = [[], [], [], [], [], []]
    avgA = []
    avgN = []

    for N in [2,3,4,5,6,7]:

        for i in range(100):

            Apays[N-2].append(np.loadtxt('data/exp1_N'+str(N)+'_recA_trial'+str(i)+'_exppay.txt'))
            Npays[N-2].append(np.loadtxt('data/exp1_N'+str(N)+'_neggame_trial'+str(i)+'_exppay.txt'))
            #Npays.append(np.loadtxt('data/exp1_N'+str(N)+'_recN_trial'+str(i)+'_exppay.txt'))

        finalA[N-2] = map(lambda x: x[-1], Apays[N-2])
        finalN[N-2] = map(lambda x: x[-1], Npays[N-2])
        avgA.append(np.mean(finalA[N-2]))
        avgN.append(np.mean(finalN[N-2]))
        np.savetxt('data/exp1_N'+str(N)+'_recA_finalexps.txt', finalA[N-2])
        np.savetxt('data/exp1_N'+str(N)+'_neggame_finalexps.txt', finalN[N-2])

    avgdiff = map(lambda x: avgN[x] - avgA[x], range(len(avgA)))
    np.savetxt('data/exp1_avg_recA.txt', avgA)
    np.savetxt('data/exp1_avg_neg.txt', avgN)
    np.savetxt('data/exp1_avg_negMINUSrecA.txt', avgdiff)

def writeExp2Averages():

    basePays = [[], [], [], [], [], []]
    negPays = [[], [], [], [], [], []]
    finalBase = [[], [], [], [], [], []]
    finalNeg = [[], [], [], [], [], []]
    avgB = []
    avgN = []

    for N in [2,3,4,5,6,7]:

        for i in range(10):

            basePays[N-2].append(np.loadtxt('data/exp2_N'+str(N)+'_funcgame_trial'+str(i)+'_exppay.txt'))
            negPays[N-2].append(np.loadtxt('data/exp2_N'+str(N)+'_funcgame_constneg_trial'+str(i)+'_exppay.txt'))

        finalBase[N-2] = map(lambda x: x[-1], basePays[N-2])
        finalNeg[N-2] = map(lambda x: x[-1], negPays[N-2])
        avgB.append(np.mean(finalBase[N-2]))
        avgN.append(np.mean(finalNeg[N-2]))
        np.savetxt('data/exp2_N'+str(N)+'_constbase_finalexps.txt', finalBase[N-2])
        np.savetxt('data/exp2_N'+str(N)+'_constneg_finalexps.txt', finalNeg[N-2])

    np.savetxt('data/exp2_avg_constbase.txt', avgB)
    np.savetxt('data/exp2_avg_constneg.txt', avgN)

def writeExp2FuncWeight():

    baseFunc = [[], [], [], [], [], []]
    negFunc = [[], [], [], [], [], []]
    finalBase = [[], [], [], [], [], []]
    finalNeg = [[], [], [], [], [], []]
    avgB = []
    avgN = []

    for N in [2,3,4,5,6,7]:

        for i in range(10):

            baseFunc[N-2].append(np.load('data/exp2_N'+str(N)+'_funcgame_trial'+str(i)+'_recfunc.npy'))
            negFunc[N-2].append(np.load('data/exp2_N'+str(N)+'_funcgame_constneg_trial'+str(i)+'_recfunc.npy'))

        finalBase[N-2] = map(lambda x: x[-1][0], baseFunc[N-2])
        finalNeg[N-2] = map(lambda x: x[-1][0], negFunc[N-2])
        avgB.append(np.mean(finalBase[N-2]))
        avgN.append(np.mean(finalNeg[N-2]))
        np.savetxt('data/exp2_N'+str(N)+'_constbase_negWeights.txt', finalBase[N-2])
        np.savetxt('data/exp2_N'+str(N)+'_constneg_negWeights.txt', finalNeg[N-2])

    np.savetxt('data/exp2_avg_negWeight_constbase.txt', avgB)
    np.savetxt('data/exp2_avg_negWeight_constneg.txt', avgN)

def writeExp45Averages():

    Pays4 = [[], [], [], [], [], []]
    Pays5 = [[], [], [], [], [], []]
    final4 = [[], [], [], [], [], []]
    final5 = [[], [], [], [], [], []]
    avgB = []
    avgN = []

    for N in [2,3,4,5,6,7]:

        for i in range(100):

            Pays4[N-2].append(np.loadtxt('data/exp4_N'+str(N)+'_semi-fixed_1,0_trial'+str(i)+'_exppay.txt'))
            Pays5[N-2].append(np.loadtxt('data/exp5_N'+str(N)+'_semi-fixed_1,0_trial'+str(i)+'_exppay.txt'))

        final4[N-2] = map(lambda x: x[-1], Pays4[N-2])
        final5[N-2] = map(lambda x: x[-1], Pays5[N-2])
        avgN.append(np.mean(final4[N-2]))
        avgB.append(np.mean(final5[N-2]))
        np.savetxt('data/exp4_N'+str(N)+'_semi-fixed_1,0_finalexps.txt', final4[N-2])
        np.savetxt('data/exp5_N'+str(N)+'_semi-fixed_1,0_finalexps.txt', final5[N-2])

    np.savetxt('data/exp4_avg_constneg.txt', avgN)
    np.savetxt('data/exp5_avg_constbase.txt', avgB)
	
def writeTtests():

    ttests = []
    finalA = []
    finalN = []
    for N in [2,3,4,5,6,7]:
        finalA.append(np.loadtxt('data/exp1_N'+str(N)+'_recA_finalexps.txt'))
        finalN.append(np.loadtxt('data/exp1_N'+str(N)+'_neggame_finalexps.txt'))
        ttests.append(stats.ttest_ind(finalA[-1], finalN[-1], equal_var=False))
    print ttests
    np.savetxt('data/exp1_analysis_ttests.txt', ttests)

def saveLinearRegression():

    avgdiff = np.loadtxt('data/exp1_avg_negMINUSrecA.txt')
    np.savetxt('data/exp1_avgdiff_linreg.txt', stats.linregress([2,3,4,5,6,7], avgdiff))

def plotLinearRegression():

    avgdiff = np.loadtxt('data/exp1_avg_negMINUSrecA.txt')
    slope, intercept, rval, pval, err = np.loadtxt('data/exp1_avgdiff_linreg.txt')
    x = [2,3,4,5,6,7]
    xx = np.linspace(1,8,200)
    theline = map(lambda x: intercept + slope*x, xx)
    plt.plot(x, avgdiff, 'bo')
    plt.plot(xx, theline, 'r')
    plt.xlabel(r'$n$')
    plt.ylabel(r'$Diff_n$')
    plt.title('Difference in Mean Payoffs vs. Number of States')
    plt.show()

def plotHistograms():

    withLabels = True

    for i in [2,3,4,5,6,7]:
        neg = np.loadtxt('data/exp1_N'+str(i)+'_neggame_finalexps.txt')
        atom = np.loadtxt('data/exp1_N'+str(i)+'_recA_finalexps.txt')
        plt.hist([neg, atom], range=(.5, .999999), label=['neg','atom'])
        fname = 'data/exp1_hist_N'+str(i)
        if withLabels:
            plt.title('Payoff distribution for N='+str(i))
            plt.ylabel('Number of trials')
            plt.xlabel(r'$\pi ( \sigma , \rho )$')
            plt.legend(loc='upper left')
            fname = fname + '_withlabels'
        fname = fname + '.png'
        plt.savefig(fname)
        plt.clf()
