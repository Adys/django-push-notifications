from unittest import mock

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from firebase_admin.messaging import Message

from push_notifications.gcm import dict_to_fcm_message, send_message

from .responses import FCM_SUCCESS


class GCMPushPayloadTest(TestCase):

	def test_fcm_push_payload(self):
		with mock.patch("firebase_admin.messaging.send_all", return_value=FCM_SUCCESS) as p:
			message = dict_to_fcm_message({"message": "Hello world"})

			send_message("abc", message)

			# one call
			self.assertEqual(len(p.mock_calls), 1)
			call = p.mock_calls[0]

			# only messages is args, dry_run and app are in kwargs
			self.assertEqual(len(call.args), 1)

			self.assertTrue("dry_run" in call.kwargs)
			self.assertFalse(call.kwargs["dry_run"])
			self.assertTrue("app" in call.kwargs)
			self.assertIsNone(call.kwargs["app"])

			# only one message
			self.assertEqual(len(call.args[0]), 1)

			message = call.args[0][0]
			self.assertIsInstance(message, Message)
			self.assertEqual(message.token, "abc")
			self.assertEqual(message.android.notification.body, "Hello world")

	def test_fcm_push_payload_many(self):
		with mock.patch("firebase_admin.messaging.send_all", return_value=FCM_SUCCESS) as p:
			message = dict_to_fcm_message({"message": "Hello world"})

			send_message(["abc", "123"], message)

			# one call
			self.assertEqual(len(p.mock_calls), 1)
			call = p.mock_calls[0]

			# only messages is args, dry_run and app are in kwargs
			self.assertEqual(len(call.args), 1)
			messages_arg = call.args[0]

			self.assertTrue("dry_run" in call.kwargs)
			self.assertFalse(call.kwargs["dry_run"])
			self.assertTrue("app" in call.kwargs)
			self.assertIsNone(call.kwargs["app"])

			# two message
			self.assertEqual(len(messages_arg), 2)

			message_one = messages_arg[0]
			self.assertIsInstance(message_one, Message)
			self.assertEqual(message_one.token, "abc")
			self.assertEqual(message_one.android.notification.body, "Hello world")

			message_two = messages_arg[1]
			self.assertIsInstance(message_two, Message)
			self.assertEqual( message_two.token,"123")
			self.assertEqual( message_two.android.notification.body, "Hello world")

	def test_push_payload_with_app_id(self):
		with self.assertRaises(ImproperlyConfigured) as ic:
			send_message("abc", {"message": "Hello world"}, application_id="test")

		self.assertEqual(
			str(ic.exception),
			("LegacySettings does not support application_id. To enable "
			 "multiple application support, use push_notifications.conf.AppSettings.")
		)
