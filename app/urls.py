from django.urls import path
from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import (
    CPFViewSets,
    EstacaoViewSets,
    EmprestimoAvulsoViewSets,
    FamiliaViewSets,
    FerramentaViewSets,
    FOEViewSets,
    GerenciaViewSets,
    GTOViewSets,
    HangarViewSets,
    InventarioViewSets,
    KitViewSets,
    LocalCaixaBinViewSets,
    LocalOrigemViewSets,
    MontagemViewSets,
    MovimentoViewSets,
    MontaKitViewSets,
    NotificacaoViewSets,
    PagamentoViewSets,
    PagamentoFerramentaViewSets,
    PagamentoFaltaViewSets,
    ProcessoEspecialViewSets,
    QuebraFerramentaViewSets,
    UnidadeViewSets,
    UserViewSet,
    SupervisaoViewSets,
    # ----------------
    get_menu
)


router = SimpleRouter()
router.register('cpf', CPFViewSets)
router.register('estacao', EstacaoViewSets)
router.register('emprestimo', EmprestimoAvulsoViewSets)
router.register('familia', FamiliaViewSets)
router.register('ferramenta', FerramentaViewSets)
router.register('foe', FOEViewSets)
router.register('gerencia', GerenciaViewSets)
router.register('gto', GTOViewSets)
router.register('hangar', HangarViewSets)
router.register('inventario', InventarioViewSets)
router.register('kit', KitViewSets)
router.register('bin', LocalCaixaBinViewSets)
router.register('local_origem', LocalOrigemViewSets)
router.register('montagem', MontagemViewSets)
router.register('movimento', MovimentoViewSets)
router.register('monta_kit', MontaKitViewSets)
router.register('notificacao', NotificacaoViewSets)
router.register('pgto', PagamentoViewSets)
router.register('pgto_ferramenta', PagamentoFerramentaViewSets)
router.register('pgto_falta', PagamentoFaltaViewSets)
router.register('processo_especial', ProcessoEspecialViewSets)
router.register('quebra', QuebraFerramentaViewSets)
router.register('unidade', UnidadeViewSets)
router.register('user', UserViewSet)
router.register('supervisao', SupervisaoViewSets)

urlpatterns = [
    path('get_menu/<int:pk>', get_menu, name='get_menu')
]
