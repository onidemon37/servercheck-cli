# servercheck-cli
yet another python tutorial.

A python tutorial to from Linux Academy's, `Programming Use Cases with Python` course.

* requirements
Install requirements.txt

  ```
  pip install -r requirements.txt
  pip install -e .
  ```

* Usage

Create a json file, with servers and ports.
  ```
  touch example.json

  [
    "web-node1:80",
    "web-node1:8000",
    "web-node1:3000",
    "web-node2:80",
    "web-node2:3000"
  ]
  ```

Run:
  ```
  servercheck -f example.json -s 'node1:80' -s 'node1:9000'
  ```
