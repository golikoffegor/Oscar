from rest_framework import serializers
from .models import Coefficient, Results

class CoefficientSerializer(serializers.Serializer): 
    address = serializers.CharField(max_length = 128)
    author_id = serializers.IntegerField()
    diameter_PPU = serializers.IntegerField()
    vvoda_PPU = serializers.IntegerField()
    nopora_PPU = serializers.IntegerField()
    diameter_IZOP = serializers.IntegerField()
    vvoda_IZOP = serializers.IntegerField()
    nopora_IZOP = serializers.IntegerField()
    width_mon = serializers.IntegerField()
    height_mon = serializers.IntegerField()
    m_mon = serializers.IntegerField()
    width_bez_1 = serializers.IntegerField()
    m_bez_1 = serializers.IntegerField()
    width_bez_2 = serializers.IntegerField()
    m_bez_2 = serializers.IntegerField()
    l6_sht = serializers.IntegerField()
    l6_l = serializers.IntegerField()
    l6_dl = serializers.IntegerField()
    l6_pl = serializers.IntegerField()
    l6_dpl = serializers.IntegerField()
    l11_sht = serializers.IntegerField()
    l11_l = serializers.IntegerField()
    l11_dl = serializers.IntegerField()
    l11_pl = serializers.IntegerField()
    l11_dpl = serializers.IntegerField()
    fbs336 = serializers.IntegerField()
    fbs636 = serializers.IntegerField()
    fbs936 = serializers.IntegerField()
    fbs1236 = serializers.IntegerField()
    fbs2436 = serializers.IntegerField()
    podb_B15 = serializers.IntegerField()
    sil_PPU = serializers.IntegerField()
    sil_IZOP = serializers.IntegerField()

    def create(self, validated_data):
        return Coefficient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)  
        instance.author_id = validated_data.get('author_id', instance.author_id)  
        instance.diameter_PPU = validated_data.get('diameter_PPU', instance.diameter_PPU)  
        instance.vvoda_PPU = validated_data.get('vvoda_PPU', instance.vvoda_PPU) 
        instance.nopora_PPU = validated_data.get('nopora_PPU', instance.nopora_PPU) 
        instance.diameter_IZOP = validated_data.get('diameter_IZOP', instance.diameter_IZOP) 
        instance.vvoda_IZOP = validated_data.get('vvoda_IZOP', instance.vvoda_IZOP) 
        instance.nopora_IZOP = validated_data.get('nopora_IZOP', instance.nopora_IZOP) 
        instance.width_mon = validated_data.get('width_mon', instance.width_mon) 
        instance.height_mon = validated_data.get('height_mon', instance.height_mon) 
        instance.m_mon = validated_data.get('m_mon', instance.m_mon) 
        instance.width_bez_1 = validated_data.get('width_bez_1', instance.width_bez_1) 
        instance.m_bez_1 = validated_data.get('m_bez_1', instance.m_bez_1) 
        instance.width_bez_2 = validated_data.get('width_bez_2', instance.width_bez_2) 
        instance.m_bez_2 = validated_data.get('m_bez_2', instance.m_bez_2) 
        instance.l6_sht = validated_data.get('l6_sht', instance.l6_sht) 
        instance.l6_l = validated_data.get('l6_l', instance.l6_l) 
        instance.l6_dl = validated_data.get('l6_dl', instance.l6_dl) 
        instance.l6_pl = validated_data.get('l6_pl', instance.l6_pl) 
        instance.l6_dpl = validated_data.get('l6_dpl', instance.l6_dpl) 
        instance.l11_sht = validated_data.get('l11_sht', instance.l11_sht) 
        instance.l11_l = validated_data.get('l11_l', instance.l11_l) 
        instance.l11_dl = validated_data.get('l11_dl', instance.l11_dl) 
        instance.l11_pl = validated_data.get('l11_pl', instance.l11_pl) 
        instance.l11_dpl = validated_data.get('l11_dpl', instance.l11_dpl) 
        instance.fbs336 = validated_data.get('fbs336', instance.fbs336) 
        instance.fbs636 = validated_data.get('fbs636', instance.fbs636) 
        instance.fbs936 = validated_data.get('fbs936', instance.fbs936) 
        instance.fbs1236 = validated_data.get('fbs1236', instance.fbs1236) 
        instance.fbs2436 = validated_data.get('fbs2436', instance.fbs2436) 
        instance.podb_B15 = validated_data.get('podb_B15', instance.podb_B15) 
        instance.sil_PPU = validated_data.get('sil_PPU', instance.sil_PPU) 
        instance.sil_IZOP = validated_data.get('sil_IZOP', instance.sil_IZOP) 

        instance.save()
        return instance

class ResultsSerializer(serializers.Serializer):
    address = serializers.CharField(max_length = 128)
    result_CO2_1 = serializers.CharField(max_length = 3000)
    result_CO2_2 = serializers.CharField(max_length = 3000)

    def create(self, validated_data):
        return Results.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)  
        instance.result_CO2_1 = validated_data.get('result_CO2_1', instance.result_CO2_1)
        instance.result_CO2_2 = validated_data.get('result_CO2_2', instance.result_CO2_2) 

        instance.save()
        return instance 