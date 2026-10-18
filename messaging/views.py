from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Max
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import MessageForm
from .models import Conversation

User = get_user_model()


@login_required
def inbox(request):
    conversations = (
        Conversation.objects
        .filter(participants=request.user)
        .annotate(last_message_at=Max("messages__created_at"))
        .order_by("-last_message_at", "-updated_at")
    )
    return render(
        request,
        "messaging/inbox.html",
        {"conversations": conversations},
    )


@login_required
def user_list(request):
    users = User.objects.exclude(pk=request.user.pk).order_by("username")
    return render(request, "messaging/user_list.html", {"users": users})


@login_required
def start_conversation(request, username):
    recipient = get_object_or_404(User, username=username)

    if recipient.pk == request.user.pk:
        return redirect("messaging:inbox")

    existing = (
        Conversation.objects
        .filter(participants=request.user)
        .filter(participants=recipient)
    )

    conversation = None
    for candidate in existing:
        if candidate.participants.count() == 2:
            conversation = candidate
            break

    if conversation is None:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, recipient)

    return redirect(
        "messaging:conversation",
        conversation_id=conversation.pk,
    )


@login_required
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)

    if not conversation.participants.filter(pk=request.user.pk).exists():
        return HttpResponseForbidden(
            "Kamu tidak memiliki akses ke percakapan ini."
        )

    messages = conversation.messages.select_related("sender").all()

    conversation.messages.filter(
        is_read=False,
    ).exclude(
        sender=request.user,
    ).update(is_read=True)

    form = MessageForm()

    return render(
        request,
        "messaging/conversation.html",
        {
            "conversation": conversation,
            "messages": messages,
            "form": form,
        },
    )


@login_required
@require_POST
def send_message(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)

    if not conversation.participants.filter(pk=request.user.pk).exists():
        return HttpResponseForbidden(
            "Kamu tidak memiliki akses ke percakapan ini."
        )

    form = MessageForm(request.POST)

    if form.is_valid():
        message = form.save(commit=False)
        message.conversation = conversation
        message.sender = request.user
        message.save()
        conversation.save()

    return redirect(
        "messaging:conversation",
        conversation_id=conversation.pk,
    )
