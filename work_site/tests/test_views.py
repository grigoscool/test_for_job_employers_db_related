from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_static_urls(self):
        url_temp: dict = {
            '': 'work_site/index.html',
            # '/employers/': 'work_site/employers.html',
            # '/search_result/': 'work_site/search_results.html',
            '/add_employer/': 'work_site/add_employ.html',
        }
        for url, temp in url_temp.items():
            resp = self.client.get(url)
            errors = f'{url} expected {temp}'
            self.assertTemplateUsed(resp, temp, errors)
