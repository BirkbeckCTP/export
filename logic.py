import zipfile
import os
import uuid

from django.template.loader import render_to_string


from core import files, models as core_models


def export_csv(request, article, article_files):
    pass


def export_html(request, article, article_files):
    html_file_path = files.create_temp_file(
        render_to_string(
            'export/export.html',
            context = {
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

    zip_file_name = 'export_{}_{}.zip'.format(article.journal.code, article.pk)
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
