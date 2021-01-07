# Generated by Django 3.1.4 on 2021-01-07 06:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210107_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('AOR', 'AOR'), ('KRW', 'KRW'), ('TMT', 'TMT'), ('ZWR', 'ZWR'), ('XRE', 'XRE'), ('EUR', 'EUR'), ('SAR', 'SAR'), ('NAD', 'NAD'), ('BRB', 'BRB'), ('PTE', 'PTE'), ('DJF', 'DJF'), ('PYG', 'PYG'), ('HRK', 'HRK'), ('CLF', 'CLF'), ('FRF', 'FRF'), ('IDR', 'IDR'), ('XBB', 'XBB'), ('CUP', 'CUP'), ('AFA', 'AFA'), ('YDD', 'YDD'), ('STN', 'STN'), ('MGF', 'MGF'), ('BEC', 'BEC'), ('MXV', 'MXV'), ('UYP', 'UYP'), ('GHS', 'GHS'), ('CHW', 'CHW'), ('XBD', 'XBD'), ('ALK', 'ALK'), ('NGN', 'NGN'), ('RUB', 'RUB'), ('ERN', 'ERN'), ('BUK', 'BUK'), ('PAB', 'PAB'), ('PGK', 'PGK'), ('LTT', 'LTT'), ('HNL', 'HNL'), ('RHD', 'RHD'), ('VUV', 'VUV'), ('TJR', 'TJR'), ('STD', 'STD'), ('PEI', 'PEI'), ('BND', 'BND'), ('XFU', 'XFU'), ('BOV', 'BOV'), ('TTD', 'TTD'), ('ISK', 'ISK'), ('XFO', 'XFO'), ('AED', 'AED'), ('VEB', 'VEB'), ('XEU', 'XEU'), ('SVC', 'SVC'), ('AFN', 'AFN'), ('DDM', 'DDM'), ('BOL', 'BOL'), ('ARM', 'ARM'), ('GWE', 'GWE'), ('PEN', 'PEN'), ('TZS', 'TZS'), ('ANG', 'ANG'), ('ESB', 'ESB'), ('PES', 'PES'), ('MXP', 'MXP'), ('UAH', 'UAH'), ('AOA', 'AOA'), ('BGO', 'BGO'), ('TRL', 'TRL'), ('USN', 'USN'), ('GNF', 'GNF'), ('GEL', 'GEL'), ('JOD', 'JOD'), ('RUR', 'RUR'), ('CLP', 'CLP'), ('ALL', 'ALL'), ('BYB', 'BYB'), ('GNS', 'GNS'), ('UYI', 'UYI'), ('VND', 'VND'), ('XPT', 'XPT'), ('SDG', 'SDG'), ('YUN', 'YUN'), ('KHR', 'KHR'), ('MZM', 'MZM'), ('BSD', 'BSD'), ('NLG', 'NLG'), ('GRD', 'GRD'), ('DEM', 'DEM'), ('KPW', 'KPW'), ('SRD', 'SRD'), ('PKR', 'PKR'), ('ILR', 'ILR'), ('ESP', 'ESP'), ('NOK', 'NOK'), ('IQD', 'IQD'), ('LAK', 'LAK'), ('CNX', 'CNX'), ('BGL', 'BGL'), ('GMD', 'GMD'), ('XBA', 'XBA'), ('FJD', 'FJD'), ('AWG', 'AWG'), ('ILS', 'ILS'), ('NIO', 'NIO'), ('XXX', 'XXX'), ('JMD', 'JMD'), ('ZMK', 'ZMK'), ('ZWL', 'ZWL'), ('ITL', 'ITL'), ('XDR', 'XDR'), ('BRL', 'BRL'), ('KMF', 'KMF'), ('CHF', 'CHF'), ('ECS', 'ECS'), ('MXN', 'MXN'), ('ILP', 'ILP'), ('OMR', 'OMR'), ('SIT', 'SIT'), ('UZS', 'UZS'), ('CDF', 'CDF'), ('CVE', 'CVE'), ('XPD', 'XPD'), ('WST', 'WST'), ('MOP', 'MOP'), ('MMK', 'MMK'), ('MKD', 'MKD'), ('SOS', 'SOS'), ('PLZ', 'PLZ'), ('SBD', 'SBD'), ('CRC', 'CRC'), ('GTQ', 'GTQ'), ('MRO', 'MRO'), ('ECV', 'ECV'), ('GYD', 'GYD'), ('BTN', 'BTN'), ('BDT', 'BDT'), ('GEK', 'GEK'), ('LRD', 'LRD'), ('ESA', 'ESA'), ('UGX', 'UGX'), ('INR', 'INR'), ('ZRN', 'ZRN'), ('ARS', 'ARS'), ('MUR', 'MUR'), ('SLL', 'SLL'), ('XUA', 'XUA'), ('CHE', 'CHE'), ('CYP', 'CYP'), ('LUC', 'LUC'), ('ZAR', 'ZAR'), ('MCF', 'MCF'), ('CLE', 'CLE'), ('SEK', 'SEK'), ('SUR', 'SUR'), ('NZD', 'NZD'), ('LUF', 'LUF'), ('KES', 'KES'), ('LBP', 'LBP'), ('BRE', 'BRE'), ('SYP', 'SYP'), ('BOP', 'BOP'), ('ETB', 'ETB'), ('COU', 'COU'), ('MDL', 'MDL'), ('BIF', 'BIF'), ('TJS', 'TJS'), ('KYD', 'KYD'), ('BAD', 'BAD'), ('HRD', 'HRD'), ('LVR', 'LVR'), ('KRO', 'KRO'), ('SGD', 'SGD'), ('HKD', 'HKD'), ('HUF', 'HUF'), ('SDP', 'SDP'), ('COP', 'COP'), ('ZAL', 'ZAL'), ('ZMW', 'ZMW'), ('CSK', 'CSK'), ('GIP', 'GIP'), ('KGS', 'KGS'), ('PHP', 'PHP'), ('MWK', 'MWK'), ('BAM', 'BAM'), ('BEL', 'BEL'), ('DZD', 'DZD'), ('IEP', 'IEP'), ('RSD', 'RSD'), ('BZD', 'BZD'), ('ARA', 'ARA'), ('CZK', 'CZK'), ('KWD', 'KWD'), ('XSU', 'XSU'), ('TWD', 'TWD'), ('ZRZ', 'ZRZ'), ('MDC', 'MDC'), ('ADP', 'ADP'), ('BOB', 'BOB'), ('KZT', 'KZT'), ('XBC', 'XBC'), ('GWP', 'GWP'), ('AZM', 'AZM'), ('MKN', 'MKN'), ('XAU', 'XAU'), ('MZE', 'MZE'), ('BWP', 'BWP'), ('CSD', 'CSD'), ('XCD', 'XCD'), ('YUM', 'YUM'), ('FKP', 'FKP'), ('ISJ', 'ISJ'), ('BYN', 'BYN'), ('YER', 'YER'), ('MAD', 'MAD'), ('XAF', 'XAF'), ('UYU', 'UYU'), ('TMM', 'TMM'), ('BHD', 'BHD'), ('BGM', 'BGM'), ('MNT', 'MNT'), ('BEF', 'BEF'), ('XAG', 'XAG'), ('CNY', 'CNY'), ('MAF', 'MAF'), ('BRC', 'BRC'), ('BGN', 'BGN'), ('GQE', 'GQE'), ('QAR', 'QAR'), ('MRU', 'MRU'), ('ARP', 'ARP'), ('SSP', 'SSP'), ('DOP', 'DOP'), ('UGS', 'UGS'), ('RWF', 'RWF'), ('AON', 'AON'), ('ARL', 'ARL'), ('DKK', 'DKK'), ('MZN', 'MZN'), ('TRY', 'TRY'), ('LSL', 'LSL'), ('GBP', 'GBP'), ('MVR', 'MVR'), ('PLN', 'PLN'), ('NPR', 'NPR'), ('RON', 'RON'), ('USD', 'USD'), ('UYW', 'UYW'), ('AOK', 'AOK'), ('LUL', 'LUL'), ('JPY', 'JPY'), ('YUR', 'YUR'), ('BAN', 'BAN'), ('AZN', 'AZN'), ('CAD', 'CAD'), ('KRH', 'KRH'), ('BRN', 'BRN'), ('LVL', 'LVL'), ('XPF', 'XPF'), ('TND', 'TND'), ('ROL', 'ROL'), ('GHC', 'GHC'), ('BMD', 'BMD'), ('XTS', 'XTS'), ('SZL', 'SZL'), ('AMD', 'AMD'), ('MLF', 'MLF'), ('MVP', 'MVP'), ('XOF', 'XOF'), ('SKK', 'SKK'), ('LKR', 'LKR'), ('EGP', 'EGP'), ('MGA', 'MGA'), ('AUD', 'AUD'), ('BRR', 'BRR'), ('THB', 'THB'), ('VNN', 'VNN'), ('MYR', 'MYR'), ('TPE', 'TPE'), ('ZWD', 'ZWD'), ('YUD', 'YUD'), ('HTG', 'HTG'), ('MTL', 'MTL'), ('IRR', 'IRR'), ('ATS', 'ATS'), ('USS', 'USS'), ('NIC', 'NIC'), ('VES', 'VES'), ('EEK', 'EEK'), ('CNH', 'CNH'), ('LTL', 'LTL'), ('SDD', 'SDD'), ('SCR', 'SCR'), ('CUC', 'CUC'), ('MTP', 'MTP'), ('SRG', 'SRG'), ('LYD', 'LYD'), ('TOP', 'TOP'), ('FIM', 'FIM'), ('UAK', 'UAK'), ('VEF', 'VEF'), ('SHP', 'SHP'), ('BYR', 'BYR'), ('BRZ', 'BRZ'), ('BBD', 'BBD')], max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
