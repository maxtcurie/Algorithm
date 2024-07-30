import numpy as np

def viterbi(obs, states, start_prob, trans_prob, emit_prob):
    """
    Viterbi algorithm to find the most probable sequence of hidden states.

    Parameters:
    obs: list of observations
    states: list of states
    start_prob: dict of start probabilities
    trans_prob: dict of transition probabilities
    emit_prob: dict of emission probabilities

    Returns:
    path: list of the most probable sequence of states
    """
    # Initialize variables
    n_obs = len(obs)
    n_states = len(states)

    # Initialize the Viterbi matrix and path matrix
    V = np.zeros((n_states, n_obs))
    path = np.zeros((n_states, n_obs), dtype=int)

    # Initialization step
    for i, state in enumerate(states):
        V[i, 0] = start_prob[state] * emit_prob[state][obs[0]]
        path[i, 0] = i

    # Recursion step
    for t in range(1, n_obs):
        new_path = np.zeros((n_states, n_obs), dtype=int)
        for i, state in enumerate(states):
            prob, state_index = max(
                (V[j, t-1] * trans_prob[states[j]][state] * emit_prob[state][obs[t]], j)
                for j in range(n_states)
            )
            V[i, t] = prob
            new_path[i, :t] = path[state_index, :t]
            new_path[i, t] = i
        path = new_path

    # Termination step
    max_prob = -1
    best_path = None
    for i in range(n_states):
        if V[i, n_obs-1] > max_prob:
            max_prob = V[i, n_obs-1]
            best_path = path[i]

    return [states[state_index] for state_index in best_path], max_prob

# Example usage
obs = ['normal', 'cold', 'dizzy']
states = ['Healthy', 'Fever']
start_prob = {'Healthy': 0.6, 'Fever': 0.4}
trans_prob = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6}
}
emit_prob = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
}

path, prob = viterbi(obs, states, start_prob, trans_prob, emit_prob)
print("Most probable sequence of states:", path)
print("Probability of the sequence:", prob)
