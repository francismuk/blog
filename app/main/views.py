from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import Category, Blog, Comment
from .forms import BlogForm, CommentForm, CategoryForm
from flask_login import login_required, current_user
from app.request import get_quote
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    quote = get_quote()
    categories = Category.get_categories()

    return render_template('index.html', title=title, categories=categories, quote=quote)


@main.route('/category/new', methods=['GET', 'POST'])
@login_required
def new_category():
    '''
    View new category route function that returns a page with a form to create a category
    '''

    form = CategoryForm()

    if form.validate_on_submit():
        name = form.name.data
        new_category = Category(name=name)
        new_category.save_category()

        return redirect(url_for('.index'))

    title = 'New Category'
    return render_template('new_category.html', category_form=form, title=title)


@main.route('/category/<int:id>')
def category(id):
    '''
    View category route function that returns a list of pitches in the route and allows a user to create a pitch for the selected route
    '''
    category = Category.query.get(id)

    if category is None:
        abort(404)

    blogs = Blog.get_blogs(id)
    title = f'{category.name} page'

    return render_template('category.html', title=title, category=category, blogs=blogs)


@main.route('/category/blog/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_blog(id):
    '''
    View new blog route function that returns a page with a form to create a pitch for the specified category
    '''

    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    form = BlogForm()

    if form.validate_on_submit():
        blog_content = form.blog_content.data
        new_blog = Blog(blog_content=blog_content,category=category, user=current_user)
        new_blog.save_blog()

        return redirect(url_for('.category', id=category.id))

    title = 'New Blog'
    return render_template('new_blog.html', title=title, blog_form=form)


@main.route('/blog/<int:id>')
def single_blog(id):
    '''
    View single blog function that returns a page containing a pitch, its comments and votes
    '''
    blog = Blog.query.get(id)

    if blog is None:
        abort(404)

    comments = Comment.get_comments(id)

    title = f'Blog {blog.id}'

    return render_template('blog.html', title=title, blog=blog, comments=comments)


@main.route('/blog/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    View new blog route function that returns a page with a form to create a pitch for the specified category
    '''
    blog = Blog.query.filter_by(id=id).first()

    if blog is None:
        abort(404)

    form = CommentForm()

    if form.validate_on_submit():
        comment_content = form.comment_content.data
        new_comment = Comment(comment_content=comment_content,
                              blog=blog, user=current_user)
        new_comment.save_comment()

        return redirect(url_for('.single_blog', id=blog.id))

    title = 'New Comment'
    return render_template('new_comment.html', title=title, comment_form=form)
