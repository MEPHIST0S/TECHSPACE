from extensions import *
from forms import *
from utils import*

from app import app
from models import Category, Product, User, ContactMessage, Review, Subscriber

@app.route('/')
@app.route('/home/')
@app.route('/shop/')
@app.route('/index.html/')
def index():
    search_form = SearchForm()
    categories = Category.query.all()
    products = Product.query.all()

    subcategory_counts = {}

    # LOOKING THROUGH CATEGORIES FOR SUBCATEGORIES
    for category in categories:
        if category.parent_id is not None:
            subcategory_counts[category.name] = 0

    # COUNTING PRODUCTS 
    for product in products:
        if product.category.name in subcategory_counts:
            subcategory_counts[product.category.name] += 1

    # PAGE AND AMOUNT OF PRODUCTS ON IT
    page = request.args.get('page', 1, type=int)
    per_page = 15

    # FILTER AND CATEGORY SELECTION
    selected_category = request.args.get('category')
    search_query = request.args.get('search')

    if selected_category:
        filtered_products = [p for p in products if p.category.name == selected_category]
    else:
        filtered_products = products

    if search_query:
        filtered_products = [p for p in filtered_products if search_query.lower() in p.name.lower()]

    total_products = len(filtered_products)
    total_pages = ceil(total_products / per_page)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_products = filtered_products[start_index:end_index]

    context = {
        'search_form': search_form,
        'categories': categories,
        'filtered_categories': subcategory_counts,
        'products': paginated_products,
        'current_page': page,
        'total_pages': total_pages,
    }
    
    return render_template('index.html', **context)

@app.context_processor
def inject_form_and_categories():
    categories = Category.query.all()
    search_form = SearchForm()
    subscribe_form = SubscribeForm()
    
    return dict(categories=categories, search_form=search_form, subscribe_form=subscribe_form)

@app.route('/category/<int:category_id>')
def category_products(category_id):
    
    form = SearchForm()
    category = Category.query.get_or_404(category_id)
    
    # ALL RELATED PRODUCTS
    products = Product.query.filter_by(category_id=category_id).all()
    
    # COUNTING PRODUCTS FOR EACH SUBCATEGORY
    subcategories = Category.query.filter_by(parent_id=category_id).all()

    context = {
        'form': form,
        'category': category,
        'products': products,
        'subcategories': subcategories
    }

    return render_template('category_products.html', **context)

@app.route('/search', methods=['GET'])
def search_products():
    form = SearchForm()
    products = []
    query = request.args.get('query')

    if query:
        products = Product.query.join(Category, Product.category_id == Category.id).filter(
            Product.name.ilike(f'%{query}%') |
            Category.name.ilike(f'%{query}%')
        ).all()
        
    context = {
        'form': form,
        'products': products,
        'query' : query
    }

    return render_template('search_results.html', **context)

@app.route('/contact.html/')
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Create a new ContactMessage object
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        
        # Save the message to the database
        db.session.add(new_message)
        db.session.commit()
        
        flash('Your message has been sent and saved!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

@app.route('/detail.html/')
@app.route('/detail/')
@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    category_name = product.category.name

    subcategories = Category.query.filter(Category.parent_id.isnot(None)).all()
    target_categories = [subcategory.name for subcategory in subcategories]
    
    if category_name in target_categories:
        similar_products = Product.query.join(Category, Product.category_id == Category.id)\
            .filter(Category.name == category_name)\
            .filter(Product.id != product_id)\
            .order_by(func.random())\
            .limit(4)\
            .all()
    else:
        similar_products = []

    form = ReviewForm()

    if form.validate_on_submit():
        review = Review(
            review_text=form.review_text.data,
            rating=form.rating.data,
            user_id=current_user.id,
            product_id=product.id
        )
        db.session.add(review)
        db.session.commit()
        flash('Ваш отзыв был добавлен!', 'success')
        return redirect(url_for('product_detail', product_id=product.id))

    context = {
        'product': product,
        'similar_products': similar_products,
        'form': form 
    }
    
    return render_template('detail.html', **context)

@app.route('/login.html/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            if user.otp_verified:
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Please verify your email address before logging in.', 'warning')
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/register.html/')
@app.route('/register/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        existing_user = User.query.filter_by(email=register_form.email.data).first()
        if existing_user:
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))

        otp = generate_otp()
        send_otp_email(register_form.email.data, otp)
        print(otp)

        hashed_password = generate_password_hash(register_form.password.data, method='pbkdf2:sha256')
        user = User(username=register_form.username.data, email=register_form.email.data, password=hashed_password, otp=otp)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created. An OTP has been sent to {register_form.email.data}.', 'success')
        return redirect(url_for('verify_otp', user_id=user.id))

    return render_template('register.html', title='Register', form=register_form)

@app.route('/verify_otp/<int:user_id>', methods=['GET', 'POST'])
def verify_otp(user_id):
    user = User.query.get_or_404(user_id)
    form = OTPVerificationForm()
    if form.validate_on_submit():
        otp = form.otp.data
        if otp == user.otp:
            user.otp_verified = True
            db.session.commit()
            flash('Your email has been verified. You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')

    return render_template('verify_otp.html', title='Verify OTP', form=form, user=user)

@app.route('/favorites/')
@login_required
def favorites():
    # LIST OF FAVORITE PRODUCTS OF CURRENT USER
    favorite_products = current_user.favorite_products
    return render_template('favorites.html', products=favorite_products)

@app.route('/remove_from_favorites/<int:product_id>', methods=['POST'])
@login_required
def remove_from_favorites(product_id):
    product = Product.query.get_or_404(product_id)
    if product in current_user.favorite_products:
        current_user.favorite_products.remove(product)
        db.session.commit()
        flash('Product removed from favorites.', 'success')
    else:
        flash('Product not found in favorites.', 'danger')
    return redirect(url_for('favorites'))

@app.route('/add_to_favorites/<int:product_id>', methods=['POST'])
@login_required
def add_to_favorites(product_id):
    
    if not current_user.is_authenticated:
        flash('You need to log in to use this feature.', 'warning')
        return redirect(url_for('login'))

    product = Product.query.get_or_404(product_id)

    if product in current_user.favorite_products:
        flash('This product is already in your favorites.', 'info')
    else:
        current_user.favorite_products.append(product)
        db.session.commit()
        flash('Product added to your favorites.', 'success')

    return redirect(url_for('product_detail', product_id=product.id))

@app.route('/product/<int:product_id>/add_review', methods=['GET', 'POST'])
@login_required
def add_review(product_id):
    product = Product.query.get_or_404(product_id)
    form = ReviewForm()
    
    if form.validate_on_submit():
        review = Review(
            review_text=form.review_text.data,
            rating=form.rating.data,
            product_id=product.id,
            user_id=current_user.id
        )
        db.session.add(review)
        db.session.commit()
        flash('Your review has been added successfully!', 'success')
        return redirect(url_for('product_detail', product_id=product.id))

    return render_template('detail.html', product=product, form=form)

@app.route('/discounted')
def discounted_products():
    discounted_products = Product.query.filter(Product.discounted_price > 0).all()
    return render_template('discounted.html', products=discounted_products)

@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    subscribe_form = SubscribeForm()
    if subscribe_form.validate_on_submit():
        name = subscribe_form.name.data
        email = subscribe_form.email.data

        existing_subscriber = Subscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('You are already subscribed with this email address.', 'warning')
            return redirect(url_for('index'))

        new_subscriber = Subscriber(name=name, email=email)
        db.session.add(new_subscriber)
        db.session.commit()

        flash('Thank you for subscribing!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', subscribe_form=subscribe_form)

#ADMIN
@app.route('/admin/messages', methods=['GET'])
def view_messages():
    # OBSERVING ALL MESSAGES FROM DB
    messages = ContactMessage.query.all()
    
    return render_template('admin/messages.html', messages=messages)