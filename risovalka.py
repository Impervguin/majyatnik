import plotly.express as px
from Fuzzy_number_class import fuzzy
rules = [[fuzzy(1, 2, 3, 4),fuzzy(1, 2, 3, 4), fuzzy(1, 2, 3, 4)], [fuzzy(5.5, 6, 7, 8),fuzzy(5.5, 6, 7, 8),fuzzy(3, 4, 5, 6)], [fuzzy(3,4,5,6),fuzzy(3,4,5,6),fuzzy(5, 8, 9, 10)]]
situation = [fuzzy(3,4,5,6), fuzzy(3,4,5,6)]
x, y = fuzzy.combine_rules(situation, rules, 0.005)
fig = px.scatter(x=x, y=y)
fig.show()
