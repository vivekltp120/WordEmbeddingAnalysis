import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
os.chdir(os.getcwd())
#set ggplot style
plt.style.use('default')
music_control=['skip','playlist','volume','track','stop','pause','playback','next','previous']
music_control_1=['add','remove','delete','track','songs','song']

email=['email','emails','gmail','gmails','hotmails','outlook','@gmail']
music_play=['play','music']
news=['news','headlines','headline']
weather=['weather','temperature','forecast']
call=['call','voice']
calender=['appointment','event','events','appointments','schedule','meetings','meeting','reminder','reminders']
notification=['notification','notifications']

#get file name
def file_name_with_path(arg):
    fpath = os.path.split(filepath)[0]
    fname = os.path.split(filepath)[1].split('.')[0]
    # print(os.path.join(fpath,fname))
    return os.path.join(fpath,fname)
# plot data
def plot_graph(data,file):
    fig, ax = plt.subplots(figsize=(20, 10))
    data.groupby(['Intent']).count().plot(ax=ax,kind='bar')
    ax.set_xlabel('Intent')
    ax.set_ylabel('Intent Frequency')
    f=file+'.png'
    plt.savefig(f)
    # plt.show()

#save a output in a file
def output_xlsx(data,file):
    writer_orig = pd.ExcelWriter(file+'.xlsx', engine='xlsxwriter')
    data.to_excel(writer_orig, index=False)
    writer_orig.save()


#Label the query with some intent
def label_intent(dfs):
    dfs = pd.read_excel(filepath)
    i=0
    for x in dfs['Query']:
        try:
            o_sent = x.split()
            l_sent = [x.lower() for x in o_sent]
            print(l_sent)
            if set(news) & set(l_sent):
                dfs['Intent'][i] = 'news'
                news_keyword(dfs, i, l_sent)
            elif set(music_play) & set(l_sent):
                dfs['Intent'][i] = 'music_play'
                play_keyword(dfs, i, l_sent)
                # tag_artist(dfs, i, l_sent)
            elif set(music_control) & set(l_sent):
                dfs['Intent'][i] = 'music_classifier'
            elif len(set(music_control_1).intersection(set(l_sent)))>=2:
                dfs['Intent'][i] = 'music_classifier'
            elif 'weather' in l_sent:
                dfs['Intent'][i] = 'weather'
                weather_keyword(dfs, i, l_sent)
            elif set(email) & set(l_sent):
                dfs['Intent'][i] = 'email'
            elif set(call) & set(l_sent):
                dfs['Intent'][i] = 'call'
                call_keyword(dfs, i, l_sent)
            elif set(calender) & set(l_sent):
                dfs['Intent'][i] = 'calender'
                calender_keyword(dfs, i, l_sent)
            elif set(notification) & set(l_sent):
                dfs['Intent'][i] = 'notification'
            else:
                dfs['Intent'][i] = 'generic'
                generic_keyword(dfs, i, l_sent)

            i += 1
        except AttributeError:
            i += 1
            print('AttributeError')
    output_xlsx(dfs,file_name_with_path(filepath))
    plot_graph(dfs,file_name_with_path(filepath))


def tag_artist(dfs, i, l_sent):

    pass


def play_keyword(dfs, i, l_sent):
    if 'play' in l_sent:
        if 'by' in l_sent:
          l_sent.remove('play')
          dfs['keyword'][i] = " ".join(l_sent[:l_sent.index('by')-1])
          dfs['Artist'][i] = " ".join(l_sent[l_sent.index('by')+1:])

def call_keyword(dfs, i, l_sent):
    if 'call' in l_sent:
            dfs['keyword'][i] = " ".join(l_sent[l_sent.index('call')+1:])

def weather_keyword(dfs, i, l_sent):
    if 'weather' in l_sent:
        dfs['keyword'][i] = " ".join(l_sent[l_sent.index('weather')+1:])

def news_keyword(dfs, i, l_sent):
    if 'news' in l_sent:
        dfs['keyword'][i] = " ".join(l_sent[l_sent.index('news') + 1:])

def generic_keyword(dfs, i, l_sent):
        dfs['keyword'][i] = " ".join(l_sent)


def calender_keyword(dfs, i, l_sent):
    if 'calender' in l_sent:
        dfs['keyword'][i] = " ".join(l_sent[l_sent.index('calender')+1:])
# Acquire a sheet by its name
if __name__=='__main__':
    filepath = sys.argv[1]
    label_intent(filepath)














