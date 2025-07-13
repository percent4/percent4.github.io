# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020/5/31 9:21 上午
# 绘制个人足迹地图：全国范围
import yaml
from pyecharts.charts import Map
from pyecharts import options as opts

# 省和直辖市
with open("/Users/admin/PycharmProjects/github_blog/source/personal_travel_map/travel_config.yml", 'r', encoding='utf-8') as ymlfile:
    province_city_dict = yaml.safe_load(ymlfile)

province_list = [(k, len(v)) for k, v in province_city_dict.items()]
print(province_list)

china_map = (
    Map(init_opts=opts.InitOpts(chart_id='123', width='1200px', height='800px'))
    .add(
        series_name="足迹省份",
        data_pair=province_list,
        maptype="china",
        is_map_symbol_show=False,
        label_opts=opts.LabelOpts(is_show=True)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="个人足迹地图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=20,
            is_piecewise=True
        ),
    )
    .render("/Users/admin/PycharmProjects/github_blog/source/personal_travel_map/china.html")
)
