import yaml
from population_base import PopulationBase

# 設定を読み込む
with open('config.yaml', 'r') as yml:
  config = yaml.safe_load(yml)

# 人口データのフォーマットは不変のため定数として設定
MIN_AGE = 0
MAX_AGE = 86

class Population(PopulationBase):

  #########################################################################################
  # 設定系
  ######################################################################################### 
  # 既定値を読み込む
  def __init__(self):
    super().__init__()

  #########################################################################################
  # 参照系
  ######################################################################################### 
  # 対象暦年、開始年齢、終了年齢を受取、人口（千人）を返す。
  def _population(self, year: int, start: int, end: int) -> int:
    num = 0
    for age in range(start, end):
      num = num + self.getPopulation(year, age)
    return num
  
  # 対象暦年を受け取り、総人口、青年人口、労働人口、老年人口、学生人口を返す。
  def totalPopulation(self, year: int) -> int:
    return self._population(year, MIN_AGE, MAX_AGE)
  
  def adultPopulation(self, year: int) -> int:
    return self._population(year, self._minLabor(), MAX_AGE)

  def laborPopulation(self, year: int) -> int:
    return self._population(year, self._minLabor(), self._maxLabor())
  
  def seniorPopulation(self, year: int) -> int:
    return self._population(year, self._maxLabor(), MAX_AGE)
  
  def studentPopulation(self, year: int) -> int:
    return self._population(year, self._minStudent(), self._maxStudent())
  
  # 対象暦年を受け取り、総人口、青年人口、労働人口、老年人口、学生人口の対前年成長率を返す。
  def totalPopulationGrowthRatio(self, year: int) -> float:
    return self.totalPopulation(year) / self.totalPopulation(year - 1) - 1
  
  def adultPopulationGrowthRatio(self, year: int) -> float:
    return self.adultPopulation(year) / self.adultPopulation(year - 1) - 1
  
  def laborPopulationGrowthRatio(self, year: int) -> float:
    return self.laborPopulation(year) / self.laborPopulation(year - 1) - 1
  
  def seniorPopulationGrowthRatio(self, year: int) -> float:
    return self.seniorPopulation(year) / self.seniorPopulation(year - 1) - 1
  
  def studentPopulationGrowthRatio(self, year: int) -> float:
    return self.studentPopulation(year) / self.studentPopulation(year - 1) - 1

  #########################################################################################
  # 内部参照系（パラメータ）
  ######################################################################################### 
  # 労働人口レンジ、学習人口レンジを設定する。現在は定数を返すのみだが将来的には可変とする。
  def _minLabor(self) -> int:
    return config['population']['min_labor']
  
  def _maxLabor(self) -> int:
    return config['population']['max_labor']
  
  def _minStudent(self) -> int:
    return config['population']['min_student']
  
  def _maxStudent(self) -> int:
    return config['population']['max_student']
  