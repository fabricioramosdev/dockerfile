import json
import jwt
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import (authenticate, login)
from rest_framework_simplejwt.tokens import RefreshToken, Token
from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseForbidden)
from .models import User
from app.models import (CpfUsuario)

from datetime import datetime, time


@csrf_exempt
def go_in(request):

    def cpf_dic(i):
        return {
            'pk': i.pk,
            'descricao': i.cpf.descricao,
        }

    def grupo_dic(i):
        return {
            'pk': i.pk,
            'descricao': i.name,
        }

    def token_dic(i):

        # Faz o decode do token para retornar o timestamp de expiração
        # decode_token = jwt.decode(str(i.access_token), options={"verify_signature": False})

        return {
            'access': str(i.access_token),
            'refresh': str(i),
            # 'exp': decode_token.get('exp')
        }

    if request.method == 'POST':

        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        try:
            user = User.objects.get(email=email)
            # Atualizar a senha do usuário para autentica-lo se o primeiro login
            if user.last_login is None:
                user.set_password(password)

            user.save()
            autenticado = authenticate(email=email, password=password)
            if autenticado is not None:

                # backend authenticated the credentials
                login(request, user)

                # Seleciona o CPF que o usuário faz parte
                cpf = [cpf_dic(k) for k in CpfUsuario.objects.filter(usuario=user)]

                # Seleciona os grupos do usuário
                groups = [grupo_dic(k) for k in user.groups.all()]

                # Pega o token JWT
                refresh = RefreshToken.for_user(user)

                token = token_dic(refresh)
                request.session['logged'] = json.dumps({
                                                'pk': user.pk,
                                                'username': user.username,
                                                'email': user.email,
                                                'first_name': user.first_name,
                                                'last_name': user.last_name,
                                                'employee_registration': user.employee_registration,
                                                'groups': groups,
                                                'cpf': cpf,
                                                'token': token
                })
                return HttpResponse(json.dumps({
                                                'pk': user.pk,
                                                'username': user.username,
                                                'email': user.email,
                                                'first_name': user.first_name,
                                                'last_name': user.last_name,
                                                'employee_registration': user.employee_registration,
                                                'groups': groups,
                                                'cpf': cpf,
                                                'token': token
                }),
                                    content_type="application/json")
            else:
                return HttpResponseForbidden('User not authorized.')

        except Exception as error:
            return HttpResponseNotFound(error)


@csrf_exempt
def change_password(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    try:
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return HttpResponse(json.dumps({'pk': user.pk,
                                        'username': user.username,
                                        'email': user.email,
                                        'first_name': user.first_name,
                                        'last_name': user.last_name,
                                        'employee_registration': user.employee_registration
                                        }), content_type="application/json")
    except Exception as error:
        return HttpResponseNotFound(error)
