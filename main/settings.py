import flask

main_app = flask.Flask(
    import_name= "settings",
    template_folder = "template",
    static_folder = "static",
    static_url_path = "/main/"

)