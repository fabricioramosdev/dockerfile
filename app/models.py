from django.db.models import JSONField
from django.db import models
from django.core.validators import (MinValueValidator)

# from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.utils.html import format_html

from account.models import User
from django.contrib.auth.models import Group


#  Funções templates para os campos JSON
def get_default_impressoras():
    return {'impressoras': [{'ip': '', 'etiqueta': ''}]}


def get_default_emails():
    return {'email': [{'email': ''}]}


class Base(models.Model):
    criacao_base = models.DateTimeField(auto_now_add=True)
    atualizacao_base = models.DateTimeField(auto_now=True)
    situacao_base = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Unidade(Base):
    """
    Unidade Embraer
    """
    descricao = models.CharField(max_length=255)
    sigla = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}\t({self.sigla})'


class Hangar(Base):
    """
    Hangar Embraer
    """
    # B-001; F-107
    descricao = models.CharField(max_length=10, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Hangar'
        verbose_name_plural = 'Hangares'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class CPF(Base):

    """
    Sala CPF
    """
    descricao = models.CharField(max_length=255, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    hangar = models.ForeignKey(Hangar, on_delete=models.PROTECT)
    emails = JSONField('Emails', default=get_default_emails,  blank=True, null=True)
    impressoras = JSONField('Impressora', default=get_default_impressoras, blank=True, null=True)
    latiude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'CPF'
        verbose_name_plural = 'CPF´s'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'

    # @admin.display(ordering='descricao')
    # def colored_descricao(self):
    #     return format_html(
    #         '<h1 style="color: #{};">{}</h1>',
    #         '000',
    #         self.descricao,
    #     )


class CpfUsuario(Base):
    """
    Usuários da CPF
    """
    cpf = models.ForeignKey(CPF, on_delete=models.CASCADE, db_index=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, db_index=False)

    class Meta:
        verbose_name = 'CPF Usuário'
        verbose_name_plural = 'CPF´s Usuários'
        ordering = ['id']
        unique_together = ('cpf', 'usuario',)

    def __str__(self):
        return f'{self.pk}#\t{self.cpf}\t[{self.usuario}'


class Estacao(Base):
    """
    Estação/Posto de pagamento
    """
    descricao = models.CharField(max_length=255, blank=False, null=False)
    latiude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    hangar = models.ForeignKey(Hangar, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Estação'
        verbose_name_plural = 'Estações'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class LocalOrigem(Base):
    """
    Local de origem
    """
    descricao = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Local Origem'
        verbose_name_plural = 'Locais de Origens'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class LocalCaixaBin(Base):
    """
    Local da caixa bin
    """
    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    corredor = models.IntegerField(validators=[MinValueValidator(1)])
    fila = models.CharField(max_length=2)
    caixa = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'Local Bin'
        verbose_name_plural = 'Locais  Bin`s'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\tC{"%02d"%self.corredor}{self.fila}{"%02d"%self.caixa}'


class ProcessoEspecial(Base):
    """
    Processo Especiais
    """
    descricao = models.CharField(max_length=255, blank=False, null=False)
    observacao = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Processo Especial'
        verbose_name_plural = 'Processos Especiais'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class Gerencia(Base):
    """
    Gerencia
    """
    nome = models.CharField(max_length=255)
    chapa = models.CharField(max_length=255)
    login = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=255, blank=True, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Gerencia'
        verbose_name_plural = 'Gerencias'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.nome}\t(Matricula:{self.chapa})'


class Supervisao(Base):
    """
    Supervisão
    """
    nome = models.CharField(max_length=255)
    chapa = models.CharField(max_length=255)
    login = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=255, blank=True, null=True)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Supervisão'
        verbose_name_plural = 'Supervisões'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.nome}\t(Matricula:{self.chapa})'


class Montagem(Base):
    """
    Montagem
    """
    descricao = models.CharField(max_length=255, blank=False, null=False)
    estacao = models.ForeignKey(Estacao, on_delete=models.PROTECT)
    supervisor = models.ForeignKey(Supervisao, on_delete=models.PROTECT)
    hangar = models.ForeignKey(Hangar, on_delete=models.PROTECT)
    emails = JSONField('Emails', default=get_default_emails,  blank=True, null=True)
    riscos = (('0', 'Alto Risco'), ('1', 'Médio Risco'), ('2', 'Baixo Risco'), ('3', 'Área não produtiva'))
    risco_foe = models.CharField(choices=riscos, default=riscos[3], max_length=1)

    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Montagem'
        verbose_name_plural = 'Montagens'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'

    @admin.display(ordering='risco_foe')
    def classificacao_risco_foe(self):

        if self.risco_foe == '0':
            return format_html(
                '<span style="color: #{};background-color: #eceff1;padding: 0.6em;">{}</span>',
                'f44336',
                'Alto Risco',
            )
        elif self.risco_foe == '1':
            return format_html(
                '<span style="color: #{};background-color: #eceff1;padding: 0.6em;">{}</span>',
                '673ab7',
                'Médio Risco',
            )
        elif self.risco_foe == '2':
            return format_html(
                '<span style="color: #{};background-color: #eceff1;padding: 0.6em;">{}</span>',
                '9ccc65',
                'Baixo Risco',
            )
        else:
            return format_html(
                '<span style="color: #{};background-color: #eceff1;padding: 0.6em;">{}</span>',
                'bdbdbd',
                'Área não produtiva',
            )

class Kit(Base):
    """
    Kit de ferramenta
    """
    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(unique=True, validators=[MinValueValidator(1)])
    montagem = models.ForeignKey(Montagem, on_delete=models.PROTECT)
    arquivo = models.CharField(max_length=255, blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)  # base64 da imagem da ferramenta
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Kit'
        verbose_name_plural = 'Kits'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.cpf}\t(CPF{"%03d"%self.numero})'


class Familia(Base):
    """
    Família de ferramenta
    """
    consumo = (('0', 'Não'), ('1', 'Sim'))

    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255, blank=True, null=True, unique=True)
    consumo = models.CharField(choices=consumo, default=consumo[0], max_length=1)
    kit = models.ManyToManyField(Kit, through='MontaKit')

    class Meta:
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class MontaKit(Base):
    """
    Ferramentas do kit
    """
    descricao = models.CharField(max_length=255, blank=True, null=True)
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT)
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, blank=False, null=False)

    class Meta:
        verbose_name = 'Montagem de Kit'
        verbose_name_plural = 'Montagens de Kits'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.familia}\t{self.quantidade}'


class Ferramenta(Base):
    """
    Ferramentas
    """
    situacao = (('1', 'Estoque'), ('2', 'Produçao'), ('3', 'Discarte'),
                ('4', 'Manutenção'), ('5', 'Calibração'), ('6', 'Análise'), ('7', 'FOE'),
                ('8', 'Calibração expirada'), ('9', 'Sala'), ('10', 'Emprestimo avulso'))

    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    descricao_abr = models.CharField(max_length=255, blank=False, null=False)
    descricao_lon = models.TextField()
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT, related_name='familia_ferramenta')
    consumo = (('0', 'Não'), ('1', 'Sim'))
    consumo = models.CharField(choices=consumo, default=consumo[0], max_length=1)

    ativo = models.CharField(max_length=255,  unique=True, blank=True, null=True)
    pn = models.CharField(max_length=255, blank=True, null=True)
    cemb = models.CharField(max_length=255, blank=True, null=True)

    quantidade_cadastro = models.IntegerField(default=0, blank=False, null=False)
    quantidade_estoque = models.IntegerField(default=0, blank=True, null=True)
    quantidade_analise = models.IntegerField(default=0, blank=True, null=True)
    quantidade_discarte = models.IntegerField(default=0, blank=True, null=True)
    quantidade_manutencao = models.IntegerField(default=0, blank=True, null=True)
    quantidade_calibracao = models.IntegerField(default=0, blank=True, null=True)
    quantidade_producao = models.IntegerField(default=0, blank=True, null=True)
    quantidade_foe = models.IntegerField(default=0, blank=True, null=True)
    quantidade_calibracao_exp = models.IntegerField(default=0, blank=True, null=True)
    quantidade_sala = models.IntegerField(default=0, blank=True, null=True)
    quantidade_emprestimo_avul = models.IntegerField(default=0, blank=True, null=True)

    local_caixa_bin = models.ForeignKey(LocalCaixaBin, on_delete=models.PROTECT)
    local_origem = models.ForeignKey(LocalOrigem, on_delete=models.PROTECT)

    descarte_em = models.DateField(null=True, blank=True)
    situacao_inventario = models.BooleanField()
    inventario_em = models.DateField(null=True, blank=True)

    calibrado = models.BooleanField()
    calibracao_exp = models.DateField(null=True, blank=True)

    modificado = models.BooleanField()

    valor = models.FloatField(default=0.0, blank=True, null=True)

    processo_especial = models.ForeignKey(ProcessoEspecial, on_delete=models.SET_NULL, blank=True, null=True)

    etiqueta_rfid = models.TextField(blank=True, null=True)
    imagem = models.TextField(blank=True, null=True)  # base64 da imagem da ferramenta
    desenho = models.TextField(blank=True, null=True)  #

    observacao = models.TextField(blank=True, null=True)

    situacao = models.CharField(choices=situacao, default=situacao[0], max_length=45)

    class Meta:
        verbose_name = 'Ferramenta'
        verbose_name_plural = 'Ferramentas'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.cpf}\t{self.descricao_abr}'


"""
CALCULO DE CARGA CAPACIDADE COLETAR DADOS PRE PAGAMENTO
class PrePagamento(Base):
    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT)

    usuario_pgto = models.CharField(max_length=255, blank=False, null=False)
    data_pgto = models.DateField(blank=False, null=False)



class PrePagamentoFerramenta(Base):
    prepagamento = models.ForeignKey(PrePagamento, on_delete=models.PROTECT)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    # hora_leitura
    # hora_pagamento
"""


class Pagamento(Base):
    """
    pagamento kit
    """

    cpf = models.ForeignKey(CPF, on_delete=models.PROTECT)
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT)

    usuario_cpf_pgto = models.CharField(max_length=255, blank=True, null=True)  # login
    data_pgto = models.DateField(blank=False,  null=False)
    completo_pgto = models.BooleanField(blank=True,  null=True)

    usuario_cpf_rcto = models.CharField(max_length=255, blank=True, null=True)  # login
    data_rcto = models.DateField(blank=True,  null=True)
    completo_rcto = models.BooleanField(blank=True,  null=True)

    tempo_pgto = models.IntegerField(blank=True,  null=True)

    class Meta:
        verbose_name = 'Pgto. kit'
        verbose_name_plural = 'Pgtos. kits'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.kit}'


class PagamentoFerramenta(Base):

    """
    Pagamento de ferramentas
    """

    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'Pgto. Ferramenta'
        verbose_name_plural = 'Pgtos. Ferramentas'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.pagamento}\t{self.ferramenta}'


class PagamentoFalta(Base):

    """
    Pagamentos faltas
    """
    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT)
    familia = models.ForeignKey(Familia, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = 'Pagamento Falta'
        verbose_name_plural = 'Pagamentos Falta'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.pagamento}'


class EmprestimoAvulso(Base):

    """
    Emprestimos avulsos de ferramentas
    """
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    usuario_producao = models.CharField(max_length=255, blank=True, null=True)  # login
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t[{self.usuario_producao}]'


class FOE(Base):

    """
    FOE
    """

    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT)
    pagamento_ferramenta = models.ForeignKey(PagamentoFerramenta, on_delete=models.PROTECT)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    nota_perda = models.CharField(blank=True, null=True, max_length=45)  # Nota foe de perda
    perda_em = models.DateTimeField(blank=True, null=True)

    nota_encontro = models.CharField(blank=True, null=True, max_length=45)  # Nota foe de encontrado
    encontro_em = models.DateTimeField(blank=True, null=True)
    situacao = (('1', 'Perdida'), ('0', 'Encontrada'))
    situacao_foe = models.CharField(choices=situacao, default=situacao[0], max_length=45)

    usuario_producao = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Foe'
        verbose_name_plural = 'Foes'
        ordering = ['id']

    def __str__(self):
        return f'#{self.pk}]\t[{self.pagamento}\t{self.pagamento_ferramenta}\t{self.ferramenta}'


class GTO(Base):
    """
    GTO agendamento de ferramentas
    """
    kit = models.ForeignKey(Kit, on_delete=models.PROTECT)
    dia_solicitado = models.TextField()  # Armazena uma lista ou json com os dias que foram marcados

    turnos = (('1', '1º Turno'), ('2', '2º Turno'), ('3', '1º e 2º Turno'))

    turno_solicitado = models.CharField(choices=turnos, default=turnos[0], max_length=1)
    usuario_producao = models.CharField(max_length=255, blank=True, null=True)  # login

    turno_pagamento = models.CharField(choices=turnos, default=turnos[0], max_length=1)
    data_pagamento = models.DateField(null=False, blank=False)
    situacao_pagamento = models.BooleanField(default=False)

    turno_recebimento = models.CharField(choices=turnos, default=turnos[0], max_length=1)
    data_recebimento = models.DateField(null=False, blank=False)
    situacao_recebimento = models.BooleanField(default=False)

    tipos = (('1', 'Agendamento'), ('2', 'Spot'))
    tipo_gto = models.CharField(choices=tipos, default=tipos[0], max_length=1)

    sla = models.DecimalField(decimal_places=2, max_digits=2)  # Sla em horas

    obs = models.TextField()
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'GTO'
        verbose_name_plural = 'GTO´s'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.kit}'


class QuebraFerramenta(Base):

    """
    Quebras de ferramentas
    """

    pagamento = models.ForeignKey(Pagamento, on_delete=models.PROTECT)
    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    pagamento_ferramenta = models.ForeignKey(PagamentoFerramenta, on_delete=models.PROTECT)
    usuario_producao = models.CharField(max_length=255, blank=True, null=True)  # login
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Quebra Ferramenta'
        verbose_name_plural = 'Quebras'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.pagamento}\t{self.pagamento_ferramenta}\t{self.ferramenta}'


class Movimento(Base):

    """
    Movimentação de ferramentas
    """

    situacao = (('1', 'Estoque'), ('2', 'Produçao'), ('3', 'Discarte'),
                ('4', 'Manutenção'), ('5', 'Calibração'), ('6', 'Análise'), ('7', 'FOE'),
                ('8', 'Calibração expirada'), ('9', 'Sala'), ('10', 'Emprestimo avulso'))

    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)

    situacao_de = models.CharField(choices=situacao, max_length=45)
    situacao_para = models.CharField(choices=situacao, max_length=45)

    pagamento_de = models.ForeignKey(Pagamento, null=True, blank=True, on_delete=models.SET_NULL,
                                     related_name='pagamento_de')
    pagamento_para = models.ForeignKey(Pagamento, null=True, blank=True, on_delete=models.SET_NULL,
                                       related_name='pagamento_para')

    cpf_de = models.ForeignKey(CPF, on_delete=models.SET_NULL, blank=True, null=True, related_name='cpf_de')
    cpf_para = models.ForeignKey(CPF, on_delete=models.SET_NULL, blank=True, null=True, related_name='cpf_para')

    quantidade = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    obs = models.TextField(blank=True, null=True)
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimentações'
        ordering = ['id']

    def __str__(self):
        return f'#{self.pk}\t{self.ferramenta}\t{self.situacao_de}\t{self.situacao_para}'


class Notificacao(Base):
    """
    Nofificações do sistema
    """

    descricao = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['id']

    def __str__(self):
        return f'#{self.pk}\t{self.descricao}\t{self.usuario_cpf}\t{self.data}'


class Inventario(Base):

    """
    Inventário semanal
    """

    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    semana = models.IntegerField()
    quantidades_estoque = models.IntegerField()
    quantidades_inventario = models.IntegerField()
    consolida = models.BooleanField(default=False, null=False)
    usuario_cpf = models.CharField(max_length=255, blank=True, null=True)  # login

    class Meta:
        verbose_name = 'Iventario'
        verbose_name_plural = 'Inventários'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.ferramenta}\t{self.semana}'


class InventarioHistorico(Base):
    """
    Histórico inventário semanal
    """

    ferramenta = models.ForeignKey(Ferramenta, on_delete=models.PROTECT)
    semana = models.IntegerField()
    quantidades_estoque = models.IntegerField()
    quantidades_inventario = models.IntegerField()
    consolida = models.BooleanField(default=False, null=False)
    usuario_cpf = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Iventario Histórico'
        verbose_name_plural = 'Inventários Históricos'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.ferramenta}\t{self.semana}'


class MenuSistema(Base):

    """
    Menu sistema
    """
    descricao = models.CharField(max_length=255, blank=False, null=False)
    icone = models.CharField(max_length=255, default='apps', blank=False, null=False)
    grupo = models.ManyToManyField(Group, blank=True)

    class Meta:
        verbose_name = 'Menu App'
        verbose_name_plural = 'Menus App'
        ordering = ['id']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'


class SubMenuSistema(Base):

    """
    SubMenu sistema
    """

    menu = models.ManyToManyField(MenuSistema, blank=False)
    view = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=False, null=False)
    descricao_curta = models.CharField(max_length=2, blank=False, null=False)
    url = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Sub-menu App'
        verbose_name_plural = 'Subs-menus App'
        ordering = ['descricao']

    def __str__(self):
        return f'{self.pk}#\t{self.descricao}'
