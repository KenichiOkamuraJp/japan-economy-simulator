import requests

def _do(url, filename):
  urlData = requests.get(url).content

  with open(filename ,mode='wb') as f:
    f.write(urlData)

if __name__ == '__main__':

  ############################################################################################
  # 人口
  ############################################################################################
  # 人口推計（表１　出生中位（死亡中位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_1.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/1-9.xlsx'
  filename='row_data/population/1-9.xlsx'
  _do(url, filename)

  # 人口推計（表２　出生高位（死亡中位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_2.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/2-9.xlsx'
  filename='row_data/population/2-9.xlsx'
  _do(url, filename)

  # 人口推計（表３　出生低位（死亡中位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_3.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/3-9.xlsx'
  filename='row_data/population/3-9.xlsx'
  _do(url, filename)

  # 人口推計（表４　出生中位（死亡高位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_4.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/4-9.xlsx'
  filename='row_data/population/4-9.xlsx'
  _do(url, filename)

  # 人口推計（表５　出生高位（死亡高位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_5.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/5-9.xlsx'
  filename='row_data/population/5-9.xlsx'
  _do(url, filename)

  # 人口推計（表６　出生低位（死亡高位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_6.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/6-9.xlsx'
  filename='row_data/population/6-9.xlsx'
  _do(url, filename)

  # 人口推計（表７　出生中位（死亡低位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_7.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/7-9.xlsx'
  filename='row_data/population/7-9.xlsx'
  _do(url, filename)

  # 人口推計（表８　出生高位（死亡低位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_8.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/8-9.xlsx'
  filename='row_data/population/8-9.xlsx'
  _do(url, filename)

  # 人口推計（表９　出生低位（死亡低位）推計 （2021～2070年））
  # https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/db_r5_suikeikekka_9.html
  url='https://www.ipss.go.jp/pp-zenkoku/j/zenkoku2023/db_zenkoku2023/s_tables/9-9.xlsx'
  filename='row_data/population/9-9.xlsx'
  _do(url, filename)

  # 我が国の推計人口（大正9年～平成12年）
  # https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200524&tstat=000000090001&cycle=0&tclass1=000000090004&tclass2=000000090005&tclass3val=0
  url='https://www.e-stat.go.jp/stat-search/file-download?statInfId=000000090264&fileKind=0'
  filename='row_data/population/actual1920-2000.xlsx'
  _do(url, filename)

  # 我が国の推計人口（大正9年～平成12年）
  # https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00200524&tstat=000000090001&cycle=0&tclass1=000000090004&tclass2=000001051180&tclass3val=0
  url='https://www.e-stat.go.jp/stat-search/file-download?statInfId=000013168604&fileKind=4'
  filename='row_data/population/actual2000-2020.xlsx'
  _do(url, filename)

  ############################################################################################
  # 需給ギャップと潜在成長率
  ############################################################################################
  # https://www.boj.or.jp/research/research_data/gap/index.htm
  url='https://www.boj.or.jp/research/research_data/gap/gap.xlsx'
  filename='row_data/og_and_pgr/og_and_pgr.xlsx'
  _do(url, filename)

  ############################################################################################
  # 金利
  ############################################################################################
  # 過去の金利情報（昭和49年（1974年）～）
  # https://www.mof.go.jp/jgbs/reference/interest_rate/index.htm
  url='https://www.mof.go.jp/jgbs/reference/interest_rate/data/jgbcm_all.csv'
  filename='row_data/bond/jgbcm_all.csv'
  _do(url, filename)

  ############################################################################################
  # 予算  
  ############################################################################################
  # 令和５年度予算政府案
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2023/seifuan2023/index.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2023/seifuan2023/01.pdf'
  filename='row_data/budget/fy2023-honyosan.pdf'
  _do(url, filename)
  # 令和５年度補正予算
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2023/20231110071409.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2023/hosei231110a.pdf'
  filename='row_data/budget/fy2023-hosei.pdf'
  _do(url, filename)

  # 令和４年度予算政府案
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/seifuan2022/index.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/seifuan2022/01.pdf'
  filename='row_data/budget/fy2022-honyosan.pdf'
  _do(url, filename)
  # 令和４年度補正予算（第１号）
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/hosei0517.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/hosei0517a.pdf'
  filename='row_data/budget/fy2022-hosei01.pdf'
  _do(url, filename)
  # 令和４年度補正予算（第２号）
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/20221108033406.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2022/hosei221108a.pdf'
  filename='row_data/budget/fy2022-hosei02.pdf'
  _do(url, filename)

  # 令和３年度予算政府案
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2021/seifuan2021/index.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2021/seifuan2021/01.pdf'
  filename='row_data/budget/fy2021-honyosan.pdf'
  _do(url, filename)
  # 令和３年度補正予算
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2021/20211125201916.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2021/hosei211126a.pdf'
  filename='row_data/budget/fy2021-hosei.pdf'
  _do(url, filename)

  # 令和２年度予算政府案
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/seifuan2019/index.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/seifuan2019/01.pdf'
  filename='row_data/budget/fy2020-honyosan.pdf'
  _do(url, filename)
  # 令和２年度補正予算（第１号）
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/hosei0420.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/sy020407/hosei020420.pdf'
  filename='row_data/budget/fy2020-hosei01.pdf'
  _do(url, filename)
  # 令和２年度補正予算（第２号）
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/hosei0527.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/sy020407/hosei020527.pdf'
  filename='row_data/budget/fy2020-hosei02.pdf'
  _do(url, filename)
  # 令和２年度補正予算（第３号）
  # https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/hosei1215.html
  url='https://www.mof.go.jp/policy/budget/budger_workflow/budget/fy2020/hosei021215.pdf'
  filename='row_data/budget/fy2020-hosei03.pdf'
  _do(url, filename)

  # 令和元年度予算政府案
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12213409/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2019/seifuan31/index.html
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12213409/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2019/seifuan31/01.pdf'
  filename='row_data/budget/fy2019-honyosan.pdf'
  _do(url, filename)
  # 令和元年度補正予算
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12213409/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2019/hosei1213.html
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12213409/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2019/sy011213/hosei011213.pdf'
  filename='row_data/budget/fy2019-hosei.pdf'
  _do(url, filename)

  # 平成30年度予算政府案
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/seifuan30/index.htm
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/seifuan30/01.pdf'
  filename='row_data/budget/fy2018-honyosan.pdf'
  _do(url, filename)
  # 平成30年度補正予算（第１号）
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/hosei1015.html
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/sy301015/sy301015.pdf'
  filename='row_data/budget/fy2018-hosei01.pdf'
  _do(url, filename)
  # 平成30年度補正予算（第２号）
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/hosei301221.html
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2018/sy301015/hosei301221.pdf'
  filename='row_data/budget/fy2018-hosei02.pdf'
  _do(url, filename)

  # 平成29年度予算政府案
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2017/seifuan29/index.htm
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2017/seifuan29/01.pdf'
  filename='row_data/budget/fy2017-honyosan.pdf'
  _do(url, filename)
  # 平成29年度補正予算
  # https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2017/hosei1222.htm
  url='https://warp.da.ndl.go.jp/info:ndljp/pid/12069570/www.mof.go.jp/policy/budget/budger_workflow/budget/fy2017/sy291220/hosei291222a.pdf'
  filename='row_data/budget/fy2017-hosei01.pdf'
  _do(url, filename)

  # 平成28年度予算政府案
  # https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/seifuan28/index.html
  url='https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/seifuan28/01.pdf'
  filename='row_data/budget/fy2016-honyosan.pdf'
  _do(url, filename)
  # 平成28年度補正予算（第１号）
  # https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/hosei280513.html
  url='https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/sy280513/hosei280513a.pdf'
  filename='row_data/budget/fy2016-hosei01.pdf'
  _do(url, filename)
  # 平成28年度補正予算（第２号）
  # https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/hosei0824.html
  url='https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/sy280513/hosei280824a.pdf'
  filename='row_data/budget/fy2016-hosei02.pdf'
  _do(url, filename)
  # 平成28年度補正予算（第３号）
  # https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/hosei1222.html
  url='https://warp.ndl.go.jp/info:ndljp/pid/11400594/www.mof.go.jp/budget/budger_workflow/budget/fy2016/sy280513/hosei281222a.pdf'
  filename='row_data/budget/fy2016-hosei03.pdf'
  _do(url, filename)

  ############################################################################################
  # 国債
  ############################################################################################
  # 政府債務合計
  # https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000&lstSelection=PF02
  url='https://www.stat-search.boj.or.jp/ssi/html/nme_R031.2833.20240123135302.01.csv'
  filename='row_data/bond/bond.csv'
  _do(url, filename)

  # 普通国債残高の満期構成（令和5年9月末）
  # https://www.mof.go.jp/jgbs/reference/appendix/index.htm
  url='https://www.mof.go.jp/jgbs/reference/appendix/maturity.pdf'
  filename='row_data/bond/maturity.pdf'
  _do(url, filename)