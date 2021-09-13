import zipfile
import os
import uuid
import csv

from bs4 import BeautifulSoup

from django.template.loader import render_to_string
from django.utils import translation
from django.conf import settings

from core import files, models as core_models


def html_table_to_csv(html):
    filepath = files.get_temp_file_path_from_name(
        '{0}.csv'.format(uuid.uuid4())
    )
    soup = BeautifulSoup(str(html), 'lxml')
    with open(filepath, "w", encoding="utf-8") as f:
        wr = csv.writer(f)
        for table in soup.find_all("table"):
            for row in table.find_all("tr"):
                cells = [cell.string for cell in row.findChildren(['th', 'td'])]
                wr.writerow(cells)
            wr.writerow([])

    f.close()
    return filepath


def export_csv(request, article, article_files):
    elements = [
        'general.html',
        'authors.html',
        'files.html',
        'dates.html',
        'funding.html',
    ]

    context = {
        'article': article,
        'journal': request.journal,
        'files': article_files,
    }

    html = ''
    for element in elements:
        html = html + render_to_string(
            'export/elements/{element}'.format(element=element),
            context,
        )
    csv_file_path = html_table_to_csv(html)

    zip_file_name = 'export_{}_{}_csv.zip'.format(article.journal.code, article.pk)
    zip_path = os.path.join(files.TEMP_DIR, zip_file_name)
    zip_file = zipfile.ZipFile(zip_path, mode='w')

    zip_file.write(
        csv_file_path,
        'article_data.csv'
    )

    for file in article_files:
        zip_file.write(
            file.self_article_path(),
            file.original_filename,
        )

    zip_file.close()

    return files.serve_temp_file(zip_path, zip_file_name)


def export_html(request, article, article_files):
    with translation.override(settings.LANGUAGE_CODE):
        html_file_path = files.create_temp_file(
            render_to_string(
                'export/export.html',
                context={
                    'article': article,
                    'journal': request.journal,
                    'files': article_files,
                }
            ),
            '{code}-{pk}.html'.format(
                code=article.journal.code,
                pk=article.pk,
            )
        )

    zip_file_name = 'export_{}_{}_html.zip'.format(article.journal.code, article.pk)
    zip_path = os.path.join(files.TEMP_DIR, zip_file_name)
    zip_file = zipfile.ZipFile(zip_path, mode='w')
    zip_file.write(
        html_file_path,
        'article_data.html'
    )

    for file in article_files:
        zip_file.write(
            file.self_article_path(),
            file.original_filename,
        )

    zip_file.close()

    return files.serve_temp_file(zip_path, zip_file_name)
