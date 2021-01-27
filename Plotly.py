#!/usr/bin/env python
# coding: utf-8

import pandas as pd


ds = pd.read_csv("C:\gayatri\Datasets\cit-Patents_deg.csv",header=None)


ds.rename(columns={0:'col1'},inplace = True)
ds.rename(columns={1:'col2'},inplace = True)


import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.express as px
import numpy as np
from plotly.figure_factory import create_table


table = create_table(ds.head(10))
py.iplot(table)


px.bar(ds.head(50), x='col1', y='col2',height= 600)


px.scatter(ds.head(50), x='col1', y='col2',color='col1')


px.scatter(ds.head(50),x='col1',y='col2',color='col1',size='col2',size_max=40,hover_name='col1')


px.line(ds.head(50),x='col1',y='col2',color='col1',line_group='col1',line_shape='spline',render_mode='svg')


px.line(ds.head(50),x='col1',y='col2',color='col1',line_group='col2',line_shape='spline',render_mode='svg')


px.line(ds.head(50),x='col1',y='col2',color='col2',line_group='col2',line_shape='spline',render_mode='svg')


px.area(ds.head(50),x='col1',y='col2',color='col1',line_group='col1')


px.area(ds.head(50),x='col1',y='col2',color='col1',line_group='col2')





