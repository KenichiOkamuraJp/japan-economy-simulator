import yaml
from potential_growth_rate_base import PotentialGrowthRateBase
from population import Population

# 設定を読み込む
with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)

class PotentialGrowthRate(PotentialGrowthRateBase):

  #########################################################################################
  # 設定系
  ######################################################################################### 
  # 既定値を読み込む
  def __init__(self):
    super().__init__()
    self.calc_data = {}

  #########################################################################################
  # 参照系
  #########################################################################################  
  # 当該データが存在するかどうかを、読み込みデータ、計算データの双方で確かめる
  def exist(self, year) -> bool:
    if super().factdata_exist(year):
      return True
    elif str(year) in self.calc_data.keys():
      return True
    else:
      return False
    
  # 暦年を受け取り、潜在成長率を返す
  def getPotentialGrowthRate(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getPotentialGrowthRate(year)
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['potential_growth_rate']
    else:
      raise
    
  # 暦年を受け取り、全要素生産性成長率を返す
  def getTotalFactorProductivity(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getTotalFactorProductivity(year)
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['total_factor_productivity']
    else:
      raise

  # 暦年を受け取り、資本ストック成長率を返す
  def getCapitalStock(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getCapitalStock(year)
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['capital_stock']
    else:
      raise

  # 暦年を受け取り、労働時間成長率を返す
  def getHoursWorked(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getHoursWorked(year)
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['hours_worked']
    else:
      raise

  # 暦年を受け取り、労働参加率増加率を返す
  def getParticipateRate(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getNumberOfEmployed(year) - self.pop.laborPopulationGrowthRatio(year) * 100
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['participate_rate']
    else:
      raise

  # 暦年を受け取り、就業者数成長率を返す
  def getNumberOfEmployed(self, year: int) -> float:
    if super().factdata_exist(year):
      return super().getNumberOfEmployed(year)
    elif str(year) in self.calc_data.keys():
      return self.calc_data[str(year)]['number_of_employed']
    else:
      raise

  #########################################################################################
  # 処理系
  ######################################################################################### 
  # 計算の前提となるパラメーターを設定する
  def setParameter(self, pop: Population):
    self.pop = pop

  # 暦年を指定し、その年のデータを作成する
  def execute(self, year) -> bool:
    # 既に当該年のデータが存在する場合、エラーを返す
    if self.exist(year):
      print(str(year) + ' is already exist.')
      return False
    
    # 前年のデータが存在しない場合、前年のデータを先に作成する
    if not self.exist(year - 1):
      print('Prior to ' + str(year) + ' is not exist. Will generate it.')
      self.execute(year - 1)

    # 全要素生産性、資本ストック、労働時間、労働参加率、就業者の各成長率を算出する。
    totalFactorProductivity = self.makeTotalFactorProductivity(year)
    capitalStock = self.makeCapitalStock(year)
    hoursWorked = self.makeHoursWorked(year)
    participateRate = self.makePaticipateRate(year)
    NumberOfEmployed = self.makeNumberOfEmployed(year, participateRate)

    # 潜在成長力を算出する。
    potentialGrowthRate = totalFactorProductivity + capitalStock + hoursWorked + NumberOfEmployed

    # calc_dataに格納する。
    self.calc_data[str(year)] = {
      'year' : year,
      'potential_growth_rate' : potentialGrowthRate,
      'total_factor_productivity' : totalFactorProductivity,
      'capital_stock' : capitalStock,
      'hours_worked' : hoursWorked,
      'participate_rate' : participateRate,
      'number_of_employed' : NumberOfEmployed,
      'calc_data' : 1
    }

    return True

  # 全要素生産性成長率を求める
  def makeTotalFactorProductivity(self, year: int) -> float:
    if year == self._tfpStartYear():
      return self._tfpStartValue()
    else:
      return self.getTotalFactorProductivity(year - 1) * self._tfpDelta()
    
  # 資本ストック成長率を求める
  def makeCapitalStock(self, year: int) -> float:
    if year == self._capitalStockStartYear():
      return self._capitalStockStartValue()
    else:
      return self.getCapitalStock(year - 1) * self._capitalStockDelta()
    
  # 労働時間成長率を求める
  def makeHoursWorked(self, year: int) -> float:
    if year == self._hoursWorkedStartYear():
      return self._hoursWorkedStartValue()
    else:
      return self.getHoursWorked(year - 1) * self._hoursWorkedDelta()

  # 就業者成長率を求める
  def makePaticipateRate(self, year: int) -> float:
    return self.getParticipateRate(year - 1) * self._participateDelta()

  # 就業者成長率を求める
  def makeNumberOfEmployed(self, year: int, participateRate: float) -> float:
    return self.pop.laborPopulationGrowthRatio(year) * 100 + participateRate
  
  #########################################################################################
  # 内部参照系（処理用パラメータ）
  ######################################################################################### 
  # 全要素生産性、資本ストック、労働時間の初期値設定時期、初期値、増分、労働参加率の増分を設定する
  def _tfpStartYear(self) -> int:
    return config['potential_growth_rate']['tfp']['start_year']
  
  def _tfpStartValue(self) -> int:
    return config['potential_growth_rate']['tfp']['start_value']
  
  def _tfpDelta(self) -> int:
    return config['potential_growth_rate']['tfp']['delta']
  
  def _capitalStockStartYear(self) -> int:
    return config['potential_growth_rate']['capital_stock']['start_year']
  
  def _capitalStockStartValue(self) -> int:
    return config['potential_growth_rate']['capital_stock']['start_value']
  
  def _capitalStockDelta(self) -> int:
    return config['potential_growth_rate']['capital_stock']['delta']
  
  def _hoursWorkedStartYear(self) -> int:
    return config['potential_growth_rate']['hours_worked']['start_year']
  
  def _hoursWorkedStartValue(self) -> int:
    return config['potential_growth_rate']['hours_worked']['start_value']
  
  def _hoursWorkedDelta(self) -> int:
    return config['potential_growth_rate']['hours_worked']['delta']

  def _participateDelta(self) -> int:
    return config['potential_growth_rate']['participate']['delta']

  #########################################################################################
  # 出力系
  #########################################################################################
  def output(self) -> list:
    # fact_dataとcalc_dataを統合する
    integrated_data = super().output()
    for year in self.calc_data.keys():
      integrated_data[year] = self.calc_data[year]
    
    # 統合されたデータをリスト型に整形
    reply = []
    for year in integrated_data.keys():
      reply.append(integrated_data[year])
    return reply