from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (CPF, Estacao, EmprestimoAvulso, Familia, Ferramenta, FOE,  Gerencia, GTO, Hangar, Inventario, Kit, LocalCaixaBin,
                     LocalOrigem, Montagem, MontaKit, Movimento, Notificacao, Pagamento, PagamentoFerramenta, PagamentoFalta,
                     ProcessoEspecial, QuebraFerramenta,  Supervisao, Unidade)


class CPFSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPF
        fields = '__all__'


class EstacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estacao
        fields = '__all__'


class EmprestimoAvulsoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmprestimoAvulso
        fields = '__all__'


class FamiliaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Familia
        fields = '__all__'


class FerramentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ferramenta
        fields = '__all__'


class FOESerializer(serializers.ModelSerializer):

    class Meta:
        model = FOE
        fields = '__all__'


class GerenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gerencia
        fields = '__all__'


class GTOSerializer(serializers.ModelSerializer):

    class Meta:
        model = GTO
        fields = '__all__'


class HangarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hangar
        fields = '__all__'


class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario
        fields = '__all__'


class KitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kit
        fields = '__all__'


class LocalCaixaBinSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalCaixaBin
        fields = '__all__'


class LocalOrigemBinSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalOrigem
        fields = '__all__'


class LocalOrigemBinSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocalOrigem
        fields = '__all__'


class MontagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Montagem
        fields = '__all__'


class MovimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movimento
        fields = '__all__'


class SupervisaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supervisao
        fields = '__all__'


class MontaKitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MontaKit
        fields = '__all__'


class PagamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pagamento
        fields = '__all__'


class PagamentoFerramentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PagamentoFerramenta
        fields = '__all__'


class PagamentoFaltaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PagamentoFalta
        fields = '__all__'


class ProcessoEspecialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProcessoEspecial
        fields = '__all__'


class QuebraFerramentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuebraFerramenta
        fields = '__all__'


class UnidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unidade
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = User
        fields = '__all__'


class NotificacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notificacao
        fields = '__all__'