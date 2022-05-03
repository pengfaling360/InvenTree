""" Unit tests for scheduled tasks"""

from django.test import TestCase

from plugin import registry


class ScheduledTaskPluginTests(TestCase):
    """ Tests for ScheduledTaskPlugin """

    def test_function(self):
        """check if the scheduling works"""
        # The plugin should be defined
        self.assertIn('schedule', registry.plugins)
        plg = registry.plugins['schedule']
        self.assertTrue(plg)

        # check that the built-in function is running
        plg.member_func()

        # check that the tasks are defined
        self.assertEqual(plg.get_task_names(), ['plugin.schedule.member', 'plugin.schedule.hello', 'plugin.schedule.world'])

        # register
        plg.register_tasks()
        # check that schedule was registers
        from django_q.models import Schedule
        scheduled_plugin_tasks = Schedule.objects.filter(name__istartswith="plugin.")
        self.assertEqual(len(scheduled_plugin_tasks), 3)
