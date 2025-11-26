#Ali kianoosh  40220863


#dar sorat niaz be srap cardan site do tabe comment shode dar akhar file ra az comment dar avarid.

import json
from bs4 import BeautifulSoup
import requests
import numpy as np
import re
from numpy.linalg import norm



def get_movies_details():
    url = "https://www.imdb.com/chart/top/"
    headers = {"User-Agent": "PostmanRuntime/7.32.3"}
    request_result = requests.get(url, headers=headers)


    scrap = BeautifulSoup(request_result.text, 'html.parser')
    movies_name_summary_href = scrap.find_all('a', attrs={'class':'ipc-title-link-wrapper'}, href=True)
    movie_dict = {}
    with open('movie_details.json', 'w+') as f:
        for movie in movies_name_summary_href:
            if movie.string:
                movie_id , moive_title = int(movie.string.split()[0][:-1]), ' '.join(movie.string.split()[1:])
                movie_dict[movie_id] = {'title': moive_title, 'href': movie['href']}
        json.dump(movie_dict, f, indent = 3)
    return movie_dict

def get_movies_summery():
    headers = {"User-Agent": "PostmanRuntime/7.32.3"}

    with open('movie_details.json', 'r+') as file:
        movie_detail = json.load(file)
        new_dict = {}
        for movie_id in movie_detail:
            temp_dict = {}
            summery_page_url = 'https://www.imdb.com/' + '/'.join((movie_detail[movie_id]['href'].split('/'))[1:3])+ '/plotsummary/?ref_=tt_stry_pl'
            request_result = requests.get(summery_page_url, headers=headers)

            scrap = BeautifulSoup(request_result.text, 'html.parser')
            section_sumeries = scrap.find_all('section', attrs={'class': 'ipc-page-section ipc-page-section--base'})
            outer_div = section_sumeries[0].find_all('div', attrs={'class': 'ipc-html-content-inner-div'})
            all_cleaned_summeries, count = {}, 1
            for i in outer_div:
                inner_div = i.find('div', attrs={'class': 'ipc-html-content-inner-div'})
                if inner_div:
                    only_alphabetical_text = re.findall('[a-zA-z]+', inner_div.get_text().lower())
                    cleaned = re.sub(r'\b(?:and|a|an|the|of|by)\b', '', ' '.join(only_alphabetical_text))
                    all_cleaned_summeries[count] = cleaned
                    count += 1  
            temp_dict['title'] = movie_detail[movie_id]['title']
            temp_dict['summery_href'] = summery_page_url
            temp_dict['full_summery'] = " ".join(all_cleaned_summeries.values()).split()
            new_dict[movie_id] = temp_dict
            print(movie_id)

    with open('movie_details.json', 'w') as f:
        json.dump(new_dict, f, indent=3)

def full_terms_D():
    
    with open('movie_details.json', 'r+') as f:
        full_terms = {}
        mov_detail = json.load(f)
        for id in mov_detail:
            for term in mov_detail[id]['full_summery']:
                if term not in full_terms:
                    full_terms[term] = 0
        return full_terms


def TF_IDF():
    
    with open('movie_details.json', 'r+') as f:
        while True:
            knn_matrix1 = np.empty((len(full_terms_D().keys())+1, 250), dtype=float)
            movies_details = json.load(f)
            tf_idfs = {}
            
            for id in movies_details:
                temp_list = [float(id)]
                all_term = full_terms_D()
                for term in movies_details[id]['full_summery']:
                    
                    tf = movies_details[id]['full_summery'].count(term)/len(movies_details[id]['full_summery'])
                
                    idf = len([1 for id in movies_details if term in movies_details[id]['full_summery']])
                    all_term[term] = tf*(np.log10(250/idf) + 1)

                for tfidf in all_term.values():
                    temp_list.append(float(tfidf))
                temp_array = np.array(temp_list).reshape((len(full_terms_D())+1, ))
                knn_matrix1[:, int(id)-1] = temp_array
            if id == '250':
                break
        return knn_matrix1

def summry_input():

    summery_input = re.findall('[a-zA-z]+', input('your summery : ... ').lower())
    summery_cleaned_input = re.sub(r'\b(?:and|a|an|the|of|by)\b', '', ' '.join(summery_input))
    summry_list = [251]
    input_usser = summery_cleaned_input.split() 
    all_term = full_terms_D()
    with open('movie_details.json', 'r+') as f:
        movie_details = json.load(f)
        for term in input_usser:
            tf = input_usser.count(term) / len(input_usser)
            documents_term = [1 for id in movie_details if term in movie_details[id]['full_summery']]
            if len(documents_term):
                idf = np.log10(250/len(documents_term)) + 1
                if term in all_term:
                    all_term[term] = tf*idf
    return np.array([val for val in all_term.values()])




def Knn_model():
    user_input = summry_input() 
    data_matrix = TF_IDF()
    cosine = {}
    for movie in range(250):
        movie_tfidf = data_matrix[1:, movie]
        cosine[movie+1] = np.dot(movie_tfidf, user_input) / (norm(movie_tfidf)*norm(user_input))
    with open('movie_details.json', 'r') as f:
        movies = json.load(f)
        movie_id = sorted(cosine.items(), key=lambda x: x[1])[-5:]
        for id in reversed(movie_id):
            if str(id[1]) != str(np.nan):
                print(movies[str(id[0])]['title'])
        if str(movie_id[-1][1]) == str(np.nan):
            print('cant find similar movie')



#get_movies_details()
#get_movies_summery()

Knn_model()


