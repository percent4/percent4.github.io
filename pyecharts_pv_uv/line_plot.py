# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: line_plot.py
# @time: 2023/7/24 13:30
import pyecharts.options as opts
from pyecharts.charts import Line

now_date = "2023-07-24"
week_name_list = [now_date]
pv = [513]
uv = [92]
docs = [75]

Line(init_opts=opts.InitOpts(width="100%", height="500px"))\
    .add_xaxis(xaxis_data=week_name_list)\
    .add_yaxis(
    series_name="总访问量",
    y_axis=pv
)\
    .add_yaxis(
    series_name="总访客数",
    y_axis=uv
)\
    .add_yaxis(
    series_name="总文章数",
    y_axis=docs
)\
    .set_global_opts(
    title_opts=opts.TitleOpts(title="博客访问数据统计"),
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
)\
    .render(f"{now_date}.html")

print("图表已生成！请查收！")
