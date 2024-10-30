import yaml
from fact_data import FactData

with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)

class PopulationBase(FactData):

  #########################################################################################
  # 設定系
  ######################################################################################### 
  def __init__(self):
    super().__init__(config['fact_data']['population'])

  #########################################################################################
  # 参照系
  ######################################################################################### 
  # 暦年を受け取り、該当年の年齢別人口（千人単位）のDictを返す
  def getYearData(self, year: int) -> dict:
    return self.fact_data[str(year)]

  # 暦年と年齢を受け取り、人口（千人単位）を返す
  def getPopulation(self, year: int, age: int) -> int:
    return self.fact_data[str(year)][str(age)]
