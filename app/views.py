# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
import json
import jwt

from django.http import (HttpResponse,
                         HttpResponseNotFound,
                         HttpResponseForbidden)

from account.models import User
from django.contrib.auth import (authenticate, login)
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

from .models import (CPF, CpfUsuario, Estacao, EmprestimoAvulso, Familia, Ferramenta, FOE,  Gerencia, GTO, Hangar, Inventario, Kit,
                     LocalCaixaBin, LocalOrigem, MenuSistema, Montagem, MontaKit, Movimento, Notificacao, Pagamento, PagamentoFerramenta,
                     PagamentoFalta, ProcessoEspecial, QuebraFerramenta, SubMenuSistema, Supervisao, Unidade)

from .serializers import (CPFSerializer, EstacaoSerializer, EmprestimoAvulsoSerializer, FamiliaSerializer,
                          FerramentaSerializer, FOESerializer, GerenciaSerializer, GTOSerializer, HangarSerializer,
                          InventarioSerializer, KitSerializer, LocalCaixaBinSerializer, LocalOrigemBinSerializer,
                          MontagemSerializer, MovimentoSerializer, NotificacaoSerializer, SupervisaoSerializer, MontaKitSerializer,
                          PagamentoSerializer, PagamentoFerramentaSerializer, PagamentoFaltaSerializer,
                          ProcessoEspecialSerializer, QuebraFerramentaSerializer, UnidadeSerializer, UserSerializer)


class CPFViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CPF.objects.all()
    serializer_class = CPFSerializer


class EstacaoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Estacao.objects.all()
    serializer_class = EstacaoSerializer


class EmprestimoAvulsoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = EmprestimoAvulso.objects.all()
    serializer_class = EmprestimoAvulsoSerializer


class FamiliaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer


class FerramentaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ferramenta.objects.all()
    serializer_class = FerramentaSerializer


class FOEViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FOE.objects.all()
    serializer_class = FOESerializer


class GerenciaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Gerencia.objects.all()
    serializer_class = GerenciaSerializer


class GTOViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = GTO.objects.all()
    serializer_class = GTOSerializer


class HangarViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hangar.objects.all()
    serializer_class = HangarSerializer


class InventarioViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


class KitViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Kit.objects.all()
    serializer_class = KitSerializer


class LocalCaixaBinViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = LocalCaixaBin.objects.all()
    serializer_class = LocalCaixaBinSerializer


class LocalOrigemViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = LocalOrigem.objects.all()
    serializer_class = LocalOrigemBinSerializer


class MontagemViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Montagem.objects.all()
    serializer_class = MontagemSerializer


class MovimentoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Movimento.objects.all()
    serializer_class = MovimentoSerializer


class MontaKitViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MontaKit.objects.all()
    serializer_class = MontaKitSerializer


class PagamentoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer


class PagamentoFerramentaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PagamentoFerramenta.objects.all()
    serializer_class = PagamentoFerramentaSerializer


class PagamentoFaltaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PagamentoFalta.objects.all()
    serializer_class = PagamentoFaltaSerializer


class ProcessoEspecialViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ProcessoEspecial.objects.all()
    serializer_class = ProcessoEspecialSerializer


class QuebraFerramentaViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = QuebraFerramenta.objects.all()
    serializer_class = QuebraFerramentaSerializer


class UnidadeViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SupervisaoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Supervisao.objects.all()
    serializer_class = SupervisaoSerializer


class NotificacaoViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer


@csrf_exempt
def get_menu(request, pk):

    def fn_menu(mn):

        def fn_sub_menu(sm):
            return {
                'view': sm.view,
                'descricao': sm.descricao,
                'descricao_curta': sm.descricao_curta,
                'url': sm.url
            }

        sub_menu = [fn_sub_menu(sm) for sm in SubMenuSistema.objects.filter(menu=mn.id).order_by('descricao_curta')]

        return {
            'descricao': mn.descricao,
            'icone': mn.icone,
            'itens': sub_menu
        }

    return HttpResponse(json.dumps([fn_menu(mn) for mn in MenuSistema.objects.filter(grupo=pk).order_by('descricao')]),
                        content_type="application/json")
