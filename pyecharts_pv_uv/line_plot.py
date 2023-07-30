# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: line_plot.py
# @time: 2023/7/24 13:30
import datetime
import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd

now_date = datetime.date.today()
print(now_date)

df = pd.read_csv('stats.csv', delimiter=',')
date_str_list = []
pv_list = []
uv_list = []
doc_num_list = []
for i in range(df.shape[0]):
    date_str, pv, uv, doc_num = df.iloc[i, :]
    date_str_list.append(str(date_str))
    pv_list.append(int(pv))
    uv_list.append(int(uv))
    doc_num_list.append(int(doc_num))

print(date_str_list, pv_list, uv_list, doc_num_list)
print('read stats data ...')

Line(init_opts=opts.InitOpts(width="100%", height="500px"))\
    .add_xaxis(xaxis_data=date_str_list)\
    .add_yaxis(
    series_name="总访问量",
    y_axis=pv_list
)\
    .add_yaxis(
    series_name="总访客数",
    y_axis=uv_list
)\
    .add_yaxis(
    series_name="总文章数",
    y_axis=doc_num_list
)\
    .set_global_opts(
    title_opts=opts.TitleOpts(title="博客访问数据统计"),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
)\
    .render(f"{now_date}.html")

print("图表已生成！请查收！")
