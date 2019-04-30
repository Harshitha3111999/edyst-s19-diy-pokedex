from flask import Flask,json,render_template,jsonify,make_response
app= Flask(__name__)
@app.route("/api/pokemon")
def index():
    return "hello"

@app.route("/api/pokemon/<int:id>",methods=["GET"])
def jso(id):   
    k="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
    p=".png"
    q=str(id)
    t=k+q+p
    c = json.loads(open('names.json').read())
    x = json.dumps(c[id-1])
    response_body={
        "pokemon":{
            "id": id,
            "name": x,
            "sprite": t,
        }
    }    
    
    res = make_response(jsonify(response_body), 200)
    return res

if __name__ == '__main__':
    app.run(host='localhost', port=8006, debug=True)