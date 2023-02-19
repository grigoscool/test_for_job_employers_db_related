from django.core.exceptions import ValidationError
from django.test import TestCase

from work_site.models import Director


class ValidationTestCase(TestCase):
    def test_is_valid_fio(self):
        dir = Director(fio='Mark Avreliy Crass')
        self.assertRaises(ValidationError, dir.full_clean)
