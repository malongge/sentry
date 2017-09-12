from __future__ import absolute_import

from sentry.similarity.backends.abstract import AbstractIndexBackend
from sentry.utils.metrics import timer


class MetricsWrapper(AbstractIndexBackend):
    def __init__(self, backend, template='similarity.{}'):
        self.backend = backend
        self.template = template

    def __getattr__(self, name):
        return getattr(self, name)

    def __timer(self, name, scope):
        return timer(
            self.template.format(name),
            tags={'scope': scope},
        )

    def record(self, scope, *args, **kwargs):
        with self.__timer('record', scope):
            return super(MetricsWrapper, self).record(scope, *args, **kwargs)

    def classify(self, scope, *args, **kwargs):
        with self.__timer('classify', scope):
            return super(MetricsWrapper, self).classify(scope, *args, **kwargs)

    def compare(self, scope, *args, **kwargs):
        with self.__timer('compare', scope):
            return super(MetricsWrapper, self).compare(scope, *args, **kwargs)

    def merge(self, scope, *args, **kwargs):
        with self.__timer('merge', scope):
            return super(MetricsWrapper, self).merge(scope, *args, **kwargs)

    def delete(self, scope, *args, **kwargs):
        with self.__timer('delete', scope):
            return super(MetricsWrapper, self).delete(scope, *args, **kwargs)

    def scan(self, scope, *args, **kwargs):
        with self.__timer('scan', scope):
            return super(MetricsWrapper, self).scan(scope, *args, **kwargs)

    def flush(self, scope, *args, **kwargs):
        with self.__timer('flush', scope):
            return super(MetricsWrapper, self).flush(scope, *args, **kwargs)

    def export(self, scope, *args, **kwargs):
        with self.__timer('export', scope):
            return super(MetricsWrapper, self).export(scope, *args, **kwargs)

    def import_(self, scope, *args, **kwargs):
        with self.__timer('import', scope):
            return super(MetricsWrapper, self).import_(scope, *args, **kwargs)
