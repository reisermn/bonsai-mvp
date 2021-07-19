"""Non-login required, informational pages"""
from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
    request,
    jsonify,
    url_for,
    flash,
)
from flask_login import login_user, logout_user
from app.extensions import login_manager
from app.models import User, Company
# from .forms import LoginForm, RegisterForm


# Blueprint Configuration
about_bp = Blueprint(
    "about_bp", __name__, template_folder="templates", static_folder="../static"
)


@login_manager.user_loader
def load_user(_id):
    return User.objects(pk=_id).first()
    # return mongo_col_user.find_one({"_id": "user_id"})


@about_bp.route("/", methods=["GET", "POST"])
def home():
    """Homepage"""

    return render_template(
        "index.jinja2",
        page_title="Bonsai",
    )


@about_bp.route("/about", methods=["GET", "POST"])
def about():
    """About / How it works page"""

    return render_template(
        "about.jinja2",
        page_title="How It Works",
    )


@about_bp.route("/team", methods=["GET", "POST"])
def team():
    """Team page"""

    return render_template(
        "team.jinja2",
        page_title="Our Team",
    )


@about_bp.route("/blog", methods=["GET", "POST"])
def blog():
    """Blog page"""

    return render_template(
        "blog.jinja2",
        page_title="Blog",
    )


@about_bp.route("/register", methods=["GET", "POST"])
def register():
    """Register page"""
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        # return '<h1>the name is {}. The email is {}'.format(form.name.data, form.email.data)
        # Convert form data to python vars
        name = register_form.name.data
        email = register_form.email.data
        password = register_form.password.data
        company_name = register_form.company_name.data

        # Create MongoDB record
        mongo_col_user.insert_one(
            {
                "name": name,
                "email": email,
                "password": password,
                "company_name": company_name,
             }
        )
        flash("Thanks, " + name + ". You can now log in.", 'success')
        return redirect(url_for("about_bp.login"))
    return render_template(
        "register.jinja2",
        page_title="Register",
        form=register_form,
    )


@about_bp.route("/login", methods=["GET", "POST"])
def login():
    """Login page"""
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            user = User.objects(email=login_form.email.data).first()
            # return '<h1>The email is {}'.format(user_email)
            login_user(user)
            flash("Welcome back, " + user.name, 'success')
            return redirect(url_for("about_bp.home"))
        else:
            flash("Invalid email or password. Please try again.", 'error')
            return redirect(url_for("about_bp.login"))
    return render_template(
        "login.jinja2",
        page_title="Login",
        form=login_form,
    )

@about_bp.route("/logout", methods=["GET", "POST"])
def logout():
    """Logout page"""
    logout_user()
    flash("You've been successfully logged out", 'info')
    return redirect(url_for("about_bp.home"))