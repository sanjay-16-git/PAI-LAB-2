import numpy as np
class GridWorldMDP:
    def __init__(self, size, goal, trap):
        self.size = size
        self.goal = goal
        self.trap = trap
        self.state_space = [(i, j) for i in range(size) for j in range(size)]
        self.action_space = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.transitions = self.build_transitions()
        self.rewards = self.build_rewards()
    def build_transitions(self):
        transitions = {}
        for state in self.state_space:
            transitions[state] = {}
            for action in self.action_space:
                transitions[state][action] = self.calculate_transitions(state, action)
        return transitions
    def calculate_transitions(self, state, action):
        i, j = state
        if action == 'UP':
            return self.validate_state(i - 1, j)
        elif action == 'DOWN':
            return self.validate_state(i + 1, j)
        elif action == 'LEFT':
            return self.validate_state(i, j - 1)
        elif action == 'RIGHT':
            return self.validate_state(i, j + 1)
    def validate_state(self, i, j):
        i = max(0, min(i, self.size - 1))
        j = max(0, min(j, self.size - 1))
        return [(1.0, (i, j))]
    def build_rewards(self):
        rewards = {}
        for state in self.state_space:
            rewards[state] = -1.0
        rewards[self.goal] = 0.0
        rewards[self.trap] = -10.0
        return rewards
def value_iteration(mdp, gamma=0.9, epsilon=0.01):
    state_values = {state: 0.0 for state in mdp.state_space}
    iteration = 0
    while True:
        delta = 0
        new_values = state_values.copy()
        print(f"\nIteration {iteration}")
        for state in mdp.state_space:
            if state == mdp.goal or state == mdp.trap:
                continue
            v = state_values[state]
            new_values[state] = max(
                sum(p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][action])
                for action in mdp.action_space
            )
            delta = max(delta, abs(v - new_values[state]))
        state_values = new_values
        for s in sorted(state_values):
            print(f"State {s}: {round(state_values[s], 2)}")
        iteration += 1
        if delta < epsilon:
            break
    return state_values
def policy_iteration(mdp, gamma=0.9):
    policy = {state: np.random.choice(mdp.action_space)
              for state in mdp.state_space
              if state != mdp.goal and state != mdp.trap}
    state_values = {state: 0.0 for state in mdp.state_space}
    iteration = 0
    while True:
        print(f"\nPolicy Iteration Step {iteration}")
        while True:
            delta = 0
            for state in mdp.state_space:
                if state == mdp.goal or state == mdp.trap:
                    continue
                v = state_values[state]
                action = policy[state]
                state_values[state] = sum(
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][action]
                )
                delta = max(delta, abs(v - state_values[state]))
            if delta < 0.01:
                break
        print("State Values:")
        for s in sorted(state_values):
            print(f"State {s}: {round(state_values[s], 2)}")
        policy_stable = True
        for state in mdp.state_space:
            if state == mdp.goal or state == mdp.trap:
                continue
            old_action = policy[state]
            policy[state] = max(
                mdp.action_space,
                key=lambda a: sum(
                    p * (mdp.rewards[next_state] + gamma * state_values[next_state])
                    for p, next_state in mdp.transitions[state][a]
                )
            )
            if old_action != policy[state]:
                policy_stable = False
        print("Policy:")
        for s in policy:
            print(f"State {s}: {policy[s]}")
        iteration += 1
        if policy_stable:
            break
    return policy, state_values
size = 3
goal = (2, 2)
trap = (1, 1)
mdp = GridWorldMDP(size, goal, trap)
print("=== VALUE ITERATION ===")
vi_values = value_iteration(mdp)
print("\n=== FINAL VALUE FUNCTION ===")
for s in sorted(vi_values):
    print(f"{s}: {round(vi_values[s], 2)}")
print("\n=== POLICY ITERATION ===")
policy, values = policy_iteration(mdp)
print("\nFinal Policy:")
for s in policy:
    print(f"{s}: {policy[s]}")
