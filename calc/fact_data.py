import pandas as pd

class FactData:

  #########################################################################################
  # 設定系
  ######################################################################################### 
  def __init__(self, filename: str):

    # 固定データを読み込む
    records = self._loadFromData(filename)
    
    # 暦年をKeyにデータをセット
    self.fact_data = {}
    for record in records:
      year = record['year']
      self.fact_data[str(year)] = record

  # 固定データの読み込み
  def _loadFromData(self, filename: str) -> list:
    # ファイルからの読み込み
    df = pd.read_excel(filename, index_col=None, header=0)
    return df.to_dict(orient='records')

  #########################################################################################
  # 参照系
  #########################################################################################    
  # 暦年を受け取り、その年のレコードが存在するかを返す
  def factdata_exist(self, year: int) -> bool:
    return str(year) in self.fact_data.keys()

  #########################################################################################
  # 出力系
  ######################################################################################### 
  def output(self) -> dict:
    return self.fact_data
