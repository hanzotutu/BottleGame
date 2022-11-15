from itertools import permutations 
from copy import deepcopy


depth = 4
state = [
    list('ABBC'), 
    list('DEFF'),
    list('EEGH'),
    list('FHDC'),
    list('AICD'),
    list('AHGA'),
    list('GGIC'),
    list('IFID'),
    list('HBEB'),
    list('    '),
    list('    '),
    ]

def displayState(state):
    for i, bottle in enumerate(state):
        print(i, ': ', ''.join(bottle), '|')

def Done(state):
    done = True
    for bottle in state:
        if len(set(''.join(bottle))) != 1:
            done = False
            break
    return done

def moveState(state, n, m):
   # out of range check
    if n >= len(state): return False
    if m >= len(state): return False

    start = ''.join(state[n]).lstrip()
    # empty start bottle
    if start == '': return False
    # full target bottle
    target = ''.join(state[m]).lstrip()
    if len(target) == depth: return False

    # useless movement
    if len(set(start)) == 1:
        if len(start) == depth: return False
        if target == '': return False
    # no match
    if target != '' and target[0] != start[0]: return False

    # can move
    start_idx = ''.join(state[n]).index(start[0])
    if target == '':
        target_idx = depth
    else:
        target_idx = ''.join(state[m]).index(target[0])
    state[m][target_idx-1] = state[n][start_idx]
    state[n][start_idx] = ' '
    while start_idx+1 < depth and target_idx-1 > 0:
        start_idx += 1
        target_idx -= 1
        if state[n][start_idx] == state[m][target_idx]:
            state[m][target_idx-1] = state[n][start_idx]
            state[n][start_idx] = ' '

    # return False for incomplete move 
    if start_idx+1 < depth and target_idx-1 == 0:
        if state[n][start_idx+1] == state[m][0]: return False

    return True

def solveState(state, old_states = set(), nb = 0):
    print(nb, '......')
    if nb == 100: return False

    if Done(state): return True
    if str(state) in old_states: return False

    all_moves = permutations(list(range(len(state))), 2)
    old_states_cpy = deepcopy(old_states)
    old_states_cpy.add(str(state))

    for move in all_moves:
        state_cpy = deepcopy(state)
        if moveState(state_cpy, move[0], move[1]):
            if solveState(state_cpy, old_states_cpy, nb+1):
                print(move[0], '-->', move[1])
                # displayState(state)
                return True

    print('no solution')
    return False


if __name__ == '__main__':
    solveState(state)
    # displayState(state)
