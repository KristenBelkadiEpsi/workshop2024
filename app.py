from detoxify import Detoxify
import pandas as pd
from flask import Flask, request, make_response

model = Detoxify("multilingual")
toxicity_limit = 0.6
app = Flask(__name__)


@app.route("/eval-toxicity", methods=["POST"])
def eval():
    json = request.json
    if json is None:
        return make_response(404)
    else:
        text = json["text"]
        if text is None:
            return make_response(404)
        else:
            predict = model.predict([text])
            data_frame = pd.DataFrame(predict).round(5)
            result = bool(data_frame["toxicity"][0] >= toxicity_limit)
            print(result)
            response = {"is_toxic": result}
            return make_response(response, 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
