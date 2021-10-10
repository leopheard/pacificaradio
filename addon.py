from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL0 = "https://kpfa.org/program/the-pacifica-evening-news-weekdays/feed/" #PACIFICA_EVENING_NEWS_WEEKDAY
URL8 = "https://kpfa.org/program/the-kpfa-evening-news-weekend/feed/" #WEEKEND
URL1 = "http://streams.kpfa.org:8000/kpfa" #KPFA_BERKELEY #KPFA http://stream.kpfa.org:8000/kpfa.m3u
URL2 = "http://ic1.sslstream.com/kpfk-fm.mp3" #KPFK
URL3 = "http://www.wpfwfm.org:8000/wpfw_128" #WPFW_DC
URL4 = "http://streams.pacifica.org:9000/wbai_128" #WBAI_NY
URL5 = "http://kpft.org:8000/live_64" #KPFT_HOUSTON
URL6 = "https://rss.castbox.fm/everest/b088b9187e4b4295acb3c6be052c1083.xml" #ARCHIVES
URL7 = "https://fromthevaultradio.org/home/category/uncategorized/feed/" #UNCATEGORIZED

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes0'),
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/0.jpg?raw=true"},
        {
            'label': plugin.get_string(30008), 
            'path': plugin.url_for('all_episodes8'),
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/8.jpg?raw=true"},
   {
            'label': plugin.get_string(30001), 
            'path': "https://streams.kpfa.org:8000/kpfa",
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/1.jpg?raw=true",
            'is_playable': True},
   {
            'label': plugin.get_string(30002), 
            'path': "https://ic1.sslstream.com/kpfk-fm.mp3",
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/2.jpg?raw=true",
            'is_playable': True},
   {
            'label': plugin.get_string(30003), 
            'path': "https://www.wpfwfm.org:8000/wpfw_128",
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/3.jpg?raw=true",
            'is_playable': True},
   {
            'label': plugin.get_string(30004), 
            'path': "https://streams.pacifica.org:9000/wbai_128",
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/4.jpg?raw=true",
            'is_playable': True},
   {
            'label': plugin.get_string(30005), 
            'path': "https://kpft.org:8000/live_64",
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/5.jpg?raw=true",
            'is_playable': True},
        {
            'label': plugin.get_string(30006), 
            'path': plugin.url_for('archive_episodes'),
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/6.jpg?raw=true"},
        {
            'label': plugin.get_string(30007), 
            'path': plugin.url_for('uncategorized_episodes'),
            'thumbnail': "https://github.com/leopheard/pacificaradio/blob/master/resources/media/7.jpg?raw=true"},
    ]
    return items

@plugin.route('/all_episodes0/')
def all_episodes0():
    soup0 = mainaddon.get_soup0(URL0)
    playable_podcast0 = mainaddon.get_playable_podcast0(soup0)
    items = mainaddon.compile_playable_podcast0(playable_podcast0)
    return items
@plugin.route('/archive_episodes/')
def archive_episodes():
    soup6 = mainaddon.get_soup6(URL6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/uncategorized_episodes/')
def uncategorized_episodes():
    soup7 = mainaddon.get_soup7(URL7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/all_episodes8/')
def all_episodes8():
    soup8 = mainaddon.get_soup8(URL8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
if __name__ == '__main__':
    plugin.run()
