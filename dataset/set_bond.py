import pandas as pd
import yaml
import datetime
import numpy as np
import operator

with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)
INTEREST  = config['bond']['interest']
STRUCTURE = config['bond']['structure']

def wareki_parser(aDate: str):
  wareki = {
    "R":2018,
    "H":1988,
    'S':1925
  }
  loc = aDate.find('.')
  if loc == 3:
    aDate = str(int(aDate[1:3])+wareki[aDate[0]])+aDate[3:9]
  else:
    aDate = str(int(aDate[1:2])+wareki[aDate[0]])+aDate[2:9]
  dt = datetime.datetime.strptime(aDate, '%Y.%m.%d')
  return dt

def nendo_parser(aDate):
  year = aDate.year
  month = aDate.month
  if month < 4:
    year = year - 1
  return year

def set_interest():
  df = pd.read_csv(INTEREST, header=0, index_col=False, skiprows=1, encoding='sjis')
  df['基準日-西暦'] = df['基準日'].apply(wareki_parser)
  df['年度'] = df['基準日-西暦'].apply(nendo_parser)
  df.set_index('基準日-西暦', inplace=True)
  df.replace('-', np.nan, inplace=True)
  df = df.astype({
    '1年': 'float64', 
    '2年': 'float64', 
    '3年': 'float64', 
    '4年': 'float64', 
    '5年': 'float64', 
    '6年': 'float64', 
    '7年': 'float64', 
    '8年': 'float64', 
    '9年': 'float64', 
    '10年': 'float64', 
    '15年': 'float64', 
    '20年': 'float64', 
    '25年': 'float64',
    '30年': 'float64',
    '40年': 'float64'
  }) 
  df_nendo = df.groupby(df['年度']).mean(numeric_only=True)
  # df_year  = df.resample('Y').mean(numeric_only=True)
  df_nendo.to_excel('output\\interest_by_nendo.xlsx', index=True, header=True)

def set_history():
  df = pd.read_excel(STRUCTURE, header=0, index_col=False)
  records = df.to_dict(orient='records')

  # 満期年ごとの債権構成から、発行年ごとの債券構成に変換
  work = []
  for row in records:
    year = row['FY']
    year1 = row['1year']
    year2 = row['2years']
    year5 = row['5years']
    year10 = row['10years']
    year20 = row['20years']
    year30 = row['30years']
    year40 = row['40years']
    work.append({
      str(year-1): {'value': year1, 'type': '1year'},
      str(year-2): {'value': year2, 'type': '2years'},
      str(year-5): {'value': year5, 'type': '5years'},
      str(year-10): {'value': year10, 'type': '10years'},
      str(year-20): {'value': year20, 'type': '20years'},
      str(year-30): {'value': year30, 'type': '30years'},
      str(year-40): {'value': year40, 'type': '40years'},
    })

  # 発行年ごとの債券構成を集約
  history = {}
  for row in work:
    for col in row.keys():
      value = row[col]['value']
      bond_type = row[col]['type']
      key = col + '@' + bond_type
      if not key in history.keys():
        history[key] = value
      else:
        history[key] = history[key] + value

  # 発行年ごとの債券構成を構造化
  result = {}
  for rec in history.keys():
    loc = rec.find('@')
    year = rec[:loc]
    bond_type = rec[loc+1:]
    value = history[rec]
    if value == 0:
      continue
    if not year in result.keys():
      result[year] = {bond_type: value}
    else:
      if not bond_type in result[year].keys():
        result[year][bond_type] = value
      else:
        result[year][bond_type] = result[year][bond_type] + value

  final = []
  for rec in result.keys():
    dat = result[rec]
    val = {'year': rec}
    for lab in dat.keys():
      val[lab] = dat[lab]
    final.append(val)
  
  final = sorted(final, key=operator.itemgetter('year'))
  
  final_df = pd.DataFrame(final)
  final_df.to_excel('output\\bond_by_issueyear.xlsx', index=True, header=True)

if __name__ == '__main__':
  set_interest()
  set_history()