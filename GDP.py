from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

f=open("E:\GDP.txt","r",encoding="UTF-8")
data_lines = f.readlines()
f.close()
data_lines.pop(0)  #删除第一条数据

timeline = Timeline(
    {"How GDP changed from 1960 to 2024":ThemeType.LIGHT}
)
#自动播放设置
timeline.add_schema(
    play_interval=100,#单位是毫秒,1000ms = 1s
    is_timeline_show=True,
    is_auto_play=False,
    is_loop_play=False
)

#将数据转换为字典存储:{year1:[[country1,GDP],[country2,GDP],...], year2:[[country1,GDP],[country2,GDP]]}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    GDP = float(line.split(",")[2])

    try:
        data_dict[year].append([country,GDP])
    except Exception:
        data_dict[year] = []
        data_dict[year].append([country, GDP])

sort_year_list = sorted(data_dict.keys())#拿到字典所有的key并以此为依据进行排序
for year in sort_year_list:
    data_dict[year].sort(key=lambda element: element[1],reverse = False)
    data_year = data_dict[year][:10]  #取当年GDP前十的国家

    x = []
    y = []
    for country_GDP in data_year:
        x.append(country_GDP[0])
        y.append(country_GDP[1])

    bar = Bar()
    bar.add_yaxis("GDP(亿)",y,label_opts=LabelOpts(position="right"))
    bar.add_xaxis(x)
    bar.reversal_axis()

    timeline.add(bar, f"GDP {year}")
    timeline.render()