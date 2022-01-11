# File we run to start our webserver or website.  

from Website import create_app
from Website import db
app = create_app()

if __name__ == "__main__":  # The next line is executed only if we run this file and not import this file.
    app.run(debug=True)  # Anytime we make a change to our python code, it'll automatically rerun the webserver.

