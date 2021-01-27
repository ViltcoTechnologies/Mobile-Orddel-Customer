# Generated by Django 3.1.4 on 2021-01-21 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210121_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('GWE', 'GWE'), ('BAN', 'BAN'), ('CUC', 'CUC'), ('MKN', 'MKN'), ('SLL', 'SLL'), ('CDF', 'CDF'), ('KHR', 'KHR'), ('KRW', 'KRW'), ('HRK', 'HRK'), ('BAM', 'BAM'), ('BRR', 'BRR'), ('BGM', 'BGM'), ('RUR', 'RUR'), ('BRC', 'BRC'), ('GQE', 'GQE'), ('RUB', 'RUB'), ('STN', 'STN'), ('TZS', 'TZS'), ('DOP', 'DOP'), ('SZL', 'SZL'), ('RWF', 'RWF'), ('MZE', 'MZE'), ('NPR', 'NPR'), ('XBD', 'XBD'), ('PLZ', 'PLZ'), ('CLE', 'CLE'), ('FIM', 'FIM'), ('LVR', 'LVR'), ('KES', 'KES'), ('XAU', 'XAU'), ('KGS', 'KGS'), ('GMD', 'GMD'), ('WST', 'WST'), ('XAF', 'XAF'), ('AZN', 'AZN'), ('BRB', 'BRB'), ('MDL', 'MDL'), ('SGD', 'SGD'), ('BEF', 'BEF'), ('CNX', 'CNX'), ('TMT', 'TMT'), ('BGL', 'BGL'), ('LVL', 'LVL'), ('MUR', 'MUR'), ('KWD', 'KWD'), ('TRL', 'TRL'), ('ZMK', 'ZMK'), ('IQD', 'IQD'), ('STD', 'STD'), ('BOB', 'BOB'), ('CNH', 'CNH'), ('XSU', 'XSU'), ('ESP', 'ESP'), ('CHE', 'CHE'), ('ISK', 'ISK'), ('OMR', 'OMR'), ('BRL', 'BRL'), ('LRD', 'LRD'), ('DJF', 'DJF'), ('SAR', 'SAR'), ('AUD', 'AUD'), ('UAH', 'UAH'), ('COU', 'COU'), ('ARL', 'ARL'), ('BHD', 'BHD'), ('MYR', 'MYR'), ('MXP', 'MXP'), ('BUK', 'BUK'), ('BOV', 'BOV'), ('XTS', 'XTS'), ('SUR', 'SUR'), ('ZRZ', 'ZRZ'), ('ANG', 'ANG'), ('AZM', 'AZM'), ('GRD', 'GRD'), ('UGS', 'UGS'), ('GTQ', 'GTQ'), ('XBA', 'XBA'), ('MWK', 'MWK'), ('MRU', 'MRU'), ('LTT', 'LTT'), ('AOA', 'AOA'), ('AOK', 'AOK'), ('LUL', 'LUL'), ('BGN', 'BGN'), ('MGF', 'MGF'), ('SOS', 'SOS'), ('JMD', 'JMD'), ('DEM', 'DEM'), ('PKR', 'PKR'), ('YDD', 'YDD'), ('ECS', 'ECS'), ('XRE', 'XRE'), ('INR', 'INR'), ('THB', 'THB'), ('PYG', 'PYG'), ('IDR', 'IDR'), ('XDR', 'XDR'), ('UYI', 'UYI'), ('ZRN', 'ZRN'), ('XPD', 'XPD'), ('GHS', 'GHS'), ('GEL', 'GEL'), ('CYP', 'CYP'), ('GNS', 'GNS'), ('EEK', 'EEK'), ('XAG', 'XAG'), ('PEI', 'PEI'), ('ILP', 'ILP'), ('LYD', 'LYD'), ('BOL', 'BOL'), ('XFO', 'XFO'), ('BBD', 'BBD'), ('BND', 'BND'), ('MXV', 'MXV'), ('NOK', 'NOK'), ('NGN', 'NGN'), ('LAK', 'LAK'), ('GBP', 'GBP'), ('MMK', 'MMK'), ('BEC', 'BEC'), ('PGK', 'PGK'), ('KPW', 'KPW'), ('TPE', 'TPE'), ('QAR', 'QAR'), ('ECV', 'ECV'), ('BIF', 'BIF'), ('JPY', 'JPY'), ('BAD', 'BAD'), ('GWP', 'GWP'), ('YER', 'YER'), ('ZWR', 'ZWR'), ('DKK', 'DKK'), ('JOD', 'JOD'), ('BTN', 'BTN'), ('UZS', 'UZS'), ('HNL', 'HNL'), ('YUR', 'YUR'), ('CLF', 'CLF'), ('BZD', 'BZD'), ('SIT', 'SIT'), ('USD', 'USD'), ('BYN', 'BYN'), ('FKP', 'FKP'), ('LUF', 'LUF'), ('KRO', 'KRO'), ('XOF', 'XOF'), ('TTD', 'TTD'), ('AED', 'AED'), ('TMM', 'TMM'), ('VND', 'VND'), ('HKD', 'HKD'), ('LUC', 'LUC'), ('IRR', 'IRR'), ('PES', 'PES'), ('CAD', 'CAD'), ('DZD', 'DZD'), ('ALL', 'ALL'), ('BSD', 'BSD'), ('BEL', 'BEL'), ('GYD', 'GYD'), ('CUP', 'CUP'), ('HRD', 'HRD'), ('TJS', 'TJS'), ('ZWL', 'ZWL'), ('GIP', 'GIP'), ('TJR', 'TJR'), ('NZD', 'NZD'), ('ERN', 'ERN'), ('SBD', 'SBD'), ('VEF', 'VEF'), ('ZMW', 'ZMW'), ('SRG', 'SRG'), ('HUF', 'HUF'), ('SSP', 'SSP'), ('MAD', 'MAD'), ('ARS', 'ARS'), ('UYW', 'UYW'), ('BMD', 'BMD'), ('MZN', 'MZN'), ('NIO', 'NIO'), ('FRF', 'FRF'), ('ARM', 'ARM'), ('MOP', 'MOP'), ('AON', 'AON'), ('KRH', 'KRH'), ('CZK', 'CZK'), ('CHW', 'CHW'), ('AMD', 'AMD'), ('VEB', 'VEB'), ('SDP', 'SDP'), ('ARA', 'ARA'), ('MNT', 'MNT'), ('BRE', 'BRE'), ('NIC', 'NIC'), ('TND', 'TND'), ('RSD', 'RSD'), ('AOR', 'AOR'), ('MGA', 'MGA'), ('VUV', 'VUV'), ('GNF', 'GNF'), ('ZAR', 'ZAR'), ('MRO', 'MRO'), ('ADP', 'ADP'), ('PTE', 'PTE'), ('MKD', 'MKD'), ('AFN', 'AFN'), ('AWG', 'AWG'), ('ETB', 'ETB'), ('MTP', 'MTP'), ('LSL', 'LSL'), ('SVC', 'SVC'), ('MAF', 'MAF'), ('ITL', 'ITL'), ('PEN', 'PEN'), ('BYB', 'BYB'), ('UYP', 'UYP'), ('MDC', 'MDC'), ('KZT', 'KZT'), ('SHP', 'SHP'), ('AFA', 'AFA'), ('COP', 'COP'), ('VNN', 'VNN'), ('MZM', 'MZM'), ('EGP', 'EGP'), ('HTG', 'HTG'), ('SRD', 'SRD'), ('TWD', 'TWD'), ('IEP', 'IEP'), ('VES', 'VES'), ('CRC', 'CRC'), ('ARP', 'ARP'), ('RHD', 'RHD'), ('XUA', 'XUA'), ('EUR', 'EUR'), ('MCF', 'MCF'), ('YUN', 'YUN'), ('LKR', 'LKR'), ('MVR', 'MVR'), ('UYU', 'UYU'), ('RON', 'RON'), ('TOP', 'TOP'), ('UGX', 'UGX'), ('BGO', 'BGO'), ('MLF', 'MLF'), ('LTL', 'LTL'), ('BYR', 'BYR'), ('ESA', 'ESA'), ('SYP', 'SYP'), ('BRZ', 'BRZ'), ('ILS', 'ILS'), ('CNY', 'CNY'), ('ZAL', 'ZAL'), ('CHF', 'CHF'), ('GHC', 'GHC'), ('SCR', 'SCR'), ('XFU', 'XFU'), ('CLP', 'CLP'), ('ZWD', 'ZWD'), ('CSD', 'CSD'), ('FJD', 'FJD'), ('GEK', 'GEK'), ('XXX', 'XXX'), ('PLN', 'PLN'), ('CSK', 'CSK'), ('NAD', 'NAD'), ('XEU', 'XEU'), ('MXN', 'MXN'), ('ALK', 'ALK'), ('UAK', 'UAK'), ('USS', 'USS'), ('ILR', 'ILR'), ('MTL', 'MTL'), ('KMF', 'KMF'), ('XBB', 'XBB'), ('ATS', 'ATS'), ('PHP', 'PHP'), ('DDM', 'DDM'), ('TRY', 'TRY'), ('NLG', 'NLG'), ('ISJ', 'ISJ'), ('BDT', 'BDT'), ('KYD', 'KYD'), ('ROL', 'ROL'), ('USN', 'USN'), ('BRN', 'BRN'), ('BOP', 'BOP'), ('MVP', 'MVP'), ('SKK', 'SKK'), ('SDD', 'SDD'), ('LBP', 'LBP'), ('ESB', 'ESB'), ('XPF', 'XPF'), ('YUD', 'YUD'), ('CVE', 'CVE'), ('PAB', 'PAB'), ('SEK', 'SEK'), ('XPT', 'XPT'), ('XCD', 'XCD'), ('BWP', 'BWP'), ('YUM', 'YUM'), ('XBC', 'XBC'), ('SDG', 'SDG')], max_length=100),
        ),
    ]
