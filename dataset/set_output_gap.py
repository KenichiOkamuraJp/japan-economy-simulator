import openpyxl
import pandas as pd
import yaml

with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)
ORIGINAL = config['output_gap_and_potential_growth_rate']['original']

if __name__ == '__main__':
  filename = ORIGINAL
  workbook = openpyxl.load_workbook(filename)

  # 需給ギャップのデータを読み出す
  data_excel = pd.DataFrame(workbook['Chart']["A6":"F9999"]).values.tolist()
  
  data_by_quarter = []
  for record in data_excel:
    quarterly = record[0].value
    # A列（年度・四半期）が空欄の場合スキップする
    if quarterly is None:
      continue
    year = int(quarterly.split('.')[0])
    quarter = quarterly.split('.')[1]
    if quarter == '1Q':
      month = '4-6'
    elif quarter == '2Q':
      month = '7-9'
    elif quarter == '3Q':
      month = '10-12'
    elif quarter == '4Q':
      month = '1-3'
      year = year + 1

    data_by_quarter.append({
      'quarterly' : record[0].value, 
      'year' : year,
      'month' : month,
      'output_gap' : record[1].value,
      'capital_input_gap' : record[2].value,
      'labor_input_gap' : record[3].value, 
      'tankan_factor_utilization_index1' : record[4].value,
      'tankan_factor_utilization_index2' : record[5].value
    })

  df = pd.DataFrame(data_by_quarter)
  df.to_excel('output\\output_gap_by_quarter.xlsx', index=False, header=True)
 