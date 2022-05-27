from django.shortcuts import redirect, render
from django.contrib import messages
from email_validator import validate_email, EmailNotValidError

from .forms import AddEmailForm, AddEmailToGroupForm, AddEmailGroupToRecipientListForm, UploadFileForm
from .models import EmailList

# Create your views here.

import chardet
from pprint import pprint


def check_email(email):
    try:
        # Validate & take the normalized form of the email
        # address for all logic beyond this point (especially
        # before going to a database query where equality
        # does not take into account normalization).
        email = validate_email(email).email
        return "valid"
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return str(e)


def index(request):
    context = {}
    return render(request, "home.html", context)


def upload_file(request):
    validate_error = []

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["file"]
            file_read = file.read()
            rs = chardet.detect(file_read)
            file_encoding = rs['encoding']

            try:
                if "UTF" in file_encoding:
                    print(f"utf-detect: {file_encoding}")
                    file_content = file_read.decode(file_encoding)
                else:
                    print(f'none-utf-detet: {file_encoding}')
                    file_content = file_read.decode('iso-8859-1')
            except Exception as e:
                messages.error(request, f"Error invalid fileType: {e}")
                return redirect("upload_file")

        else:
            print(f"erors: {form.errors.as_data}")
            file = None

        # validate email format
        # print("-"*100)

        lines = file_content.split("\r\n")
        lines = [i for i in lines if i]

        for idx, line in enumerate(lines):
            check = check_email(line)
            if check != "valid":
                payload = {
                    "line": idx,
                    "error": check,
                    "email": line
                }
                validate_error.append(payload)
            
            # print(f"line: {idx} - data: {line}")
        
        # pprint(validate_error)

        if not validate_error:
            validate_error = None

        context = {
            "form": form,
            "data": validate_error,
            "file_name": file.name,
            "file_encode": file_encoding
        }

        # return redirect("upload_file")
        messages.info(request, "check success")
        return render(request, "upload_file.html", context)

    # request.GET
    else:
        form = UploadFileForm()

    context = {
        "form": form,
        "data": None
    }

    return render(request, "upload_file.html", context)


def add_email(request):

    email_list = EmailList.objects.all()

    if request.method == "POST":
        add_email_form = AddEmailForm(request.POST)
        if add_email_form.is_valid():
            print(add_email_form.cleaned_data)
            add_email_form.save()
            return redirect("add_email")
        else:
            messages.error(request, add_email_form.errors)
            return redirect("add_email")

    add_email_form = AddEmailForm()

    context = {
        "form": add_email_form,
        "data": email_list
    }

    return render(request, "add_email.html", context)


def add_email_to_group(request):
    add_mail_to_group_form = AddEmailToGroupForm()
    context = {
        "form": add_mail_to_group_form
    }
    return render(request, "add_email_to_group.html", context)
