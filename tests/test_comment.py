from app.models import Comment,User
from app import db


def setUp(self):
        self.user_Briankiiru = User(username = 'Briankiiru',password = 'andela', email = 'kimanibrian424@gmail.com')
        self.new_comment = Comment(blog_id=12345,blog_title='comment for blogs',blog_comment='This blog is the best thing since sliced bread',user = self.user_Briankiiru )


def tearDown(self):
        Comment.query.delete()
        User.query.delete()


def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.blog_id,12345)
        self.assertEquals(self.new_comment.blog_title,'Comment for blogs')
        self.assertEquals(self.new_comment.blog_comment,'This blog is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_Briankiiru)


def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comment = Comment.get_comments(12345)
        self.assertTrue(len(got_comment) == 1)