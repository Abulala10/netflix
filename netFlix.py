import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

welcome = '< ___Welcome Netflix Program___ >'


class Netflix:

    def __init__(self, netflix):
        global save
        self.verbose = True
        print(netflix)

    def readFile(self, netflix_df):
        verbose = input('Do you want to print First 10 lines of the File (yes/no)? ').casefold()
        try:
            if verbose.__eq__('yes'):
                if netflix_df is not None:
                    print(netflix_df.head(10))
        except FileNotFoundError as fnf:
            print('1 :', fnf)

    def countries_type_on_netflix(self, movie_show): # movie_tv_pie is the ooutput of this function.
        try:
            label = ['Number of Movies', 'Number of TV Shows']
            tv_movie = movie_show.value_counts()
            plt.pie(tv_movie, colors=['green', 'purple'], autopct='%1.1f', radius=0.8)
            plt.title('Comparing Number of Tv Shows and Movies on Netflix')
            plt.legend(labels=label, loc='lower left')
            if save.__eq__('yes'):
                plt.savefig('D:dataSets\\netflixFigures\movie_tv_pie.png')
            plt.show()
        except Exception as e:
            print(e)

    def content_added_over_years(self, year, tv_movie): # content_added_over_years.png is the output of this function.
        try:
            growth = year.value_counts().reset_index()
            Movie_index = growth['index'].where(tv_movie == 'Movie')
            Movie_year = growth['release_year'].where(tv_movie == 'Movie')
            plt.bar(Movie_index, Movie_year, color=['green', 'purple'])
            Tv_index = growth['index'].where(tv_movie == 'TV Show')
            Tv_year = growth['release_year'].where(tv_movie == 'TV Show')
            plt.bar(Tv_index, Tv_year, color='purple')
            plt.title('Content Added Over The Years On Netflix')
            plt.xlabel('Years')
            plt.ylabel('Number Of Movies')
            plt.legend(labels=['Movie', 'TV Show'])
            if save.__eq__('yes'):
                plt.savefig('D:\dataSets\\netflixFigures\content_added_over_years_bar.png')
            plt.show()
        except Exception as e:
            print(e)


cmd = Netflix(welcome)
if __name__ == '__main__':
    global df, col_Name, copy_df, movies, save
    try:
        df = pd.read_csv('D:\dataSets\kaggle\\netflix_titles.csv')
        copy_df = df.copy()
        cmd.readFile(df)
        save = input('Do you want to save the charts ? (yes/no) ')
        cmd.countries_type_on_netflix(copy_df['type'])
        cmd.content_added_over_years(copy_df['release_year'], copy_df['type'])
    except Exception as e:
        print(e)
