from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name
from flask import Flask, render_template

PATH = 'candidates.json'
candidates = load_candidates_from_json(PATH)
app = Flask(__name__)


@app.route("/")
def get_all_users():
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:x>")
def get_by_id(x):
    item = get_candidate(x, PATH)
    if item:
        return render_template('card.html', item=item)
    return "Not Found :("


@app.route("/search/<candidate_name>")
def get_by_name(candidate_name):
    items = get_candidates_by_name(candidate_name, PATH)
    if items:
        return render_template('search.html', candidates=items)
    return "Not Found :("


@app.route("/skill/<skill_name>")
def get_by_skill(skill_name):
    items = get_candidates_by_skill(skill_name, PATH)
    if items:
        return render_template('skill.html', skill=skill_name, candidates=items)
    return "Not Found :("


app.run()




