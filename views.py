from django.shortcuts import render, get_object_or_404
from django.http import Http404

from plugins.export import forms, plugin_settings, logic
from submission import models
from security import decorators
from core import models as core_models


@decorators.has_journal
@decorators.editor_user_required
def manager(request):
    """
    A view for managing the export plugin.
    :param request: HttpRequest object
    :return: HttpReponse or HttpRedirect
    """
    template = 'export/manager.html'
    context = {
    }

    return render(request, template, context)


@decorators.has_journal
@decorators.editor_user_required
def export_articles(request):
    """
    A view that presents a list of articles in this stage.
    :param request: HttpRequest
    :return: HttpReponse
    """
    articles_in_stage = models.Article.objects.filter(
        journal=request.journal,
        stage=plugin_settings.STAGE,
    )

    template = 'export/articles.html'
    context = {
        'articles_in_stage': articles_in_stage,
    }

    return render(request, template, context)


@decorators.has_journal
@decorators.editor_user_required
def export_article(request, article_id, format='csv'):
    """
    A view that exports either a CSV or HTML representation of an article.
    :param request: HttpRequest object
    :param article_id: Article object PK
    :param format: string, csv or html
    :return: HttpResponse or Http404
    """
    in_stage = request.GET.get('in_stage', 'true')
    if in_stage == 'true':
        article = get_object_or_404(
            models.Article,
            pk=article_id,
            journal=request.journal,
            stage=plugin_settings.STAGE,
        )
    else:
        article = get_object_or_404(
            models.Article,
            pk=article_id,
            journal=request.journal,
        )
    files = core_models.File.objects.filter(
        article_id=article.pk,
    )

    if request.GET.get('action') == 'output_html':
        context = {
            'article': article,
            'journal': request.journal,
            'files': files,
        }

        return render(
            request,
            'export/export.html',
            context,
        )

    if format == 'csv':
        return logic.export_csv(request, article, files)
    elif format == 'html':
        return logic.export_html(request, article, files)

    raise Http404


@decorators.has_journal
@decorators.editor_user_required
def export_articles_all(request):
    """
    A view that displays all articles in a journal and allows export.
    """
    articles = models.Article.objects.filter(
        journal=request.journal,
    ).select_related(
        'correspondence_author',
    )

    template = 'export/articles_all.html'
    context = {
        'articles_in_stage': articles,
    }

    return render(request, template, context)
