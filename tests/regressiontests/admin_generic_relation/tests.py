from django.contrib.admin.util import NestedObjects
from django.db import router
from django.test import TestCase

from models import ModelB


class NestedObjectsTests(TestCase):
    def test_generic_relations(self):
        """NestedObjects collector should work with generic relations."""
        # Create related objects
        b = ModelB.objects.create()
        a = b.model_a.create()

        # Collect them for display using NestedObjects
        using = router.db_for_write(ModelB)
        collector = NestedObjects(using=using)
        collector.collect([b])
        assert a in collector.edges[None]
        assert b in collector.edges[None]
