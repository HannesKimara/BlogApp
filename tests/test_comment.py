import unittest
from app.models import User, Blog, Comment
from app import db

class CommentModelTest(unittest.TestCase):
    """
    Test Case to test functionality of Comment Model
    """

    def setUp(self):
        """
        setUp method initializes all our objects before tests
        """
        self.new_user = User(username = "test_user", email = "testuser@mail.com", password = "testpass")
        self.new_blog = Blog(content = "Test Blog Content", user = self.new_user)
        self.new_comment = Comment(content = "very beliavable comment", blog = self.new_blog, user = self.new_user)

    def test_save_comment(self):
        """
        test_save_comment method to test if save method works
        """
        self.comment_save_id = self.new_comment.save()
        self.assertTrue(self.comment_save_id)

    def tearDown(self):
        """
        tearDown class to run after every test
        """
        db.session.delete(self.new_comment)
        db.session.delete(self.new_blog)
        db.session.delete(self.new_user)
        db.session.commit()
