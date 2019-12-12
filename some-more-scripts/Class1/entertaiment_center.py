
import media
import fresh_tomatoes

Toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that come to life', 'https://image.tmdb.org/t/p/w600/uMZqKhT4YA6mqo2yczoznv7IDmv.jpg', 'https://www.youtube.com/watch?v=JcpWXaA2qeg')

#print toy_story.storyline

Avatar = media.Movie('Avatar', 'A marine on an alien planet', 'https://image.tmdb.org/t/p/w600/tcqb9NHdw9SWs2a88KCDD4V8sVR.jpg', 'https://www.youtube.com/watch?v=5PSNL1qE6VY')

#print avatar.storyline

#avatar.show_trailer()

Interstellar = media.Movie('Interstellar', 'A man travels through space and time', 'https://image.tmdb.org/t/p/w600/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg', 'https://www.youtube.com/watch?v=zSWdZVtXT7E')

#interstellar.show_trailer()

Arrival = media.Movie('Arrival', 'Aliens from distant worlds visit Earth to help the human kind', 'https://pbs.twimg.com/media/CySG6SxXcAEQF9Z.jpg', 'https://www.youtube.com/watch?v=tFMo3UJ4B4g')


The_Martian = media.Movie('The Martian', ' An astronaut becomes stranded on Mars', 'http://indianinkonline.com/wp-content/uploads/2015/10/the-martian-600x900.jpeg', 'https://www.youtube.com/watch?v=Ue4PCI0NamI')

Deadpool = media.Movie('Deadpool', 'Deadpool is a fictional antihero appearing in American comic books', 'http://instinctmagazine.com/sites/instinctmagazine.com/files/images/blog_posts/Adam%20Dupuis/2016/09/06/Deadpool-2.jpg', 'https://www.youtube.com/watch?v=9vN6DHB6bJc')

movies = [Toy_story, Avatar, Interstellar, Arrival, The_Martian, Deadpool]

#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.valid_ratings
print media.Movie.__doc__


