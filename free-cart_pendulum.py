import gym as g
from Fuzzy_number_class import fuzzy

STEP = 0.05
# cart_position, pole_angle, push_direction
RULES = [[fuzzy(-2.4, -1, 1, 2.4), fuzzy(-42, -40, -10, 0), fuzzy(-1, -0.5, -0.5, 0)],
         [fuzzy(-2.4, -1, 1, 2.4), fuzzy(0, 10, 40, 42), fuzzy(0, 0.5, 0.5, 1)],
         [fuzzy(-100, -99, -3, -2.4), fuzzy(-15, -10, 10, 15), fuzzy(0.5, 1, 1, 1.5)],
         [fuzzy(2.4, 3, 99, 100), fuzzy(-15, -10, 10, 15), fuzzy(-0.5, 0, 0, 0.5)]]
env = g.make("CartPole-v1")
observation = env.reset()
for _ in range(1000):
    env.render()
    parametres = [fuzzy(observation[0] - 4, observation[0] - 2, observation[0] + 2, observation[0] + 4),
                  fuzzy(observation[2] - 4, observation[2] - 2, observation[2] + 2, observation[2] + 4)]
    force = fuzzy.mass_center(*fuzzy.combine_rules(parametres, RULES, STEP), STEP)
    print(force)
    if force >= 0.7:
        action = 1
    else:
        action = 0
    observation, reward, done, info = env.step(action)
env.close()
