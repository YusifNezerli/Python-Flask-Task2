from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=False)


movies_list = [{ 'id': 1,
            'name': 'El Camino', 
            'imdb': '7.3', 
            'producer': 'Mark Johnson', 
            'image': 'https://www.indiewire.com/wp-content/uploads/2019/10/El-Camino-Jesse-Netflix.jpg?resize=1024,683',
            'status': 'active'},

            {'id': 2,
            'name': 'La La Land', 
            'imdb': '8.0',            
            'producer': 'Fred Berger', 
            'image': 'https://static01.nyt.com/images/2016/09/19/arts/la-la-land-watching/19TORONTO-jumbo.jpg?quality=75&auto=webp',
            'status': 'active' },

            {'id': 3,
            'name': 'Truman Show', 
            'imdb': '8.2',            
            'producer': 'Scott Rudin', 
            'image': 'https://www.nzherald.co.nz/resizer/0x9wQwogrviXc0QVLSI-AZoWiDM=/1440x810/smart/filters:quality(70)/cloudfront-ap-southeast-2.images.arcpublishing.com/nzme/PF4ROLSNHJHNVTGQS4BJYQ4XSA.jpg',
            'status': 'active'},

            {'id': 4,
            'name': 'Midsommar', 
            'imdb': '7.1',            
            'producer': 'Patrik Andersson', 
            'image': 'https://images.mubicdn.net/images/film/210029/cache-416486-1636971271/image-w1280.jpg?size=800x',
            'status': 'active'},

            {'id': 5,
            'name': 'Intersteller', 
            'imdb': '8.6',            
            'producer': 'Emma Thomas', 
            'image': 'https://media.npr.org/assets/img/2014/11/13/fl-17895r_wide-d745edc663a75ddc961f66684631a621dc148566-s800-c85.webp',
            'status': 'realased' }]

@app.route('/movies')
def movies():
    active_movies_list = [movie for movie in movies_list if movie['status'] == 'active']
    return render_template('movies.html', is_active=True, movies =active_movies_list)


@app.route('/movie/<int:id>')
def movie(id):
    i = [i for i in movies_list if i['id'] == id]
    if i:
        return render_template('movie.html', movie_film = i)
    else:
        return "film movcud deyil"
    







