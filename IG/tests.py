from django.test import TestCase
from .models import Profile,Posts,Comments,Following

class  FollowingTestcaseClass(TestCase):
    def setUp(self):
        self .mykey=Following(username='marabel',followed='shanice')


    def test_instance(self):
        sel.assertTrue(isinstance)(self.mykey,Following))


class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1
                           username='mykey',
                           comment='What an aweome memory!'
                           date='Jan 17, 2020 11:07 a.m' ,
                           count=0)

    def tast_instance(self):
        self.assertTrue(isinstance(self.first,Comment))                                  
