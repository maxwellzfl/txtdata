import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:r &sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
print("total reponsitories:",response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned:',len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\n keys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
names, stars=[], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 60
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred python projects on Github'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('python_repos.svg')