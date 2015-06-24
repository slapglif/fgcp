from flask import Flask

app = Flask(__name__)


@app.route('/')
def gcp():
    output = "gamecp_is_a_small_company_please_dont_rip_us_off_we_work_really_hard"

    return output


if __name__ == '__main__':
    app.run()
