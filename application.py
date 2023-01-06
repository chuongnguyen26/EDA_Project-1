import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

st.set_page_config(layout="wide")

with st.sidebar:
    st.write("hello")

data = pd.read_csv("./fipe_2022.csv")

st.header("1. Introduction")

##############################
### Plot 1 - Correlations  ###
##############################

def plot1():
    new_data = data.loc[:,"engine_size":"age_years"]
    correlation = new_data.corr()
    fig, cor = plt.subplots(figsize = (3,3))

    sns.heatmap(correlation, square = True, cmap='Blues_r')

    plt.tick_params(left = False)
    plt.minorticks_off()
    plt.tick_params(bottom = False)
    plt.title("Correlations Between Categories in Dataset", 
            fontfamily = 'sans serif', fontsize = 10, pad = 40, color = '#078282FF')

    plt.xticks(color = '#078282FF', fontsize = 5)
    plt.yticks(color = '#078282FF', fontsize = 5)

    st.pyplot(fig)

left_col, right_col = st.columns((10, 10))

with left_col:
    plot1()
with right_col:
    st.write()


###################################
### Find 2 - Avg Price by Month ###
###################################

def find_mean(dataframe):
  return round(dataframe["avg_price_brl"].mean())

def find_specific_mean(dataframe, element):
  dataframe_specific = dataframe.loc[dataframe["fuel"] == element,:]
  return round(dataframe_specific["avg_price_brl"].mean())

months = ["January", "February", "March", "April", "May", "June", "July", 
            "August", "September", "October", "November", "December"]
month = []
mean = []
mean_diesel = []
mean_gas = []

for i in range(len(months)):
  curr_month = data.loc[data["month_of_reference"] == months[i],:]
  month.append(months[i][0:3])
  mean.append(find_mean(curr_month))
  mean_diesel.append(find_specific_mean(curr_month, "Diesel"))
  mean_gas.append(find_specific_mean(curr_month, "Gasoline"))

###################################
### Plot 2 - Avg Price by Month ###
###################################

def costumize_plot(fig, plots, size, label_color, bar_color1, bar_color2, y_label, 
graph_title): 
  rect = plots.bar(month, size, color = {bar_color1, bar_color2})

  plots.spines['top'].set_visible(False)
  plots.spines['right'].set_visible(False)
  plots.spines['left'].set_visible(False)
  plots.spines['bottom'].set_visible(False)

  plt.xlabel("Months", fontfamily = 'sans serif', fontsize = 25, 
  color = label_color)
  plt.xticks(color = label_color, fontsize = 20)

  plt.yscale("log")
  plt.ylabel(y_label, fontfamily = 'sans serif', fontsize = 25, 
  color = label_color)

  plt.tick_params(left = False, bottom = False)
  plt.minorticks_off()
  plt.title(graph_title, fontfamily = 'sans serif', fontsize = 25, pad = 40, 
  color = label_color)

  plt.bar_label(rect, padding=3, fontsize = 20, color = label_color)
  plt.tight_layout()
  st.pyplot(fig)

### Pie Graph of the Avg Price by Month ###
###########################################

def pie1():
    explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
    colors = ['#A07855FF','#D4B996FF']

    fig, pie = plt.subplots(figsize=(7,7))
    pie.pie(mean, explodes, month, colors, shadow=True, radius =3, startangle=90, 
    autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
    pie.axis("Equal")

    plt.title("Average Price Per Vehicle for Each Month", fontfamily ='sans serif', 
    fontsize = 20, pad = 40, color = '#A07855FF')
    st.pyplot(fig, use_container_width=True)

### Bar Graph of the Avg Price by Month ###
###########################################

def bar1():
    fig, bar = plt.subplots(figsize=(20,7))

    y_label = "Average Price Per Vehicle"
    graph_title = "Average Price Per Vehicle for Each Month"

    costumize_plot(fig, bar, mean, '#A07855FF', '#A07855FF', '#D4B996FF', y_label, 
    graph_title)

left_col1, right_col1 = st.columns((7.5, 20))

with left_col1:
    pie1()
with right_col1:
    bar1()

### Pie Graph of the Avg Price Run on Diesel by Month ###
#########################################################

def pie2():
    explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
    colors = ['#FFA177FF','#F5C7B8FF']

    fig, pie = plt.subplots(figsize=(7,7))
    pie.pie(mean_diesel, explodes, month, colors, shadow=True, radius = 3, 
    startangle=90, autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
    pie.axis("Equal")

    plt.title("Average Price Per Vehicle Run on Diesel for Each Month", 
    fontfamily = 'sans serif', fontsize = 15, pad = 40, color = '#A07855FF')
    st.pyplot(fig)
    
### Bar Graph of the Avg Price Run on Diesel by Month ###
#########################################################

def bar2():
    fig, bar = plt.subplots(figsize=(20,7))

    y_label = "Average Price Per Vehicle Run on Diesel"
    graph_title = "Average Price Per Vehicle Run on Diesel for Each Month"

    costumize_plot(fig, bar, mean_diesel, '#A07855FF', '#FFA177FF','#F5C7B8FF', 
    y_label, graph_title)

left_col2, right_col2 = st.columns((7.5, 20))

with left_col2:
    pie2()
with right_col2:
    bar2()

### Pie Graph of the Avg Price Run on Gas by Month ###
######################################################

def pie3():
    explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
    colors = ['#EDC2D8FF','#8ABAD3FF']

    fig, pie = plt.subplots(figsize=(7,7))
    pie.pie(mean_gas, explodes, month, colors, shadow=True, radius = 3, 
    startangle=90, autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
    pie.axis("Equal")

    plt.title("Average Price Per Vehicle Run on Gas for Each Month", fontfamily = 'sans serif', fontsize = 15, pad = 40, color = '#A07855FF')
    st.pyplot(fig)

### Bar Graph of the Avg Price Run on Gas by Month ###
######################################################

def bar3():
    fig, bar = plt.subplots(figsize=(20,7))

    y_label = "Average Price Per Vehicle Run on Gas"
    graph_title = "Average Price Per Vehicle Run on Gas for Each Month"

    costumize_plot(fig, bar, mean_gas, '#A07855FF', '#EDC2D8FF', '#8ABAD3FF', 
    y_label, graph_title)

left_col3, right_col3 = st.columns((7.5, 20))

with left_col3:
    pie3()
with right_col3:
    bar3()

##################################
### Find 3 - Avg Price by Year ###
##################################

curr_year = 1985
year = []
mean = []
mean_diesel = []
mean_gas = []

for i in range(39):
  year.append(curr_year)
  curr_time = data.loc[data["year_model"] == curr_year]
  mean.append(find_mean(curr_time))
  mean_diesel.append(find_specific_mean(curr_time, "Diesel"))
  mean_gas.append(find_specific_mean(curr_time, "Gasoline"))
  curr_year+=1

##################################
### Plot 3 - Avg Price by Year ###
##################################

def graph1():
    fig, graph = plt.subplots(figsize=(10,4))

    graph.plot(year, mean, label = "Avg Price Per Vehicle", linestyle = "--", linewidth=2, color="#078282FF")
    graph.plot(year, mean_diesel, label = "Avg Price Per Vehicle Run On Diesel", linestyle = ":", linewidth=2, color="#339E66FF")
    graph.plot(year, mean_gas, label = "Avg Price Per Vehicle Run on Gas", linestyle = "-.", linewidth=2, color="#95DBE5FF")
    graph.legend(fontsize=7)
    plt.yscale("log")

    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)

    plt.tick_params(left = False, bottom = False)
    plt.minorticks_off()
    plt.title("Average Price Per Vehicle Over the Years", 
    fontfamily = 'sans serif', fontsize = 15, pad = 40, color = '#078282FF')

    plt.xlabel("Years", fontfamily = 'sans serif', fontsize = 10, 
    color = '#078282FF')
    plt.xticks(color = '#339E66FF', fontsize = 10)
    plt.ylabel("Average Price Per Vehicle", fontfamily = 'sans serif', 
    fontsize = 10, color = '#078282FF')
    plt.yticks(color = '#339E66FF', fontsize = 10)

    st.pyplot(fig)

graph1()

####################################################
### Find 4 - Avg Price by Year and Total Vehicle ###
####################################################

diesel_vehicle = data.loc[data["fuel"] == "Diesel"]
price_diesel = diesel_vehicle["avg_price_brl"]
year_diesel = diesel_vehicle["year_model"]

price = data["avg_price_brl"]
year = data["year_model"]


gas_vehicle = data.loc[data["fuel"] == "Gasoline"]
price_gas = gas_vehicle["avg_price_brl"]
year_gas = gas_vehicle["year_model"]

####################################################
### Plot 4 - Avg Price by Year and Total Vehicle ###
####################################################

def scatter1():
    fig, plot = plt.subplots(figsize=(10,10))

    sns.scatterplot(year, price/1000, color = '#5A5A5A')

    plt.title("Average Price Per Vehicle Over the Years", 
    fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#195190FF')

    plt.xlabel("Years", fontfamily = 'sans serif', fontsize = 20, 
    color = '#195190FF')
    plt.xticks(color = '#195190FF', fontsize = 20)

    plt.ylabel("Average Price Per Vehicle", fontfamily = 'sans serif', 
    fontsize = 20, color = '#195190FF')
    plt.yticks(color = '#195190FF', fontsize = 20)
    st.pyplot(fig)

def scatter2():
    fig, plot = plt.subplots(figsize=(10,10))

    sns.scatterplot(year_diesel, price_diesel/1000, color = '#5A5A5A')

    plt.title("Average Price Per Vehicle Run On Diesel Over the Years", 
    fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#990011FF')

    plt.xlabel("Years", fontfamily = 'sans serif', fontsize = 20, color = '#990011FF')
    plt.xticks(color = '#990011FF', fontsize = 20)

    plt.ylabel("Average Price Per Vehicle Run On Diesel", 
    fontfamily = 'sans serif', fontsize = 20, color = '#990011FF')
    plt.yticks(color = '#990011FF', fontsize = 20)
    st.pyplot(fig)

def scatter3():
    fig, plot = plt.subplots(figsize=(10,10))

    sns.scatterplot(year_gas, price_gas/1000, color = '#5A5A5A')

    plt.title("Average Price Per Vehicle Run On Gas Over the Years", 
    fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#2C5F2D')
    plt.xlabel("Years", fontfamily = 'sans serif', fontsize = 20, color = '#2C5F2D')
    plt.xticks(color = '#2C5F2D', fontsize = 20)

    plt.ylabel("Average Price Per Vehicle Run On Gas", 
    fontfamily = 'sans serif', fontsize = 20, color = '#2C5F2D')
    plt.yticks(color = '#2C5F2D', fontsize = 20)    
    st.pyplot(fig)

left_col4, middle_col4, right_col4 = st.columns(3)

with left_col4:
    scatter1()
with middle_col4:
    scatter2()
with right_col4:
    scatter3()

###########################################################
### Find 5 - Avg Price by Engine Size and Total Vehicle ###
###########################################################

diesel_vehicle = data.loc[data["fuel"] == "Diesel"]
price_diesel = diesel_vehicle["avg_price_brl"]
engine_diesel = diesel_vehicle["engine_size"]

gas_vehicle = data.loc[data["fuel"] == "Gasoline"]
price_gas = gas_vehicle["avg_price_brl"]
engine_gas = gas_vehicle["engine_size"]

###########################################################
### Plot 5 - Avg Price by Engine Size and Total Vehicle ###
###########################################################

def scatter4():
    fig, engine = plt.subplots(figsize=(10,10))

    sns.scatterplot(engine_diesel, price_diesel/1000, color = '#5A5A5A')

    plt.title("Average Price Per Vehicle Run On Diesel With Different Engine Sizes", fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#603F83FF')

    plt.xlabel("Engine Sizes", fontfamily = 'sans serif', fontsize = 20, color = '#603F83FF')
    plt.xticks(color = '#603F83FF', fontsize = 20)

    plt.ylabel("Average Price Per Vehicle Run On Diesel", fontfamily = 'sans serif', fontsize = 20, color = '#603F83FF')
    plt.yticks(color = '#603F83FF', fontsize = 20)
    st.pyplot(fig)

def scatter5():
    fig, engine = plt.subplots(figsize=(10,10))

    sns.scatterplot(engine_gas, price_gas/1000, color = '#5A5A5A')

    plt.title("Average Price Per Vehicle Run On Gasoline With Different Engine Sizes", fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#195190FF')

    plt.xlabel("Engine Sizes", fontfamily = 'sans serif', fontsize = 20, color = '#195190FF')
    plt.xticks(color = '#195190FF', fontsize = 20)

    plt.ylabel("Average Price Per Vehicle Run On Gasoline", fontfamily = 'sans serif', fontsize = 20, color = '#195190FF')
    plt.yticks(color = '#195190FF', fontsize = 20)
    st.pyplot(fig)

left_col5, right_col5 = st.columns(2)

with left_col5:
    scatter4()
with right_col5:
    scatter5()

#############################################
### Find 6 - Number of Vehicles by Brands ###
#############################################

data.drop(data[(data['fuel'] == "Alcohol")].index, inplace=True)

car_brand = data["brand"].unique()
fuel = data['fuel'].unique()

car_brand_1 = []
diesel_1 = []
gas_1 = []

car_brand_2 = []
diesel_2 = []
gas_2 = []

for i in car_brand:
  brand = data.loc[data["brand"] == i]
  brand_fuel_unique = brand['fuel'].unique()
  brand_fuel_count = brand["fuel"].value_counts()

  if len(car_brand_1) < 43:
    car_brand_1.append(i)
  else:
    car_brand_2.append(i)
  
  if brand_fuel_unique.size == 1:
    if brand_fuel_unique[0] == "Gasoline":
      if len(diesel_1) < 43 and len(gas_1) < 43: 
        gas_1.append(brand_fuel_count[0])
        diesel_1.append(0)
      else:
        gas_2.append(brand_fuel_count[0])
        diesel_2.append(0)
    else:
      if len(diesel_1) < 43 and len(gas_1) < 43:
        diesel_1.append(brand_fuel_count[0])
        gas_1.append(0)
      else:
        diesel_2.append(brand_fuel_count[0])
        gas_2.append(0)
  else:
      if len(diesel_1) < 43 and len(gas_1) < 43:
        gas_1.append(brand_fuel_count[0])
        diesel_1.append(brand_fuel_count[1])
      else:
        gas_2.append(brand_fuel_count[0])
        diesel_2.append(brand_fuel_count[1])

#############################################
### Plot 6 - Number of Vehicles by Brands ###
#############################################

def stacked_bar1():
    fig, graph = plt.subplots(figsize=(20,20))

    graph.barh(car_brand_1, diesel_1, label = "Diesel", color = "#CBCE91FF")
    graph.barh(car_brand_1, gas_1, left=diesel_1, label = "Gasoline", color = "#76528BFF")

    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)
    graph.spines['left'].set_visible(False)
    graph.spines['bottom'].set_visible(False)

    plt.tick_params(left = False)
    plt.minorticks_off()
    plt.tick_params(bottom = False)
    plt.title("Amount of Diesel and Gasoline Vehicles by Brand", fontfamily = 'sans serif', fontsize = 25, pad = 40, color = '#76528BFF')

    plt.xlabel("Total Amount of Vehicles", fontfamily = 'sans serif', fontsize = 20, color = '#76528BFF')
    plt.xticks(color = '#76528BFF', fontsize = 20)

    plt.ylabel("Brands", fontfamily = 'sans serif', fontsize = 20, color = '#76528BFF')
    plt.yticks(color = '#76528BFF', fontsize = 15)

    plt.legend(prop={'size': 20})
    st.pyplot(fig)

def stacked_bar2():
    fig, graph = plt.subplots(figsize=(20,20))

    graph.barh(car_brand_2, diesel_2, label = "Diesel", color = "#CBCE91FF")
    graph.barh(car_brand_2, gas_2, left=diesel_2, label = "Gasoline", color = "#76528BFF")

    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)
    graph.spines['left'].set_visible(False)
    graph.spines['bottom'].set_visible(False)

    plt.tick_params(left = False)
    plt.minorticks_off()
    plt.tick_params(bottom = False)
    plt.title("Amount of Diesel and Gasoline Vehicles by Brand", 
    fontfamily = 'sans serif', fontsize = 25, pad = 40, color = '#76528BFF')

    plt.xlabel("Total Amount of Vehicles", fontfamily = 'sans serif', 
    fontsize = 20, color = '#76528BFF')
    plt.xticks(color = '#76528BFF', fontsize = 20)

    plt.ylabel("Brands", fontfamily = 'sans serif', fontsize = 20, color = '#76528BFF')
    plt.yticks(color = '#76528BFF', fontsize = 15)

    plt.legend(prop={'size': 20})
    st.pyplot(fig)

left_col6, right_col6 = st.columns(2)

with left_col6:
    stacked_bar1()
with right_col6:
    stacked_bar2()

##########################################################
### Find 7 - Number of Vehicles by Gear and Fuel Types ###
##########################################################

info = data.loc[:,["fuel", "gear"]]

def value_gear(dataframe, element, value_type):
  return dataframe.loc[info[element] == value_type]

gas = value_gear(info, "fuel", "Gasoline")
diesel = value_gear(info, "fuel", "Diesel")

manual = [len(value_gear(gas, "gear", "manual")), len(value_gear(diesel, "gear", "manual"))]
automatic = [len(value_gear(gas, "gear", "automatic")), len(value_gear(diesel, "gear", "automatic"))]

##########################################################
### Plot 7 - Number of Vehicles by Gear and Fuel Types ###
##########################################################

def stacked_bar3():
    fig, graph = plt.subplots(figsize = (10,10))

    labels = ["Gas", "Diesel"]

    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)
    graph.spines['left'].set_visible(False)
    graph.spines['bottom'].set_visible(False)
    plt.tick_params(left = False, labelleft = False, bottom = False)

    x = np.arange(len(labels))
    width = 0.35

    rects1 = graph.bar(x - width/2, manual, width, label='Manual', color = "#13424C")
    rects2 = graph.bar(x + width/2, automatic, width, label='Automatic', color = "#218490")

    plt.xlabel("Fuels", fontfamily = 'sans serif', fontsize = 25, color = "#394D5F")
    plt.xticks(x, labels, fontsize = 20, color = "#394D5F")

    plt.ylabel('Number of Vehicles by Gear Type', fontfamily = 'sans serif', fontsize = 25, color = "#394D5F")

    # Add some text for labels, title and custom x-graphis tick labels, etc.
    plt.ylabel('Number of Vehicles by Gear Type', fontfamily = 'sans serif', fontsize = 25)
    plt.title('Numbers of Manual and Automatic Vehicles based on Different Fuels', fontfamily = 'sans serif', fontsize = 25, pad = 40, color = "#394D5F")
    plt.legend(prop={'size': 20})

    plt.bar_label(rects1, padding=3, fontsize = 20, color = "#13424C")
    plt.bar_label(rects2, padding=3, fontsize = 20, color = "#218490")

    fig.tight_layout()
    st.pyplot(fig)

left_col7, right_col7 = st.columns(2)

with left_col7:
    stacked_bar3()
with right_col7:
    st.write()

###############################################################
### Find 8 - Number of Vehicles by Gear Type over the Years ###
###############################################################

info = data.loc[:,["gear", "year_model"]]

gear_manual = value_gear(info, "gear", "manual")
gear_automatic = value_gear(info, "gear", "automatic")

curr = 1985
years = []
manual = []
automatic = []

for i in range(len(info["year_model"].unique())):
  years.append(curr)
  manual.append(len(value_gear(gear_manual, "year_model", curr)))
  automatic.append(len(value_gear(gear_automatic, "year_model", curr)))
  curr += 1

gears = {
    "Manual Gear": manual,
    "Automatic Gear": automatic,
}

###############################################################
### Plot 8 - Number of Vehicles by Gear Type over the Years ###
###############################################################

def stacked_graph1():
    fig, graph = plt.subplots(figsize = (10,10))

    graph.spines['top'].set_visible(False)
    graph.spines['right'].set_visible(False)
    graph.spines['left'].set_visible(False)
    graph.spines['bottom'].set_visible(False)
    plt.tick_params(left = False, labelleft = False, bottom = False, pad = 10)

    plt.xlabel("Years", fontfamily = 'sans serif', fontsize = 25, color = "#394D5F")
    plt.ylabel("Total Vehicles", fontfamily = 'sans serif', fontsize = 25, 
    color = "#394D5F")
    plt.title("Amount of Vehicles By Gear Type Over Years",fontfamily = 'sans serif', 
    fontsize = 25, color = "#394D5F", pad = 40)

    year = [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
    plt.xticks(year, fontfamily = 'sans serif', fontsize = 20, color = "#394D5F")


    plt.stackplot(years, gears.values(), labels=gears.keys(),)

    plt.legend(prop={'size': 20}, loc="upper left")
    st.pyplot(fig)

left_col8, right_col8 = st.columns(2)

with left_col8:
    st.write()
with right_col8:
    stacked_graph1()