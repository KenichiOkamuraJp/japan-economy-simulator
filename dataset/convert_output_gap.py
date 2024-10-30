import pandas as pd
import numpy as np
import math

def convert(data: list) -> list:
  reply = []
  subset_output_gap = []
  subset_capital_input_gap = []
  subset_labor_input_gap = []
  subset_tankan_factor_utilization_index1 = []
  subset_tankan_factor_utilization_index2 = []
  pre_year = data[0]['year']

  for record in data:
    if pre_year != record['year']:
      reply.append({
        'year' : pre_year,
        'output_gap' : 0 if subset_output_gap == [] else np.mean(subset_output_gap),
        'capital_input_gap' : 0 if subset_capital_input_gap == [] else  np.mean(subset_capital_input_gap),
        'labor_input_gap' : 0 if subset_labor_input_gap == [] else  np.mean(subset_labor_input_gap),
        'tankan_factor_utilization_index1' : 0 if subset_tankan_factor_utilization_index1 == [] else  np.mean(subset_tankan_factor_utilization_index1),
        'tankan_factor_utilization_index2' : 0 if subset_tankan_factor_utilization_index2 == [] else  np.mean(subset_tankan_factor_utilization_index2),
      })
      subset_output_gap.clear()
      subset_capital_input_gap.clear()
      subset_labor_input_gap.clear()
      subset_tankan_factor_utilization_index1.clear()
      subset_tankan_factor_utilization_index2.clear()
      pre_year = record['year']

    if not math.isnan(record['output_gap']):
      subset_output_gap.append(record['output_gap'])
    if not math.isnan(record['capital_input_gap']):
      subset_capital_input_gap.append(record['capital_input_gap'])
    if not math.isnan(record['labor_input_gap']):
      subset_labor_input_gap.append(record['labor_input_gap'])    
    if not math.isnan(record['tankan_factor_utilization_index1']):
      subset_tankan_factor_utilization_index1.append(record['tankan_factor_utilization_index1'])
    if not math.isnan(record['tankan_factor_utilization_index2']):
      subset_tankan_factor_utilization_index2.append(record['tankan_factor_utilization_index2'])

  reply.append({
    'year' : pre_year,
    'output_gap' : 0 if subset_output_gap == [] else np.mean(subset_output_gap),
    'capital_input_gap' : 0 if subset_capital_input_gap == [] else  np.mean(subset_capital_input_gap),
    'labor_input_gap' : 0 if subset_labor_input_gap == [] else  np.mean(subset_labor_input_gap),
    'tankan_factor_utilization_index1' : 0 if subset_tankan_factor_utilization_index1 == [] else  np.mean(subset_tankan_factor_utilization_index1),
    'tankan_factor_utilization_index2' : 0 if subset_tankan_factor_utilization_index2 == [] else  np.mean(subset_tankan_factor_utilization_index2),
  })

  return reply

if __name__ == '__main__':
  
  df = pd.read_excel('output\\output_gap_by_quarter.xlsx', index_col=None, header=0)
  data = df.to_dict(orient='records')
  reply = convert(data)

  df = pd.DataFrame(reply)
  df.to_excel('output\\output_gap_by_annual.xlsx', index=False, header=True)