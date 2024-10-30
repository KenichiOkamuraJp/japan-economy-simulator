import pandas as pd
import numpy as np
import math

def convert(data: list) -> list:
  reply = []
  subset_potential_growth_rate = []
  subset_total_factor_productivity = []
  subset_capital_stock = []
  subset_hours_worked = []
  subset_number_of_employed = []
  pre_year = data[0]['year']

  for record in data:
    if pre_year != record['year']:
      reply.append({
        'year' : pre_year,
        'potential_growth_rate' : 0 if subset_potential_growth_rate == [] else np.mean(subset_potential_growth_rate),
        'total_factor_productivity' : 0 if subset_total_factor_productivity == [] else  np.mean(subset_total_factor_productivity),
        'capital_stock' : 0 if subset_capital_stock == [] else  np.mean(subset_capital_stock),
        'hours_worked' : 0 if subset_hours_worked == [] else  np.mean(subset_hours_worked),
        'number_of_employed' : 0 if subset_number_of_employed == [] else  np.mean(subset_number_of_employed),
      })
      subset_potential_growth_rate.clear()
      subset_total_factor_productivity.clear()
      subset_capital_stock.clear()
      subset_hours_worked.clear()
      subset_number_of_employed.clear()
      pre_year = record['year']

    if not math.isnan(record['potential_growth_rate']):
      subset_potential_growth_rate.append(record['potential_growth_rate'])
    if not math.isnan(record['total_factor_productivity']):
      subset_total_factor_productivity.append(record['total_factor_productivity'])
    if not math.isnan(record['capital_stock']):
      subset_capital_stock.append(record['capital_stock'])    
    if not math.isnan(record['hours_worked']):
      subset_hours_worked.append(record['hours_worked'])
    if not math.isnan(record['number_of_employed']):
      subset_number_of_employed.append(record['number_of_employed'])

  reply.append({
    'year' : pre_year,
    'potential_growth_rate' : 0 if subset_potential_growth_rate == [] else np.mean(subset_potential_growth_rate),
    'total_factor_productivity' : 0 if subset_total_factor_productivity == [] else  np.mean(subset_total_factor_productivity),
    'capital_stock' : 0 if subset_capital_stock == [] else  np.mean(subset_capital_stock),
    'hours_worked' : 0 if subset_hours_worked == [] else  np.mean(subset_hours_worked),
    'number_of_employed' : 0 if subset_number_of_employed == [] else  np.mean(subset_number_of_employed),
  })

  return reply

if __name__ == '__main__':
  
  df = pd.read_excel('output\\potential_growth_rate_by_half.xlsx', index_col=None, header=0)
  data = df.to_dict(orient='records')
  reply = convert(data)

  df = pd.DataFrame(reply)
  df.to_excel('output\\potential_growth_rate_by_annual.xlsx', index=False, header=True)