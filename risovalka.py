import plotly.express as px
from clas import nechetkoe as nech
rules = [[nech(1, 2, 3, 4), nech(1, 2, 3, 4)], [nech(5.5, 6, 7, 8), nech(3, 4, 5, 6)], [nech(3,4,5,6), nech(5, 8, 9, 10)]]
situation = nech(3,4,5,6)
x, y = situation.combine_rules(rules, 0.005)
fig = px.scatter(x=x, y=y)
fig.show()
