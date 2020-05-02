import random


class EpsilonGreedy:
    def __init__(self, epsilon=0.1):
        self.epsilon = epsilon
        self.arms_no = 0
        self.states = dict()
        self.expected_payouts = dict()
        random.seed()

    def initialize(self, arms_no):
        self.arms_no = arms_no
        self.states = {arm_index: {'plays': 0, 'payouts': 0} for arm_index in range(self.arms_no)}

    def predict(self):
        non_played_arms = list(set(self.states.keys()) - set(self.expected_payouts.keys()))
        if non_played_arms:
            # if we haven't played every arm at least once, explore that arm
            arm_index = non_played_arms[0]
            print("Playing arm: {} for first time!".format(arm_index))
            self.states[arm_index]['plays'] += 1
            self.expected_payouts[arm_index] = self.states[arm_index]['payouts']/self.states[arm_index]['plays']
            return arm_index
        else:
            # flip a coin
            rand = random.random()
            print("Random: {}".format(rand))
            if rand <= self.epsilon:
                # run exploration strategy by randomly picking one of the arms
                arm_index = random.choice(list(self.states))
                print("Exploration --> selected arm: {}".format(arm_index))
                self.states[arm_index]['plays'] += 1
                self.expected_payouts[arm_index] = self.states[arm_index]['payouts']/self.states[arm_index]['plays']
                return arm_index
            else:
                # run exploitation strategy by sampling the arm with maximum expected payout so far
                for k in sorted(self.expected_payouts, key=self.expected_payouts.get, reverse=True):
                    arm_index = k
                    print("Exploitation --> expected payouts: {}".format(self.expected_payouts))
                    print("Exploitation --> selected arm: {}".format(arm_index))
                    self.states[arm_index]['plays'] += 1
                    self.expected_payouts[arm_index] = self.states[arm_index]['payouts']/self.states[arm_index]['plays']
                    return arm_index


    def update(self, arm_index, payout):
        if payout > 0:
            self.states[arm_index]['payouts'] += 1
        self.expected_payouts[arm_index] = self.states[arm_index]['payouts']/self.states[arm_index]['plays']

