# Generated by Django 3.1.4 on 2021-01-12 13:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, max_length=50000, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('company', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, max_length=50000, null=True)),
                ('short_description', models.CharField(blank=True, max_length=800, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_available', models.BooleanField(default=True)),
                ('unit', models.CharField(choices=[('dozen', 'Dozen'), ('weight', 'Weight'), ('no', 'No')], max_length=300)),
                ('avg_price', models.FloatField(default=0.0)),
                ('currency', models.CharField(choices=[('AOK', 'AOK'), ('YER', 'YER'), ('ZWL', 'ZWL'), ('LTT', 'LTT'), ('DZD', 'DZD'), ('CLP', 'CLP'), ('KWD', 'KWD'), ('UYW', 'UYW'), ('LYD', 'LYD'), ('BGN', 'BGN'), ('BAN', 'BAN'), ('KGS', 'KGS'), ('GQE', 'GQE'), ('BND', 'BND'), ('XBB', 'XBB'), ('COU', 'COU'), ('SAR', 'SAR'), ('ILP', 'ILP'), ('TND', 'TND'), ('BHD', 'BHD'), ('CSK', 'CSK'), ('XOF', 'XOF'), ('ZRN', 'ZRN'), ('ROL', 'ROL'), ('EUR', 'EUR'), ('BAM', 'BAM'), ('IQD', 'IQD'), ('GHS', 'GHS'), ('KZT', 'KZT'), ('PEI', 'PEI'), ('KMF', 'KMF'), ('CUC', 'CUC'), ('XBD', 'XBD'), ('BGO', 'BGO'), ('ARL', 'ARL'), ('XFU', 'XFU'), ('VUV', 'VUV'), ('XAF', 'XAF'), ('KYD', 'KYD'), ('LVL', 'LVL'), ('SKK', 'SKK'), ('SVC', 'SVC'), ('NZD', 'NZD'), ('TRL', 'TRL'), ('BRC', 'BRC'), ('DEM', 'DEM'), ('MCF', 'MCF'), ('NAD', 'NAD'), ('TJS', 'TJS'), ('ATS', 'ATS'), ('JOD', 'JOD'), ('ALK', 'ALK'), ('CNH', 'CNH'), ('SDG', 'SDG'), ('JMD', 'JMD'), ('TMT', 'TMT'), ('ISJ', 'ISJ'), ('BRB', 'BRB'), ('USS', 'USS'), ('MAD', 'MAD'), ('HRD', 'HRD'), ('CRC', 'CRC'), ('BOP', 'BOP'), ('COP', 'COP'), ('FJD', 'FJD'), ('MRU', 'MRU'), ('IEP', 'IEP'), ('BRE', 'BRE'), ('SIT', 'SIT'), ('CNX', 'CNX'), ('LVR', 'LVR'), ('THB', 'THB'), ('RHD', 'RHD'), ('MVR', 'MVR'), ('CYP', 'CYP'), ('ZMK', 'ZMK'), ('PKR', 'PKR'), ('XCD', 'XCD'), ('PTE', 'PTE'), ('KES', 'KES'), ('PES', 'PES'), ('UGX', 'UGX'), ('SUR', 'SUR'), ('CHF', 'CHF'), ('MRO', 'MRO'), ('DDM', 'DDM'), ('MZN', 'MZN'), ('ZAL', 'ZAL'), ('AZN', 'AZN'), ('BRZ', 'BRZ'), ('ESP', 'ESP'), ('ARP', 'ARP'), ('ALL', 'ALL'), ('HNL', 'HNL'), ('ETB', 'ETB'), ('XEU', 'XEU'), ('GWP', 'GWP'), ('BRL', 'BRL'), ('XAG', 'XAG'), ('XBA', 'XBA'), ('VND', 'VND'), ('GNF', 'GNF'), ('XPD', 'XPD'), ('GHC', 'GHC'), ('MKN', 'MKN'), ('ZMW', 'ZMW'), ('TWD', 'TWD'), ('XDR', 'XDR'), ('ANG', 'ANG'), ('PLZ', 'PLZ'), ('SDD', 'SDD'), ('LUL', 'LUL'), ('JPY', 'JPY'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('IDR', 'IDR'), ('GBP', 'GBP'), ('SYP', 'SYP'), ('STD', 'STD'), ('ECV', 'ECV'), ('VEF', 'VEF'), ('FRF', 'FRF'), ('LBP', 'LBP'), ('RSD', 'RSD'), ('MZM', 'MZM'), ('BYR', 'BYR'), ('CVE', 'CVE'), ('ARM', 'ARM'), ('DOP', 'DOP'), ('LTL', 'LTL'), ('LSL', 'LSL'), ('VEB', 'VEB'), ('USD', 'USD'), ('MGA', 'MGA'), ('PYG', 'PYG'), ('BRR', 'BRR'), ('STN', 'STN'), ('RWF', 'RWF'), ('CDF', 'CDF'), ('ECS', 'ECS'), ('XAU', 'XAU'), ('UGS', 'UGS'), ('PLN', 'PLN'), ('MLF', 'MLF'), ('XUA', 'XUA'), ('BGM', 'BGM'), ('KPW', 'KPW'), ('LUF', 'LUF'), ('MNT', 'MNT'), ('ERN', 'ERN'), ('KRO', 'KRO'), ('UAH', 'UAH'), ('ARA', 'ARA'), ('OMR', 'OMR'), ('AOA', 'AOA'), ('BOL', 'BOL'), ('HUF', 'HUF'), ('LUC', 'LUC'), ('SEK', 'SEK'), ('ZWR', 'ZWR'), ('HKD', 'HKD'), ('XBC', 'XBC'), ('ILR', 'ILR'), ('AZM', 'AZM'), ('XPT', 'XPT'), ('MTP', 'MTP'), ('TRY', 'TRY'), ('BGL', 'BGL'), ('MUR', 'MUR'), ('GNS', 'GNS'), ('IRR', 'IRR'), ('LKR', 'LKR'), ('KRH', 'KRH'), ('YDD', 'YDD'), ('SCR', 'SCR'), ('KHR', 'KHR'), ('KRW', 'KRW'), ('MXV', 'MXV'), ('VNN', 'VNN'), ('CUP', 'CUP'), ('MXP', 'MXP'), ('AED', 'AED'), ('NGN', 'NGN'), ('PGK', 'PGK'), ('SSP', 'SSP'), ('BMD', 'BMD'), ('TJR', 'TJR'), ('GIP', 'GIP'), ('GEL', 'GEL'), ('TTD', 'TTD'), ('DKK', 'DKK'), ('MDC', 'MDC'), ('MGF', 'MGF'), ('INR', 'INR'), ('ZAR', 'ZAR'), ('BOB', 'BOB'), ('UZS', 'UZS'), ('QAR', 'QAR'), ('NOK', 'NOK'), ('NLG', 'NLG'), ('MZE', 'MZE'), ('AWG', 'AWG'), ('ADP', 'ADP'), ('XFO', 'XFO'), ('MAF', 'MAF'), ('LAK', 'LAK'), ('ITL', 'ITL'), ('HRK', 'HRK'), ('YUN', 'YUN'), ('HTG', 'HTG'), ('ARS', 'ARS'), ('BZD', 'BZD'), ('UYU', 'UYU'), ('AFA', 'AFA'), ('ISK', 'ISK'), ('YUD', 'YUD'), ('NIO', 'NIO'), ('UYP', 'UYP'), ('RUR', 'RUR'), ('BEF', 'BEF'), ('UAK', 'UAK'), ('XPF', 'XPF'), ('AUD', 'AUD'), ('LRD', 'LRD'), ('XXX', 'XXX'), ('SBD', 'SBD'), ('ZWD', 'ZWD'), ('ZRZ', 'ZRZ'), ('NPR', 'NPR'), ('PHP', 'PHP'), ('YUR', 'YUR'), ('TOP', 'TOP'), ('SHP', 'SHP'), ('CLF', 'CLF'), ('MVP', 'MVP'), ('SDP', 'SDP'), ('CZK', 'CZK'), ('GMD', 'GMD'), ('CAD', 'CAD'), ('SGD', 'SGD'), ('ESB', 'ESB'), ('CHE', 'CHE'), ('MMK', 'MMK'), ('RON', 'RON'), ('AFN', 'AFN'), ('ESA', 'ESA'), ('MKD', 'MKD'), ('PEN', 'PEN'), ('GEK', 'GEK'), ('SZL', 'SZL'), ('MTL', 'MTL'), ('BEL', 'BEL'), ('SRG', 'SRG'), ('CHW', 'CHW'), ('BIF', 'BIF'), ('FIM', 'FIM'), ('BSD', 'BSD'), ('AOR', 'AOR'), ('EEK', 'EEK'), ('SRD', 'SRD'), ('WST', 'WST'), ('VES', 'VES'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('UYI', 'UYI'), ('BOV', 'BOV'), ('BAD', 'BAD'), ('AON', 'AON'), ('CNY', 'CNY'), ('BYN', 'BYN'), ('AMD', 'AMD'), ('BUK', 'BUK'), ('GRD', 'GRD'), ('GTQ', 'GTQ'), ('PAB', 'PAB'), ('USN', 'USN'), ('XTS', 'XTS'), ('SLL', 'SLL'), ('BDT', 'BDT'), ('RUB', 'RUB'), ('TPE', 'TPE'), ('XSU', 'XSU'), ('GYD', 'GYD'), ('XRE', 'XRE'), ('MYR', 'MYR'), ('BYB', 'BYB'), ('BRN', 'BRN'), ('EGP', 'EGP'), ('FKP', 'FKP'), ('MOP', 'MOP'), ('GWE', 'GWE'), ('SOS', 'SOS'), ('NIC', 'NIC'), ('TZS', 'TZS'), ('TMM', 'TMM'), ('ILS', 'ILS'), ('BEC', 'BEC'), ('CLE', 'CLE'), ('MDL', 'MDL'), ('BBD', 'BBD'), ('DJF', 'DJF'), ('CSD', 'CSD'), ('YUM', 'YUM')], max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comment', models.TextField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='client_app.client')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
