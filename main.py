from flask import Flask
from func import get_all, get_by_pk, get_by_skill

app = Flask(__name__)
if __name__ == '__main__':

    @app.route("/")
    def page_index():
        return f'<pre> \n{"".join(get_all())}\n</pre>'


    @app.route("/candidates/<int:x>")
    def page_candidates(x):
        return get_by_pk(x)


    @app.route("/skills/<x>")
    def page_skills(x):
        return f'<pre> \n{"".join(get_by_skill(x))}\n</pre>'

app.run()
