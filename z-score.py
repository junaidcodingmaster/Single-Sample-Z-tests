import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
from time import sleep
import os


df = pd.read_csv("data/School2.csv")
data = df["Math_score"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)


std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)


first_std_deviation_start, first_std_deviation_end = (
    mean - std_deviation,
    mean + std_deviation,
)
second_std_deviation_start, second_std_deviation_end = mean - (
    2 * std_deviation
), mean + (2 * std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (
    3 * std_deviation
), mean + (3 * std_deviation)


df = pd.read_csv("data/School_1_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(
    go.Scatter(
        x=[mean_of_sample1, mean_of_sample1],
        y=[0, 0.17],
        mode="lines",
        name="MEAN OF STUDENTS WHO HAD MATH LABS",
    )
)
fig.add_trace(
    go.Scatter(
        x=[first_std_deviation_end, first_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 1 END",
    )
)
fig.add_trace(
    go.Scatter(
        x=[second_std_deviation_end, second_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 2 END",
    )
)
fig.add_trace(
    go.Scatter(
        x=[third_std_deviation_end, third_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 3 END",
    )
)
fig.show()



df = pd.read_csv("data/School_2_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(
    go.Scatter(
        x=[mean_of_sample2, mean_of_sample2],
        y=[0, 0.17],
        mode="lines",
        name="MEAN OF STUDENTS WHO USED THE APP",
    )
)
fig.add_trace(
    go.Scatter(
        x=[first_std_deviation_end, first_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 1 END",
    )
)
fig.add_trace(
    go.Scatter(
        x=[second_std_deviation_end, second_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 2 END",
    )
)
fig.add_trace(
    go.Scatter(
        x=[third_std_deviation_end, third_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 3 END",
    )
)
fig.show()



df = pd.read_csv("data/School_3_Sample.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(
    go.Scatter(
        x=[mean_of_sample3, mean_of_sample3],
        y=[0, 0.17],
        mode="lines",
        name="MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS",
    )
)
fig.add_trace(
    go.Scatter(
        x=[second_std_deviation_end, second_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 2 END",
    )
)
fig.add_trace(
    go.Scatter(
        x=[third_std_deviation_end, third_std_deviation_end],
        y=[0, 0.17],
        mode="lines",
        name="STANDARD DEVIATION 3 END",
    )
)
fig.show()


print("\nWait for few seconds ...\n")

sleep(1)
os.system("cls")
print("\n")

# Total
print("mean of sampling distribution:- ", mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

print("\n")

# mean of sample data
print("Mean of sample1:- ", mean_of_sample1)
print("mean of sample 2:- ", mean_of_sample2)
print("mean of sample3:- ", mean_of_sample3)

print("\n")

# Z-score outputs
z_score1 = (mean - mean_of_sample1) / std_deviation
print("The z score of Sample1 ->", z_score1)

z_score2 = (mean - mean_of_sample2) / std_deviation
print("The z score of Sample2 ->", z_score2)

z_score3 = (mean - mean_of_sample3) / std_deviation
print("The z score of Sample3 ->", z_score3)

print("\nMade By Junaid.\n")
