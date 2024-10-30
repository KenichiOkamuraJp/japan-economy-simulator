from population import Population
from potential_growth_rate import PotentialGrowthRate
import pandas as pd

pop = Population()
potential = PotentialGrowthRate()

for year in range(2025, 2071):

    potential.setParameter(pop)
    if not potential.execute(year):
        raise

df = pd.DataFrame(potential.output())
df.to_excel('test.xlsx', index=False, header=True)
