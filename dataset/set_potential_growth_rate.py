import openpyxl
import pandas as pd
import yaml

with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)
ORIGINAL = config['output_gap_and_potential_growth_rate']['original']

if __name__ == '__main__':
  filename = ORIGINAL
  workbook = openpyxl.load_workbook(filename)

  # 潜在成長力のデータを読み出す
  data_excel = pd.DataFrame(workbook['Chart']["H6":"M9999"]).values.tolist()
  
  data_by_half = []
  for record in data_excel:
    period = record[0].value
    # A列（年度・四半期）が空欄の場合スキップする
    if period is None:
      continue
    wkPeriod = period.split(':')[0]
    year = int(wkPeriod.split('.')[0])
    half = int(wkPeriod.split('.')[1].strip())

    if half == 1:
      month = '7-12'
    elif half == 2:
      month = '1-6'
      year = year + 1
    else:
      print('period : ' + period)
      raise

    data_by_half.append({
      'semi_annual' : record[0].value, 
      'year' : year,
      'month' : month,
      'potential_growth_rate' : record[1].value,
      'total_factor_productivity' : record[2].value,
      'capital_stock' : record[3].value,
      'hours_worked' : record[4].value,
      'number_of_employed' : record[5].value,
    })

  df = pd.DataFrame(data_by_half)
  df.to_excel('output\\potential_growth_rate_by_half.xlsx', index=False, header=True)
 