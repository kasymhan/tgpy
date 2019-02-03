from django import forms
import django.db
from django.core.exceptions import ValidationError
import read.models
import write.models

class Write(forms.ModelForm):
    class Meta:
        model = read.models.BlogAbiturient
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'type':'number'}),
        }

    def clean_name(self):
        new_name = int(self.cleaned_data['name'])
        db_1 = read.models.BlogApplication.objects.filter(abiturient=new_name).values()
        if not db_1:
            raise ValidationError('нет такого пользователь ')
        else:
            return new_name

    @property
    def write(self):
        new_name = int(self.cleaned_data['name'])
        print(new_name)
        name_post = read.models.BlogApplication.objects.filter(abiturient=new_name)
        abatement = name_post.values()
        lis_app = [abatement[0]['abiturient_id'],
                   abatement[0]['special_id'],
                   abatement[0]['enlisted']]
        abiturient = read.models.BlogAbiturient.objects.filter(id=lis_app[0]).values()
        print(abiturient)
        lis = [abiturient[0]['id'],
               abiturient[0]['name'],
               abiturient[0]['country_id'],
               abiturient[0]['region_id'],
               abiturient[0]['area_id'],
               abiturient[0]['city_id']]
        countr = read.models.BlogCountr.objects.filter(id=lis[2]).values()
        region = read.models.BlogRegion.objects.filter(id=lis[3]).values()
        area = read.models.BlogArea.objects.filter(id=lis[4]).values()
        city = read.models.BlogCity.objects.filter(id=lis[5]).values()
        lis_countr = [
            countr[0]['name'],
            countr[0]['out'],
        ]
        lis_region = [
            region[0]['name'],
            region[0]['out'],
        ]
        lis_area = [
            area[0]['name'],
            area[0]['out'],
        ]
        lis_city = [
            city[0]['name'],
            city[0]['out'],
        ]
        special = read.models.BlogSpecial.objects.filter(id=lis_app[1]).values()[0]
        lis_special = [
            special['name'],
            special['fac_id'],
            special['out'],

        ]
        fac = read.models.BlogFacully.objects.filter(id=lis_special[1]).values()[0]
        lis_fac = [
            fac['out'],
            fac['name'],

        ]
        creat_area = write.models.BlogArea.objects.using('user').create(id=lis_area[1],name=lis_area[0])
        create_region = write.models.BlogRegion.objects.using('user').create(id=lis_region[1], name=lis_region[0])
        creat_city = write.models.BlogCity.objects.using('user').create(id=lis_city[1], name=lis_city[0])
        creat_countr = write.models.BlogCountr.objects.using('user').create(id=lis_countr[1], name=lis_countr[0])
        creat_fac = write.models.BlogFacully.objects.using('user').create(id=lis_fac[0], name=lis_fac[1])
        print(creat_fac.id)
        creat_special = write.models.BlogSpecial.objects.using('user').create(id=lis_special[2],name=lis_special[0],fac=creat_fac)
        creat_ab = write.models.BlogAbiturient.objects.using('user').create(name=lis[0],
                                                                            area=creat_area,
                                                                            city=creat_city,
                                                                            country=creat_countr,
                                                                            region=create_region)
        creat_app = write.models.BlogApplication.objects.using('user').create(abiturient=creat_ab,
                                                                              enlisted=True,
                                                                              special=creat_special)
        return 'write_ok'
class Read(forms.ModelForm):
    class Meta:
        model = write.models.BlogAbiturient
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        new_name_1 = self.cleaned_data['name']
        db_1 = read.models.BlogAbiturient.objects.filter(name=new_name_1).values()
        if not db_1:
            raise ValidationError('нет такого пользователь ')
        else:
            raise ValidationError('есть такой пользователь')
        return new_name_1

    def read(self):
        new_name = self.cleaned_data['name']
        name_post =  read.models.BlogAbiturient.objects.filter(name=new_name)
        abiturient = name_post.values()
        lis = [abiturient[0]['id'],
               abiturient[0]['name'],
               abiturient[0]['country_id'],
               abiturient[0]['region_id'],
               abiturient[0]['area_id'],
               abiturient[0]['city_id']]
        countr =  read.models.BlogCountr.objects.filter(id=lis[2]).values()
        region = read.models.BlogRegion.objects.filter(id=lis[3]).values()
        area =  read.models.BlogArea.objects.filter(id=lis[4]).values()
        city =  read.models.BlogCity.objects.filter(id=lis[5]).values()
        lis_countr = [
            countr[0]['id'],
            countr[0]['name'],
            countr[0]['out_id'],
        ]
        lis_region = [
            region[0]['id'],
            region[0]['name'],
            region[0]['out_id'],
        ]
        lis_area = [
            area[0]['id'],
            area[0]['name'],
            area[0]['out_id'],
        ]
        lis_city = [
            city[0]['id'],
            city[0]['name'],
            city[0]['out_id'], ]
        context = {'name': lis[1], 'countr': lis_countr[1], 'region': lis_region[1], 'area': lis_area[1],
                   'city': lis_city[1]}
        return context


