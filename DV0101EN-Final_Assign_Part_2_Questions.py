{\rtf1\ansi\ansicpg950\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red89\green138\blue67;\red23\green23\blue23;\red202\green202\blue202;
\red183\green111\blue179;\red194\green126\blue101;\red70\green137\blue204;\red140\green211\blue254;\red212\green214\blue154;
\red167\green197\blue152;}
{\*\expandedcolortbl;;\cssrgb\c41569\c60000\c33333;\cssrgb\c11765\c11765\c11765;\cssrgb\c83137\c83137\c83137;
\cssrgb\c77255\c52549\c75294;\cssrgb\c80784\c56863\c47059;\cssrgb\c33725\c61176\c83922;\cssrgb\c61176\c86275\c99608;\cssrgb\c86275\c86275\c66667;
\cssrgb\c70980\c80784\c65882;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh16580\viewkind0
\deftab720
\pard\pardeftab720\sl360\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #!/usr/bin/env python\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # coding: utf-8\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # In[ ]:\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\sl360\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  dash\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  dash \cf5 \strokec5 import\cf4 \strokec4  dcc\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  dash \cf5 \strokec5 import\cf4 \strokec4  html\cb1 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  dash.dependencies \cf5 \strokec5 import\cf4 \strokec4  Input, Output\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  pandas \cf5 \strokec5 as\cf4 \strokec4  pd\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  plotly.graph_objs \cf5 \strokec5 as\cf4 \strokec4  go\cb1 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  plotly.express \cf5 \strokec5 as\cf4 \strokec4  px\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Load the data using pandas\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 data = pd.read_csv(\cf6 \strokec6 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data\cf7 \strokec7 %20F\cf6 \strokec6 iles/historical_automobile_sales.csv'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Initialize the Dash app\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 app = dash.Dash(\cf8 \strokec8 __name__\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Set the title of the dashboard\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #app.title = "Automobile Statistics Dashboard"\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 #---------------------------------------------------------------------------------\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Create the dropdown menu options\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 dropdown_options = [\cb1 \
\cb3     \{\cf6 \strokec6 'label'\cf4 \strokec4 : \cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 , \cf6 \strokec6 'value'\cf4 \strokec4 : \cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 'label'\cf4 \strokec4 : \cf6 \strokec6 'Recession Period Statistics'\cf4 \strokec4 , \cf6 \strokec6 'value'\cf4 \strokec4 : \cf6 \strokec6 'Recession Period Statistics'\cf4 \strokec4 \}\cb1 \
\cb3 ]\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # List of years \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 year_list = [i \cf5 \strokec5 for\cf4 \strokec4  i \cf5 \strokec5 in\cf4 \strokec4  \cf9 \strokec9 range\cf4 \strokec4 (\cf10 \strokec10 1980\cf4 \strokec4 , \cf10 \strokec10 2024\cf4 \strokec4 , \cf10 \strokec10 1\cf4 \strokec4 )]\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #---------------------------------------------------------------------------------------\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Create the layout of the app\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3 app.layout = html.Div([\cb1 \
\cb3     \cf2 \strokec2 #TASK 2.1 Add title to the dashboard\cf4 \cb1 \strokec4 \
\cb3     html.H1(\cf6 \strokec6 "Automobile Sales Statistics Dashboard"\cf4 \strokec4 ),\cf2 \strokec2 #May include style for title\cf4 \cb1 \strokec4 \
\cb3     html.Div([\cf2 \strokec2 #TASK 2.2: Add two dropdown menus\cf4 \cb1 \strokec4 \
\cb3         html.Label(\cf6 \strokec6 "Select Statistics:"\cf4 \strokec4 ),\cb1 \
\cb3         dcc.Dropdown(\cb1 \
\cb3             \cf8 \strokec8 id\cf4 \strokec4 =\cf6 \strokec6 'dropdown-statistics'\cf4 \strokec4 ,\cb1 \
\cb3             \cf8 \strokec8 options\cf4 \strokec4 =[\cb1 \
\cb3                            \{\cf6 \strokec6 'label'\cf4 \strokec4 : \cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 , \cf6 \strokec6 'value'\cf4 \strokec4 : \cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 \},\cb1 \
\cb3                            \{\cf6 \strokec6 'label'\cf4 \strokec4 : \cf6 \strokec6 'Recession Period Statistics'\cf4 \strokec4 , \cf6 \strokec6 'value'\cf4 \strokec4 : \cf6 \strokec6 'Recession Period Statistics'\cf4 \strokec4 \}\cb1 \
\cb3                            ],\cb1 \
\cb3             \cf8 \strokec8 value\cf4 \strokec4 =\cf6 \strokec6 'Select Statistics'\cf4 \strokec4 ,\cb1 \
\cb3             \cf8 \strokec8 placeholder\cf4 \strokec4 =\cf6 \strokec6 'Select a report'\cf4 \cb1 \strokec4 \
\cb3         )\cb1 \
\cb3     ]),\cb1 \
\cb3     html.Div(dcc.Dropdown(\cb1 \
\cb3             \cf8 \strokec8 id\cf4 \strokec4 =\cf6 \strokec6 'select-year'\cf4 \strokec4 ,\cb1 \
\cb3             \cf8 \strokec8 options\cf4 \strokec4 =[\{\cf6 \strokec6 'label'\cf4 \strokec4 : i, \cf6 \strokec6 'value'\cf4 \strokec4 : i\} \cf5 \strokec5 for\cf4 \strokec4  i \cf5 \strokec5 in\cf4 \strokec4  year_list],\cb1 \
\cb3             \cf8 \strokec8 value\cf4 \strokec4 =\cf6 \strokec6 'Select Year'\cf4 \strokec4 ,\cb1 \
\cb3         )),\cb1 \
\cb3     html.Div([\cf2 \strokec2 #TASK 2.3: Add a division for output display\cf4 \cb1 \strokec4 \
\cb3     html.Div(\cf8 \strokec8 id\cf4 \strokec4 =\cf6 \strokec6 'output-container'\cf4 \strokec4 , \cf8 \strokec8 className\cf4 \strokec4 =\cf6 \strokec6 'chart-grid'\cf4 \strokec4 , \cf8 \strokec8 style\cf4 \strokec4 =\{\cf6 \strokec6 'display'\cf4 \strokec4 : \cf6 \strokec6 'flex'\cf4 \strokec4 \}),])\cb1 \
\cb3 ])\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #TASK 2.4: Creating Callbacks\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Define the callback function to update the input container based on the selected statistics\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf9 \cb3 \strokec9 @app.callback\cf4 \strokec4 (\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3     Output(\cf8 \strokec8 component_id\cf4 \strokec4 =\cf6 \strokec6 'select_year'\cf4 \strokec4 , \cf8 \strokec8 component_property\cf4 \strokec4 =\cf6 \strokec6 'disabled'\cf4 \strokec4 ),\cb1 \
\cb3     Input(\cf8 \strokec8 component_id\cf4 \strokec4 =\cf6 \strokec6 'dropdown-statistics'\cf4 \strokec4 ,\cf8 \strokec8 component_property\cf4 \strokec4 =\cf6 \strokec6 'value'\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 update_input_container\cf4 \strokec4 (\cf8 \strokec8 selected_statistics\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 if\cf4 \strokec4  selected_statistics ==\cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 : \cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  \cf7 \strokec7 False\cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 else\cf4 \strokec4 : \cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  \cf7 \strokec7 True\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #Callback for plotting\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Define the callback function to update the input container based on the selected statistics\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf9 \cb3 \strokec9 @app.callback\cf4 \strokec4 (\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3     Output(\cf8 \strokec8 component_id\cf4 \strokec4 =\cf6 \strokec6 'output-container'\cf4 \strokec4 , \cf8 \strokec8 component_property\cf4 \strokec4 =\cf6 \strokec6 'children'\cf4 \strokec4 ),\cb1 \
\cb3     [Input(\cf8 \strokec8 component_id\cf4 \strokec4 =\cf6 \strokec6 'dropdown-statistics'\cf4 \strokec4 , \cf8 \strokec8 component_property\cf4 \strokec4 =\cf6 \strokec6 'value'\cf4 \strokec4 ), Input(\cf8 \strokec8 component_id\cf4 \strokec4 =\cf6 \strokec6 'selec-year'\cf4 \strokec4 , \cf8 \strokec8 component_property\cf4 \strokec4 =\cf6 \strokec6 'value'\cf4 \strokec4 )])\cb1 \
\
\
\pard\pardeftab720\sl360\partightenfactor0
\cf7 \cb3 \strokec7 def\cf4 \strokec4  \cf9 \strokec9 update_output_container\cf4 \strokec4 (\cf8 \strokec8 selected_statistics\cf4 \strokec4 , \cf8 \strokec8 input_year\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3     \cf5 \strokec5 if\cf4 \strokec4  selected_statistics == \cf6 \strokec6 'Recession Period Statistics'\cf4 \strokec4 :\cb1 \
\cb3         \cf2 \strokec2 # Filter the data for recession periods\cf4 \cb1 \strokec4 \
\cb3         recession_data = data[data[\cf6 \strokec6 'Recession'\cf4 \strokec4 ] == \cf10 \strokec10 1\cf4 \strokec4 ]\cb1 \
\cb3         \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #TASK 2.5: Create and display graphs for Recession Report Statistics\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 #Plot 1 Automobile sales fluctuate over Recession Period (year wise)\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         \cf2 \strokec2 # use groupby to create relevant data for plotting\cf4 \cb1 \strokec4 \
\cb3         yearly_rec=recession_data.groupby(\cf6 \strokec6 'Year'\cf4 \strokec4 )[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].mean().reset_index()\cb1 \
\cb3         R_chart1 = dcc.Graph(\cb1 \
\cb3             \cf8 \strokec8 figure\cf4 \strokec4 =px.line(yearly_rec, \cb1 \
\cb3                 \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'Year'\cf4 \strokec4 ,\cb1 \
\cb3                 \cf8 \strokec8 y\cf4 \strokec4 =\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ,\cb1 \
\cb3                 \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Average Automobile Sales fluctuation over Recession Period"\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #Plot 2 Calculate the average number of vehicles sold by vehicle type       \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         \cf2 \strokec2 # use groupby to create relevant data for plotting\cf4 \cb1 \strokec4 \
\cb3         average_sales = recession_data.groupby(\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 )[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].mean().reset_index()                           \cb1 \
\cb3         R_chart2  = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.bar(\cb1 \
\cb3                                             average_sales, \cb1 \
\cb3                                             \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 y\cf4 \strokec4 =\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Average Automobile Sales by Vehicle Type over Recession Period"\cf4 \strokec4 )\cb1 \
\cb3                             )\cb1 \
\cb3         \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Plot 3 Pie chart for total expenditure share by vehicle type during recessions\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         \cf2 \strokec2 # use groupby to create relevant data for plotting\cf4 \cb1 \strokec4 \
\cb3         exp_rec = recession_data.groupby(\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 )[\cf6 \strokec6 'Advertising_Expenditure'\cf4 \strokec4 ].sum().reset_index()\cb1 \
\cb3         R_chart3 = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.pie(\cb1 \
\cb3                                             exp_rec, \cb1 \
\cb3                                             \cf8 \strokec8 values\cf4 \strokec4 =\cf6 \strokec6 'Advertising_Expenditure'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 names\cf4 \strokec4 =\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Advertising Expenditure by Vehicle Type over Recession Period"\cf4 \strokec4 )\cb1 \
\cb3                             )\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         unemp = recession_data.groupby([\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cf6 \strokec6 'unemployment_Rate'\cf4 \strokec4 ])[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].mean().reset_index()\cb1 \
\cb3         R_chart4 = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.histogram(\cb1 \
\cb3                                             unemp,\cb1 \
\cb3                                             \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'unemployment_Rate'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 color\cf4 \strokec4 =\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Unemployment to Automobile Sales by Vehicle Type over Recession Period"\cf4 \strokec4 )\cb1 \
\cb3                             )\cb1 \
\
\
\cb3         \cf5 \strokec5 return\cf4 \strokec4  [\cb1 \
\cb3             html.Div(\cf8 \strokec8 className\cf4 \strokec4 =\cf6 \strokec6 'chart-item'\cf4 \strokec4 , \cf8 \strokec8 children\cf4 \strokec4 =[html.Div(\cf8 \strokec8 children\cf4 \strokec4 =R_chart1),html.Div(\cf8 \strokec8 children\cf4 \strokec4 =R_chart2)],\cf8 \strokec8 style\cf4 \strokec4 =\{\cf6 \strokec6 'display'\cf4 \strokec4 :\cf6 \strokec6 'flex'\cf4 \strokec4 \}),\cb1 \
\cb3             html.Div(\cf8 \strokec8 className\cf4 \strokec4 =\cf6 \strokec6 'chart-item'\cf4 \strokec4 , \cf8 \strokec8 children\cf4 \strokec4 =[html.Div(\cf8 \strokec8 children\cf4 \strokec4 =R_chart3),html.Div(\cf8 \strokec8 children\cf4 \strokec4 =R_chart4)],\cf8 \strokec8 style\cf4 \strokec4 =\{\cf6 \strokec6 'display'\cf4 \strokec4 :\cf6 \strokec6 'flex'\cf4 \strokec4 \})\cb1 \
\cb3                 ]\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # TASK 2.6: Create and display graphs for Yearly Report Statistics\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3  \cf2 \strokec2 # Yearly Statistic Report Plots                             \cf4 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 elif\cf4 \strokec4  (input_year \cf7 \strokec7 and\cf4 \strokec4  selected_statistics==\cf6 \strokec6 'Yearly Statistics'\cf4 \strokec4 ) :\cb1 \
\cb3         yearly_data = data[data[\cf6 \strokec6 'Year'\cf4 \strokec4 ] == input_year]\cb1 \
\cb3                               \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #TASK 2.5: Creating Graphs Yearly data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3                               \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #plot 1 Yearly Automobile sales using line chart for the whole period.\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         yas= data.groupby(\cf6 \strokec6 'Year'\cf4 \strokec4 )[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].mean().reset_index()\cb1 \
\cb3         Y_chart1 = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.line(yas,\cb1 \
\cb3                                             \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'Year'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 y\cf4 \strokec4 =\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Yearly Automobile Sales Average"\cf4 \strokec4 ))\cb1 \
\cb3             \cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Plot 2 Total Monthly Automobile sales using line chart.\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         mas = data.groupby(\cf6 \strokec6 'Month'\cf4 \strokec4 )[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].sum().reset_index()\cb1 \
\cb3         Y_chart2 = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.line(\cb1 \
\cb3                                             mas,\cb1 \
\cb3                                             \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'Month'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 y\cf4 \strokec4 =\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 "Monthly Automobile Sales Total"\cf4 \strokec4 )\cb1 \
\cb3                             )\cb1 \
\
\cb3             \cf2 \strokec2 # Plot bar chart for average number of vehicles sold during the given year\cf4 \cb1 \strokec4 \
\cb3         avr_vdata = yearly_data.groupby(\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 )[\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ].mean().reset_index(\cb1 \
\cb3         \cf8 \strokec8 Y_chart3\cf4 \strokec4  = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.bar(\cb1 \
\cb3                                             avr_vdata, \cb1 \
\cb3                                             \cf8 \strokec8 x\cf4 \strokec4 =\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 y\cf4 \strokec4 =\cf6 \strokec6 'Automobile_Sales'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 'Average Vehicles Sold by Vehicle Type in the year \cf7 \strokec7 \{\}\cf6 \strokec6 '\cf4 \strokec4 .format(input_year))\cb1 \
\cb3                             )\cb1 \
\cb3             \cf2 \strokec2 # Total Advertisement Expenditure for each vehicle using pie chart\cf4 \cb1 \strokec4 \
\cb3         \cf8 \strokec8 exp_data\cf4 \strokec4  = yearly_data.groupby(\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 )[\cf6 \strokec6 'Advertising_Expenditure'\cf4 \strokec4 ].sum().reset_index()\cb1 \
\cb3         \cf8 \strokec8 Y_chart4\cf4 \strokec4  = dcc.Graph(\cf8 \strokec8 figure\cf4 \strokec4 =px.pie(\cb1 \
\cb3                                             exp_data, \cb1 \
\cb3                                             \cf8 \strokec8 values\cf4 \strokec4 =\cf6 \strokec6 'Advertising_Expenditure'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 names\cf4 \strokec4 =\cf6 \strokec6 'Vehicle_Type'\cf4 \strokec4 ,\cb1 \
\cb3                                             \cf8 \strokec8 title\cf4 \strokec4 =\cf6 \strokec6 'Advertising Expenditure by Vehicle Type in the year \cf7 \strokec7 \{\}\cf6 \strokec6 '\cf4 \strokec4 .format(input_year))\cb1 \
\cb3                             )\cb1 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 #TASK 2.6: Returning the graphs for displaying Yearly data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3         \cf5 \strokec5 return\cf4 \strokec4  [\cb1 \
\cb3             html.Div(\cf8 \strokec8 className\cf4 \strokec4 =\cf6 \strokec6 'chart-item'\cf4 \strokec4 , \cf8 \strokec8 children\cf4 \strokec4 =[html.Div(\cf8 \strokec8 children\cf4 \strokec4 =Y_chart1),html.Div(\cf8 \strokec8 children\cf4 \strokec4 =Y_chart2)],\cf8 \strokec8 style\cf4 \strokec4 =\{\cf6 \strokec6 'display'\cf4 \strokec4 :\cf6 \strokec6 'flex'\cf4 \strokec4 \}),\cb1 \
\cb3             html.Div(\cf8 \strokec8 className\cf4 \strokec4 =\cf6 \strokec6 'chart-item'\cf4 \strokec4 , \cf8 \strokec8 children\cf4 \strokec4 =[html.Div(\cf8 \strokec8 children\cf4 \strokec4 =Y_chart3),html.Div(\cf8 \strokec8 children\cf4 \strokec4 =Y_chart4)],\cf8 \strokec8 style\cf4 \strokec4 =\{\cf6 \strokec6 'display'\cf4 \strokec4 :\cf6 \strokec6 'flex'\cf4 \strokec4 \})\cb1 \
\cb3                 ]\cb1 \
\cb3         \cb1 \
\cb3     \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 return\cf4 \strokec4  \cf7 \strokec7 None\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl360\partightenfactor0
\cf2 \cb3 \strokec2 # Run the Dash app\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl360\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf8 \strokec8 __name__\cf4 \strokec4  == \cf6 \strokec6 '__main__'\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl360\partightenfactor0
\cf4 \cb3     app.run_server(\cf8 \strokec8 debug\cf4 \strokec4 =\cf7 \strokec7 True\cf4 \strokec4 )\cb1 \
}