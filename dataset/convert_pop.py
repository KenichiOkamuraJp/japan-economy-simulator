import pandas as pd

def convert(data: list):

  reply = []
  subtotal = 0
  pre_year = data[0]['year']
  pre_type = data[0]['data_type']

  for record in data:
    age = int(record['age'].replace('+', ''))

    if record['year'] != pre_year:
      reply.append({
        'data_type' : pre_type,
        'year' : pre_year,
        'age' : 85,
        'total'  : subtotal,
      })
      pre_year = record['year']
      subtotal = 0

    if age >= 85:
      subtotal = subtotal + record['total']
    else:
      reply.append({
        'data_type' : record['data_type'],
        'year' : record['year'],
        'age' : age,
        'total'  : record['total'],
      })

    pre_type = record['data_type']

  reply.append({
    'data_type' : pre_type,
    'year' : pre_year,
    'age' : 85,
    'total'  : subtotal,
  })

  return reply

def matrix(data: list):
  matrix_data = {}
  for row in data:
    data_type = row['data_type']
    year = str(row['year'])
    age = str(row['age'])
    
    if data_type == '予測-死亡中位-出生中位' or data_type == 'history':
      if not year in matrix_data.keys():
        matrix_data[year] = { age : row['total']}
      else:
        matrix_data[year][age] = row['total']

  reply = []
  for year in matrix_data.keys():
    row_data = matrix_data[year]
    aRow = {'year': year}
    for age in row_data.keys():
      value = row_data[age]
      aRow[age] = value
    reply.append(aRow)

  return reply

if __name__ == '__main__':
  
  df = pd.read_excel('output\\population_master.xlsx', index_col=None, header=0)
  data = df.to_dict(orient='records')
  reply = convert(data)
  #df = pd.DataFrame(reply)
  #df.to_excel('output\\population_converted.xlsx', index=False, header=True)
  reply = matrix(reply)
  df = pd.DataFrame(reply)
  df.to_excel('output\\population_matrix.xlsx', index=False, header=True)
