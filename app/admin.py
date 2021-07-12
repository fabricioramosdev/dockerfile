from django.contrib import admin
from django.db.models import Count, Sum
from django.utils.html import format_html

from .models import (CPF, CpfUsuario, EmprestimoAvulso, Estacao, Familia, Ferramenta, FOE, Gerencia, GTO,
                     Hangar, Inventario, InventarioHistorico, Kit, LocalCaixaBin, LocalOrigem, MenuSistema, Montagem,
                     MontaKit, Movimento, Notificacao, Pagamento, PagamentoFerramenta,
                     PagamentoFalta, ProcessoEspecial, QuebraFerramenta, Supervisao, SubMenuSistema, Unidade)



@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'sigla')
    list_filter = ('sigla',)


@admin.register(CPF)
class CPFAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'hangar')
    list_filter = ('descricao',)


@admin.register(CpfUsuario)
class CpfUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'cpf')
    list_filter = ('cpf',)


@admin.register(Estacao)
class EstacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'hangar')
    list_filter = ('hangar',)


@admin.register(EmprestimoAvulso)
class EmprestimoAvulsoAdmin(admin.ModelAdmin):
    list_display = ('ferramenta', 'usuario_producao')
    list_filter = ('usuario_producao',)


@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'descricao', 'consumo')
    list_filter = ('descricao',)


@admin.register(Ferramenta)
class FerramentaAdmin(admin.ModelAdmin):
    list_display = ('descricao_abr', 'familia', 'cpf')
    list_filter = ('familia', 'cpf')


@admin.register(FOE)
class FOEAdmin(admin.ModelAdmin):
    list_display = ('id', 'pagamento', 'pagamento_ferramenta')
    list_filter = ('pagamento',)



@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'descricao', 'numero')
    list_filter = ('cpf',)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('ferramenta', 'semana', 'consolida')
    list_filter = ('semana',)


@admin.register(InventarioHistorico)
class InventarioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('ferramenta', 'semana', 'consolida')
    list_filter = ('semana',)



@admin.register(MontaKit)
class MontaKitKitAdmin(admin.ModelAdmin):
    list_display = ('kit', 'descricao', 'familia', 'quantidade')
    list_filter = ('kit', 'familia',)


@admin.register(Gerencia)
class GerenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'chapa')
    list_filter = ('nome',)


@admin.register(GTO)
class GTOAdmin(admin.ModelAdmin):
    list_display = ('id', 'kit', 'dia_solicitado')
    list_filter = ('kit',)


@admin.register(Hangar)
class HangarAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'unidade')
    list_filter = ('unidade',)


@admin.register(LocalCaixaBin)
class LocalCaixaBinAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'corredor', 'fila', 'caixa')
    list_filter = ('cpf',)


@admin.register(LocalOrigem)
class LocalOrigemAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)



@admin.register(MenuSistema)
class MenuSistemaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)


@admin.register(Montagem)
class MontagemAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'hangar', 'supervisor', 'classificacao_risco_foe')
    list_filter = ('hangar',)

@admin.register(Movimento)
class MovimentoAdmin(admin.ModelAdmin):
    list_display = ('ferramenta', 'id', 'situacao_de', 'situacao_para')
    list_filter = ('ferramenta',)


@admin.register(Supervisao)
class SupervisaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'chapa')
    list_filter = ('nome',)


@admin.register(SubMenuSistema)
class SubMenuSistemaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('kit', 'data_pgto', 'data_rcto', 'id')
    list_filter = ('kit',)


@admin.register(PagamentoFerramenta)
class PagamentoFerramentaAdmin(admin.ModelAdmin):
    list_display = ('pagamento', 'ferramenta', 'id')
    list_filter = ('ferramenta',)


@admin.register(PagamentoFalta)
class PagamentoFaltaAdmin(admin.ModelAdmin):
    list_display = ('pagamento', 'familia', 'id')
    list_filter = ('familia',)


@admin.register(ProcessoEspecial)
class ProcessoEspecialAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ('descricao',)


@admin.register(QuebraFerramenta)
class QuebraFerramentalAdmin(admin.ModelAdmin):
    list_display = ('pagamento', 'pagamento_ferramenta')
    list_filter = ('pagamento',)


@admin.register(Notificacao)
class NotificacaolAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'data', 'usuario_cpf')
    list_filter = ('usuario_cpf',)


# @admin.register(FOEResumo)
# class FOEResumoAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/foe_resumo_lista.html'

