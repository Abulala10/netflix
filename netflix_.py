import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

welcome = '{ < ___Welcome Netflix Program___ > }\n'


class Netflix:

    def __init__(self, netflix):
        global save
        self.verbose = True
        print(netflix)
        self.directory = 'D:\dataSets\\netflixFigures\\'

    def readFile(self, netflix_df):
        verbose = input('Do you want to print the File (yes/no)? ').casefold()
        try:
            if verbose.__eq__('yes'):
                if netflix_df is not None:
                    print(netflix_df)
        except FileNotFoundError as fnf:
            print('1 :', fnf)

    def countries_type_on_netflix(self, movie_show):
        global name
        try:
            label = ['Number of Movies', 'Number of TV Shows']
            tv_movie = movie_show.value_counts()
            plt.pie(tv_movie, colors=['green', 'purple'], autopct='%1.1f', radius=0.8)
            plt.title('Comparing Number of Tv Shows and Movies on Netflix')
            plt.legend(labels=label, loc='lower left')
            if save.__eq__('yes'):
                name = input('Enter Name for Chart > ')
                plt.savefig(self.directory + name + '.png')
            plt.show()
        except Exception as e:
            print(e)

    def content_added_over_years(self, year, tv_movie):
        global name
        try:
            growth = year.value_counts().reset_index()
            Movie_index = growth['index'].where(tv_movie == 'Movie')
            Movie_year = growth['release_year'].where(tv_movie == 'Movie')
            plt.bar(Movie_index, Movie_year, color=['green', 'purple'])  # x, y, color
            Tv_index = growth['index'].where(tv_movie == 'TV Show')
            Tv_year = growth['release_year'].where(tv_movie == 'TV Show')
            plt.bar(Tv_index, Tv_year, color='purple')
            plt.title('Content Added Over The Years On Netflix')
            plt.xlabel('Years')
            plt.ylabel('Number Of Movies')
            plt.legend(labels=['Movie', 'TV Show'])
            if save.__eq__('yes'):
                name = input('Enter Name of Chart > ')
                plt.savefig(self.directory + name + '.png')
            plt.show()
        except Exception as e:
            print(e)

    def most_listed_in(self, category):
        global name
        try:
            category_name = ['Documentaries', 'Stand-up Comedy', 'Dramas, International Movies',
                             'Dramas, Independent Movies, International Movies',
                             'Comedies, Dramas, International Movies']
            cat = category.value_counts().reset_index()
            # cat['listed_in'] == sum of category
            fig, ax = plt.subplots()
            plotPie = cat['listed_in'].where(cat['listed_in'] > 170).dropna()  # Main line for pie()
            ax.pie(plotPie, autopct='%2.1f', colors=['firebrick', 'yellow', 'salmon', 'palegreen', 'violet'],
                   radius=0.7)
            ax.set_title('Highest number of Movie/Tv-Show Category in Netflix')
            ax.legend(labels=category_name, loc='lower left', fontsize=8)
            if save.__eq__('yes'):
                name = input('Enter Name of Chart > ')
                plt.savefig(self.directory + name + '.png')
            plt.show()
        except Exception as e:
            print(e)


cmd = Netflix(welcome)
if __name__ == '__main__':
    global df, copy_df, save, name
    try:
        df = pd.read_csv('D:\dataSets\kaggle\\netflix_titles.csv')
        copy_df = df.copy()
        cmd.readFile(df)
        save = input('Do you want to save the charts ? (yes/no) ')
        cmd.countries_type_on_netflix(copy_df['type'])
        cmd.content_added_over_years(copy_df['release_year'], copy_df['type'])
        cmd.most_listed_in(copy_df['listed_in'])
        if save.__eq__('yes'):
            print('Charts Saved At Location : ' + cmd.directory)
    except Exception as e:
        print(e)
