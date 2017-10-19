from tornado.web import Application
import views


ROUTES_TORNADOS = Application([
        (r'/web', views.MainWeb),
		(r'/socket', views.MainSocket)

])
