import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

def line_break():
        st.markdown("<h1 ></h1>", unsafe_allow_html=True)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with st.sidebar:
    selected_tab = option_menu(
    menu_title=None,
    options=["Car Analysis", "My Journey"],
    icons=["bar-chart", "card-text"],
    menu_icon="cast",
    )
    line_break()
    st.write("**Citations:**")
    st.markdown("""
        <ul>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            hrefhttps://www.kaggle.com/datasets/vagnerbessa/average-car-prices-bazil">
            Kaggle</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="https://seaborn.pydata.org/generated/seaborn.scatterplot.html?highlight=scatterplot#seaborn.scatterplot">
            Seaborn</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="https://matplotlib.org/stable/plot_types/index.html">
            Matplotlib</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://matplotlib.org/stable/gallery/index.html">
            Matplotlib</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://stackoverflow.com/questions/63291627/how-to-do-internal-links-in-google-colab">
            Stack Over Flow</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://stackoverflow.com/questions/2969867/how-do-i-add-space-between-the-ticklabels-and-the-axes-in-matplotlib">
            Stack Over Flow</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/">
            Machine Learning Mastery</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://www.statology.org/matplotlib-legend-position/">
            Statology</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://www.freecodecamp.org/news/python-typeerror-int-object-not-subscriptable-solved/">
            Free Code Camp</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://designwizard.com/blog/design-trends/colour-combination/">
            Design Wizard</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://github.com/alckasoc">
            Vincent's Github</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://lottiefiles.com/39792-thank-you-note">
            Mishal Alnazawi's Animation</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://lottiefiles.com/90989-graph3">
            UshaR's Animation</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://lottiefiles.com/35070-car-loading">
            Shah Iran's Animation</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://lottiefiles.com/92042-fast-truck">
            Rupesh Pattanayak's Animation</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://lottiefiles.com/10911-json-journey">
            Lulu's Animation</a></li>
        </ul>""",
        unsafe_allow_html=True
    )
    st.write("I would like to acknowledge all of sources mentioned above for"
    " providing me the resources and opportunities to learn Exploratory Data"
    " Analysis and making this project possible. I would like to give a shout out"
    " to Vincent for being such as great Mentor. Thank You!")
    st.write("(Note: All animations used in this application are from Lottie Files"
    " which are free and have been permitted by creators for usage.)")
    lottie_code5 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_t7jtcf8d.json")

    st_lottie(
        lottie_code5,
    )

if selected_tab == "Car Analysis":
    data = pd.read_csv("./fipe_2022.csv")

    lottie_code = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_jay0joxv.json")

    st.markdown("<h1 style='text-align: center; font-size: 20'>Dive Into Car Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-size: 20'>By Chuong Nguyen</h4>", unsafe_allow_html=True)

    st_lottie(
        lottie_code,
        height = 500,
    )

    st.header("0. Table of Content")
    st.markdown("""
        <ul>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="#1-introduction">
            1. Introduction</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="#2-eda-analysis">2. EDA Analysis</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="#3-conclusion">
            3. Conclusion</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="#4-author-info">
            4. Author Info</a></li>
        </ul>""",
        unsafe_allow_html=True
    )

    st.header("1. Introduction")
    st.write("Hello and Welcome! I'm Chuong Nguyen, as of this project, I'm a 1st year"
    " Computer Science Major at the Universty of California San Diego. This"
    " will be my first in-depth EDA project analyzing car manufacturing market.")

    left, right = st.columns((10,5))

    with left:
        st.write("Why chose EDA Analysis? First of all, this project will be the first phase"
    " into Machine Learning. But most importantly, this is the opportunity for me"
    " to have a peek at how Machine Learning and AI work in general. I always questioned"
    " how in the world a machine could teach itself to learn. Well, this project will"
    " uncover some answers as I go through my struggles and 'oh' moments. I hope you enjoy it.")

        st.write("Brief about this project. The EDA process is performed on a largely"
        " cleaned dataset found on Kaggle. The data will be used to plot multiple charts"
        " and graphs that will focus and answer questions surrounding average price"
        " per vehicle and how the values might be impacted by fuel types, brand, time, and"
        " gear types. This project is structured with an introduction, followed by the EDA"
        " Analysis, and ends with a Conclusion. Aside the main page, there is a second"
        " page talking about my EDA journey.")

    with right:
        lottie_code1 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_yvze9l8i.json")
        st_lottie(
            lottie_code1,
            height = 200,
        )

    st.header("2. EDA Analysis")

    st.write("Since the dataset that I am using is largely clean, I don't need"
    " to make any data scrape and therefore could jump directly to EDA. (Note, I did"
    " make few checks to see if there is any NaN value and false value)")

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

        plt.xticks(rotation=45, color = '#078282FF', fontsize = 5)
        plt.yticks(color = '#078282FF', fontsize = 5)

        st.pyplot(fig)

    left_col, center_col, right_col = st.columns((15, 3, 10))

    with left_col:
        plot1()
    with center_col:
        st.write()
    with right_col:
        st.write("Beginning with my EDA process, I checked if there were any" 
        " correlations between categories in the dataset. Based on this plot, blocks"
        " with the darkest or lightest color mean that the categories in the x and y" 
        " axes have the highest correlations. While colors in between are based on"
        " the plot's legend mean, there is little to no correlation. I need to know"
        " what pair of categories to avoid doing EDA analysis since the process will"
        " be unnecessary in this case. Regarding the correlation between categories,"
        " the pairs that resulted in a negative correlation tell that the result"
        " changes are reversed, which means that when I increase the input value,"
        " my output is expected to decrease. The same logic applies to a positive"
        " correlation. But instead of having a reverse relationship, an increase in"
        " the input will also result in an increase output.")


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
        plt.bar_label(rect, padding=3, fontsize = 20, color = label_color)
        plt.tight_layout()
        st.pyplot(fig)

    line_break()
    st.markdown("<p style='text-align: center; font-size: 1em'>Average Price Per Vehicle for Each Month</p>", unsafe_allow_html=True)
    line_break()

    ### Pie Graph of the Avg Price by Month ###
    ###########################################

    def pie1():
        explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
        colors = ['#A07855FF','#D4B996FF']

        fig, pie = plt.subplots(figsize=(7,7))
        pie.pie(mean, explodes, month, colors, shadow=True, radius =3, startangle=90, 
        autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
        pie.axis("Equal")
        st.pyplot(fig, use_container_width=True)

    ### Bar Graph of the Avg Price by Month ###
    ###########################################

    def bar1():
        fig, bar = plt.subplots(figsize=(20,7))

        y_label = "Average Price Per Vehicle"
        graph_title = "Average Price Per Vehicle for Each Month"

        costumize_plot(fig, bar, mean, '#A07855FF', '#A07855FF', '#D4B996FF', y_label, 
        graph_title)

    left_col1, center_col1, right_col1 = st.columns((9, 3, 20))

    with left_col1:
        pie1()
    with center_col1:
        st.write()
    with right_col1:
        bar1()

    ### Pie Graph of the Avg Price Run on Diesel by Month ###
    #########################################################

    line_break()
    st.markdown("<p style='text-align: center; font-size: 1em'>Average Price Per Vehicle Run on Diesel for Each Month</p>", 
    unsafe_allow_html=True)
    line_break()

    def pie2():
        explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
        colors = ['#FFA177FF','#F5C7B8FF']

        fig, pie = plt.subplots(figsize=(7,7))
        pie.pie(mean_diesel, explodes, month, colors, shadow=True, radius = 3, 
        startangle=90, autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
        pie.axis("Equal")
        st.pyplot(fig)
        
    ### Bar Graph of the Avg Price Run on Diesel by Month ###
    #########################################################

    def bar2():
        fig, bar = plt.subplots(figsize=(20,7))

        y_label = "Average Price Per Vehicle Run on Diesel"
        graph_title = "Average Price Per Vehicle Run on Diesel for Each Month"

        costumize_plot(fig, bar, mean_diesel, '#A07855FF', '#FFA177FF','#F5C7B8FF', 
        y_label, graph_title)

    left_col2, center_col2, right_col2 = st.columns((20, 3, 9))

    with left_col2:
        bar2()
    with center_col2:
        st.write()
    with right_col2:
        pie2()

    ### Pie Graph of the Avg Price Run on Gas by Month ###
    ######################################################

    line_break()
    st.markdown("<p style='text-align: center; font-size: 1em'>Average Price Per Vehicle Run on Gas for Each Month</p>", 
    unsafe_allow_html=True)
    line_break()

    def pie3():
        explodes = [0.3,0.3,0,0,0,0,0,0,0.1,0.1,0.1,0.1]
        colors = ['#EDC2D8FF','#8ABAD3FF']

        fig, pie = plt.subplots(figsize=(7,7))
        pie.pie(mean_gas, explodes, month, colors, shadow=True, radius = 3, 
        startangle=90, autopct='%1.1f%%', wedgeprops={'linewidth': 3.0, 'edgecolor': 'w'})
        pie.axis("Equal")
        st.pyplot(fig)

    ### Bar Graph of the Avg Price Run on Gas by Month ###
    ######################################################

    def bar3():
        fig, bar = plt.subplots(figsize=(20,7))

        y_label = "Average Price Per Vehicle Run on Gas"
        graph_title = "Average Price Per Vehicle Run on Gas for Each Month"

        costumize_plot(fig, bar, mean_gas, '#A07855FF', '#EDC2D8FF', '#8ABAD3FF', 
        y_label, graph_title)

    left_col3, center_col3, right_col3 = st.columns((9, 3, 20))

    with left_col3:
        pie3()
    with center_col3:
        st.write()
    with right_col3:
        bar3()

    line_break()
    st.write("As I look at the pie and bar graphs, I can't stop but be amazed"
    " by the unexpecting results. Why are car prices getting higher toward the end"
    " of the year, and why is there such a big price gap between January and"
    " December? After much thought, it makes sense for the result to come out the"
    " way it is because, according to Spectrum News1, people spend more when"
    " the weather is much cooler. Coincidentally, the last quarter months of the year"
    " are also the time of the holidays, when businesses provide large discounts and sales"
    " to encourage consumers to spend more. But wait, how does spending more related to"
    " higher prices? Well, spending more drives up costs because limited"
    " products can't accommodate high demands. Creating a problem known as inflation,"
    " where buyers have to spend more than they would otherwise when goods are plentiful."
    " Notice how the price dramatically dropped in January, which is not accidental"
    " because January is after all of the big holidays. (Note regarding the average price"
    " you might think the values are false because the average price is way too"
    " high to be logical. However, in this dataset, luxurious cars like Rolls Royce and"
    " Mercedes are also included, which might increase the value a little. And these outliers"
    " are too essential to eliminate> Additionally, since I'm evaluating price trends"
    " by month, the specific values are unimportant.")

    st.markdown("<a style='color: black;' href='https://spectrumlocalnews.com/nys/central-ny/weather/2022/12/10/do-we-spend-more-money-when-it-s-cold-'>- Spectrum News1</a>",
    unsafe_allow_html=True)
    line_break()

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

    left_col4, center_col4, right_col4 = st.columns((3, 10, 3))

    with left_col4:
        st.write()
    with center_col4:
        graph1()
    with right_col4:
        st.write()

    line_break()
    st.write("As expected, the average price per vehicle trends upward over the years"
    " and will no doubt continue to grow in order to adjust for inflation, and growing"
    " labor, transportation, and raw material costs. In terms of this graph, I compared"
    " the price of vehicles based on the fuel types and if that may differ from the"
    " overall price, which serves as the controlled variable. Overall, all of the"
    " graphs trend upward which go according to my prediction.")

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

    # ####################################################
    # ### Plot 4 - Avg Price by Year and Total Vehicle ###
    # ####################################################

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

    line_break()
    left_col5, middle_col5, right_col5 = st.columns(3)

    with left_col5:
        scatter1()
    with middle_col5:
        scatter2()
    with right_col5:
        scatter3()

    line_break()
    st.write("Wait, isn't there already a graph that plotted the average price of vehicles"
    " over the years? Absolutely correct, but I want to have closer look at the"
    " distribution of vehicles based on prices over the years. And based on these scatter"
    " plots, we can see the distribution of cars based on prices to be fairly accurate"
    " with today's values.")
    line_break()

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

    left_col6, right_col6 = st.columns(2)

    with left_col6:
        lottie_code2 = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_bx07iy2i.json")
        st_lottie(
            lottie_code2,
            height = 100,
        )
        st.write("Based on research, vehicles run on diesel are typically large trucks."
        " It is very interesting to see that consumers prefer trucks with smaller"
        " engine size. And according to WhichCar, the reason the smaller engine trucks"
        " are popular among consumers is because they are more efficient and lesser cost"
        " to operate. While bigger engine size trucks are more powerful, but the less"
        " efficient performance and higher cost is too much for consumers to bear.")
        st.markdown("<a style='color: black' href='https://www.whichcar.com.au/car-advice/what-is-engine-size-and-why-does-it-matter'>- WhichCar</a>",
        unsafe_allow_html=True)
    with right_col6:
        scatter4()

    def scatter5():
        fig, engine = plt.subplots(figsize=(10,10))

        sns.scatterplot(engine_gas, price_gas/1000, color = '#5A5A5A')

        plt.title("Average Price Per Vehicle Run On Gasoline With Different Engine Sizes", fontfamily = 'sans serif', fontsize = 22, pad = 40, color = '#195190FF')

        plt.xlabel("Engine Sizes", fontfamily = 'sans serif', fontsize = 20, color = '#195190FF')
        plt.xticks(color = '#195190FF', fontsize = 20)

        plt.ylabel("Average Price Per Vehicle Run On Gasoline", fontfamily = 'sans serif', fontsize = 20, color = '#195190FF')
        plt.yticks(color = '#195190FF', fontsize = 20)
        st.pyplot(fig)
    line_break()

    left_col7, right_col7 = st.columns(2)
    with left_col7:
        scatter5()
    with right_col7:
        st.write("On the other hand, vehicles run on gasoline are typically Sedan, SUV"
        " or smaller car types. And interesting enough, consumers prefer middle to"
        " to larger engine size for smaller vehicles. According to Carbuyer, consumers"
        " are interested in larger engine size vehicle because it means that the car"
        " has the capacity to take in larger load, accelerate faster, and bigger in"
        " size. Which is very convenient for traveling long distance and carrying"
        " decent size cargoes that a truck might be large for the use.")
        st.markdown("<a style='color: black' href='https://www.whichcar.com.au/car-advice/what-is-engine-size-and-why-does-it-matter'>- CarBuyer</a>", 
        unsafe_allow_html=True)
        lottie_code3 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_zbyipz72.json")
        st_lottie(
            lottie_code3,
            height = 100,
        )
    line_break()

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

        plt.xlabel("Total Amount of Vehicles", fontfamily = 'sans serif', 
        fontsize = 20, color = '#76528BFF')
        plt.xticks(color = '#76528BFF', fontsize = 20)

        plt.ylabel("Brands", fontfamily = 'sans serif', fontsize = 20, color = '#76528BFF')
        plt.yticks(color = '#76528BFF', fontsize = 15)

        plt.legend(prop={'size': 20})
        st.pyplot(fig)

    st.markdown("<p style='text-align: center; font-size: 1em'>Amount of Diesel and Gasoline Vehicles by Brand</p>", unsafe_allow_html=True)
    line_break()
    left_col8, right_col8 = st.columns(2)

    with left_col8:
        stacked_bar1()
    with right_col8:
        stacked_bar2()

    line_break()
    st.write("As expected, the major car companies dominate in production and sales."
    " But is very suprising to see such a large difference in production number between"
    " well known and lesser known companies. Additionally, it is noticeable that almost"
    " all major car companies don't focus solely on the production of just vehicles"
    " run on gasoline or vice versa. Instead, the companies are very diverse in producing"
    " both gasoline and diesel type vehicles. Beside gear types, it is also"
    " expected to see a large portion of the car companies' production to be on gasoline"
    " type vehicles since they predominately smaller and more accessible to wider range"
    " of consumers compared to diesel which are mostly truck types.")

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
    line_break()

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

    left_col9, center_col9, right_col9 = st.columns((1,3,1))

    with left_col9:
        st.write()
    with center_col9:
        stacked_bar3()
    with right_col9:
        st.write()

    line_break()
    st.write("Shocking. I would have never guessed that automatic vehicles are less"
    " popular compared to manual. How in the world could this be, when most of the cars"
    " in the U.S. run on automatic gear and very few are manual? I thought the U.S."
    " is the world leading market, meaning that what is sold in the U.S. would be"
    " widely adopted else where in the world. After few considerations, I thought"
    " the result make sense because one type of vehicle is successful here in the U.S."
    " does mean the same whole true else where. Comapnies have consider many factors"
    " like the condition of infrastucture, affordability, and more.")
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
    line_break()

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

    left_col10, center_col10, right_col10 = st.columns((1,3,1))

    with left_col8:
        st.write()
    with center_col10:
        stacked_graph1()
    with right_col8:
        st.write()

    line_break()
    st.write("As we are taking a futher look into gear types, we can notice that"
    " manual gear got introduced a decade before automatic gear, and manual gear has"
    " domanated the market for many years. However, since 2010 moving foward, automatic"
    " gear saw an increasing popularity among consumers. Indicating a shift from manual"
    " to automatic gear. This trend will continue as autonomous and electric vehicles"
    " are becoming a reality and more people are becoming serious and concerns regarding"
    " climate change.")

    st.header("3. Conclusion")
    st.write("Amazing. If you're reading this, pat yourself in the back because you"
    " have reached the end of this project. I have learned a lot about EDA and the"
    " process of doing ML, and I hope you do as well. I am grateful to make this"
    " project a reality as I have grown a lot as a CS student, from learning EDA to"
    " linux comands. From organizing a wonderful notebook to making my own Github"
    " repository, to creating a web application. Thank you very much for your time,"
    " your dedication means a whole lot to me and I greatly appreciated. Feel free to"
    " reach out to me, the links are included below.")

    st.header("4. Author Info")

    st.markdown("""
        <ul>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://github.com/chuongnguyen26/EDA_Project-1">
            GitHub Repo</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="https://github.com/chuongnguyen26">GitHub</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2"
            href="https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin">
            LinkedIn</a></li>
            <li style="color: black;"><a style="color: black; text-decoration:none; font-size: 15px; line-height: 2" 
            href="https://www.kaggle.com/chuong26">
            Kaggle</a></li>
        </ul>""",
        unsafe_allow_html=True
    )

else:
    st.markdown("<h1 style='text-align: center; font-size: 20'>My EDA Journey</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-size: 20'>By Chuong Nguyen</h4>", unsafe_allow_html=True)
    lottie_code4 = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_6prATB.json")
    st_lottie(
        lottie_code4,
        height = 500,
    )

    st.header("1. Intro")
    st.write("This project took about a month to complete. I started this poject"
    " in the early December of 2022. Over a month on this project, I explored"
    " and analyzed the data, considered EDA approach, and created a web application."
    " This project was wonderful and I have grown a lot as CS student.")

    st.header("2. Difficulties")
    st.write("In the process of making this project, I experienced a lot of unknowns"
    " and difficulties. I had to do a lot of googling and seeking helps from my"
    " ACM mentor. I remember when generating my plots, I spent close to two weeks writing"
    " redundant codes that my Colab notebook looks so messy. I was hard coding"
    " every values from the dataset to plot my graphs. Through this project that"
    " I learned to organize my code by defining methods and using loops/conditional"
    " statements. Another technical difficulty I faced was understanding linux"
    " commands and just navigating vscode. I had difficulties cloning a repository in vscode and linking it to"
    " github, change file directory, installing new libaries, and using linux commands"
    " in the terminal. Through this project that I have the opportunity to practice"
    " and getting confident with vscode and coding tools in general. For a non-technical"
    " difficulty, I had some hard time designing and making both my notebook"
    " and this web application appealing to the viewers. I tried balancing between"
    " imagery and texts, picking the right fonts and colors for display. This project"
    " has taught me the non-cse skill that I think is very helpful in displaying my work"
    " to the audience in the most appealing and easy understand.")

    st.header("3. Takeaways")
    st.write("All in all, after much struggles and learning, I have grown a lot"
    " as a Computer Science student and a human being. I have learned the importance"
    " of googling. I learned how to use numpy, pandas, matplotlib, vscode, and streamlit."
    " I have realized that sometimes I don't have to know everything in order to"
    " work on a project. If I don't know what EDA is or Streamlit is, I learned not"
    " to be afraid to google or ask my mentor. This project has taught me that if"
    " I don't try, then how will I know where to start and what to learn. Though"
    " this project has been tough and challenging. But to accomplish and make my goal"
    " possible is far more meaningful. I have enjoyed every single part of this project"
    " and I am looking forward to starting the 2nd phase. This journey is far from"
    " over, as this is just the beginning of my journey.")
    st.write("Until then, thank you for your time.")
    st.write("Chuong Nguyen")