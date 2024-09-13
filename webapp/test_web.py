import unittest
import web
from webtest import TestApp  # Cambia esta importación

# Importa tu aplicación
from app import app

class TestIndex(unittest.TestCase):

    def setUp(self):
        # Carga la aplicación web con WebTest
        self.app = TestApp(app.wsgifunc())

    def test_get_index(self):
        # Realiza una petición GET a la ruta '/'
        response = self.app.get('/')
        
        # Verifica que el código de estado HTTP sea 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica que el contenido de la respuesta sea el esperado
        self.assertEqual(response.text, 'Hello docker world!')

if __name__ == '__main__':
    unittest.main(verbosity=2)