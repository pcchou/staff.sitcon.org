from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.forms.models import modelform_factory
from django.shortcuts import redirect
from submission.models import Submission

@login_required
def edit(request, submission_id):
	instance = get_object_or_404(Submission, id=submission_id, user=request.user)

	if request.POST.get('submit'):
		SubmissionForm = modelform_factory(Submission, fields='__all__', exclude=('status', 'type'))
		submission = SubmissionForm(request.POST, instance=instance)

		if submission.is_valid():
			submission.save()
			return redirect('submission:list')
		else:
			# Todo : return and display error messages
			pass

	context = {
			'user': request.user,
			'rule': render_document(Node(nid=settings.SUBMISSION_RULE_DOCID).model.current_revision.text.text)
			'submission': instance,
			}

	return render(request, 'submission/edit.html', context)

# vim: noet ts=8 sw=8