import os
basedir = os.path.abspath(os.path.dirname(__file__))

def temp_func(user_url):
    #to-do
    classification = 1
    heatmap_url=basedir+"/temp_heatmap/"+"imed.png"
    return classification,heatmap_url

def class_transf(class_int):
    classification="?"
    if(class_int==1):
        classification="Cataract"
    return classification