import re
from django.conf import settings
from django.db.models import Q
from notifications.utils import format_address, send_template_mail, send_template_sms
from users.models import User

def send_mail(sender, receiver, template_name, context):
	context['sender'] = sender
	context['receiver'] = receiver
	sender = settings.USER_ISSUE_SENDER.format(sender.profile.name)
	receiver = format_address(receiver.profile.name, receiver.email)
	return send_template_mail(sender, receiver, template_name, context)

def send_sms(sender, receiver, template_name, context):
	context['sender'] = sender
	context['receiver'] = receiver
	return send_template_sms('', receiver.profile.phone, template_name, context)

def filter_mentions(content):
	mention_tokens = set(re.findall(u'(?<=@)[0-9A-Za-z\u3400-\u9fff\uf900-\ufaff_\\-]+', content))
	mentions = []
	for mention in mention_tokens:
		mentionee = User.objects.filter(Q(username__istartswith=mention) | Q(profile__display_name__iexact=mention)).first()
		if mentionee:
			mentions.append(mentionee)
	return mentions

def is_issue_urgent(issue):
	# Label 1 stands for urgent in current staff system
	return issue.labels.filter(id=1).exists()
