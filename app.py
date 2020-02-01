import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# below is the database connection which is being looked for within the env.py
app.config["MONGO_DBNAME"] = 'Recipe_Book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    recipes = mongo.db.Recipes.find()
    types = mongo.db.Type.find()
    return render_template("recipes.html", recipes=recipes, types=types)


@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    recipes = mongo.db.Recipes
    types = mongo.db.Type.find()
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    types = mongo.db.Type.find()
    return render_template('editrecipe.html', recipesedit=the_recipe,
                            alltypes=types)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.Recipes
    recipes.update({'_id': ObjectId(recipe_id)}, {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_instructions': request.form.get('recipe_instructions'),
        'date_added': request.form.get('date_added'),
        'recipe_type': request.form.get('recipe_type')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_task/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.Recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)