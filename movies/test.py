from django.test import TestCase
from movies.models import Movie


class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="lion", genre="roar", year=2009, creator_id=1)

    def test_movie_created(self):
        movie = Movie.objects.filter(title="lion")
        self.assertTrue(movie.exists())
