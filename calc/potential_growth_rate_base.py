import yaml
from fact_data import FactData

with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)

class PotentialGrowthRateBase(FactData):

  #########################################################################################
  # 設定系
  ######################################################################################### 
  def __init__(self):
    super().__init__(config['fact_data']['potential_growth_rate'])

  #########################################################################################
  # 参照系
  #########################################################################################  
  # 暦年を受け取り、該当年の潜在成長率を返す
  def getPotentialGrowthRate(self, year: int) -> float:
    return self.fact_data[str(year)]['potential_growth_rate']
  
  # 暦年を受け取り、該当年の全要素生産性成長率を返す
  def getTotalFactorProductivity(self, year: int) -> float:
    return self.fact_data[str(year)]['total_factor_productivity']
  
  # 暦年を受け取り、該当年の資本ストック成長率を返す
  def getCapitalStock(self, year: int) -> float:
    return self.fact_data[str(year)]['capital_stock']
  
  # 暦年を受け取り、該当年の労働時間成長率を返す
  def getHoursWorked(self, year: int) -> float:
    return self.fact_data[str(year)]['hours_worked']
  
  # 暦年を受け取り、該当年の就業者数成長率を返す
  def getNumberOfEmployed(self, year: int) -> float:
    return self.fact_data[str(year)]['number_of_employed']
