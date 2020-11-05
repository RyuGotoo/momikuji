from django.test import TestCase
from .models import MomikujiModel

# Create your tests here.

class MomikujiModelTests(TestCase):
    def test_draw_momikuji(self):
        # Create dummy data
        for i in range(10):
            text = 'test' + str(i)
            MomikujiModel.objects.create(text=text)

        from random import randint
        all_momikujis = MomikujiModel.objects.all()
        results = []
        for i in range(1000):
            rand_id = randint(1, len(all_momikujis))
            momikuji = MomikujiModel.objects.get(pk=rand_id)
            result = momikuji in all_momikujis
            results.append(result)
        self.assertIs(False in results, False)