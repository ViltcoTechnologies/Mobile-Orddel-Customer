# Generated by Django 3.1.5 on 2021-01-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20210121_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('ZAL', 'ZAL'), ('XOF', 'XOF'), ('USS', 'USS'), ('LUC', 'LUC'), ('MGA', 'MGA'), ('BMD', 'BMD'), ('KRO', 'KRO'), ('WST', 'WST'), ('ARA', 'ARA'), ('PTE', 'PTE'), ('XXX', 'XXX'), ('AUD', 'AUD'), ('USD', 'USD'), ('BRB', 'BRB'), ('GHC', 'GHC'), ('ERN', 'ERN'), ('ILR', 'ILR'), ('BRL', 'BRL'), ('LSL', 'LSL'), ('KRW', 'KRW'), ('NGN', 'NGN'), ('THB', 'THB'), ('ILP', 'ILP'), ('GHS', 'GHS'), ('ISK', 'ISK'), ('RSD', 'RSD'), ('UGX', 'UGX'), ('FRF', 'FRF'), ('JMD', 'JMD'), ('ISJ', 'ISJ'), ('AON', 'AON'), ('UAK', 'UAK'), ('SEK', 'SEK'), ('VES', 'VES'), ('NAD', 'NAD'), ('SCR', 'SCR'), ('NIC', 'NIC'), ('BYB', 'BYB'), ('PGK', 'PGK'), ('TMT', 'TMT'), ('MGF', 'MGF'), ('MRO', 'MRO'), ('PYG', 'PYG'), ('BGM', 'BGM'), ('ZWD', 'ZWD'), ('ZMK', 'ZMK'), ('XFU', 'XFU'), ('ARM', 'ARM'), ('BOB', 'BOB'), ('MXN', 'MXN'), ('STN', 'STN'), ('BRR', 'BRR'), ('COU', 'COU'), ('MYR', 'MYR'), ('MUR', 'MUR'), ('NOK', 'NOK'), ('SRD', 'SRD'), ('HTG', 'HTG'), ('RUR', 'RUR'), ('MZN', 'MZN'), ('VEB', 'VEB'), ('XTS', 'XTS'), ('ZAR', 'ZAR'), ('IEP', 'IEP'), ('TND', 'TND'), ('CNX', 'CNX'), ('CAD', 'CAD'), ('UYI', 'UYI'), ('LVL', 'LVL'), ('SBD', 'SBD'), ('VUV', 'VUV'), ('AZN', 'AZN'), ('DKK', 'DKK'), ('MZE', 'MZE'), ('BWP', 'BWP'), ('CSD', 'CSD'), ('DZD', 'DZD'), ('XSU', 'XSU'), ('AOA', 'AOA'), ('DDM', 'DDM'), ('KGS', 'KGS'), ('XBD', 'XBD'), ('MLF', 'MLF'), ('CNY', 'CNY'), ('BZD', 'BZD'), ('GMD', 'GMD'), ('VEF', 'VEF'), ('LAK', 'LAK'), ('MDL', 'MDL'), ('MKD', 'MKD'), ('CLF', 'CLF'), ('KYD', 'KYD'), ('DEM', 'DEM'), ('XFO', 'XFO'), ('HRK', 'HRK'), ('YUD', 'YUD'), ('INR', 'INR'), ('LBP', 'LBP'), ('GEK', 'GEK'), ('ANG', 'ANG'), ('RON', 'RON'), ('CLE', 'CLE'), ('DOP', 'DOP'), ('PAB', 'PAB'), ('ZRN', 'ZRN'), ('SYP', 'SYP'), ('MDC', 'MDC'), ('BOP', 'BOP'), ('EGP', 'EGP'), ('XAF', 'XAF'), ('CHF', 'CHF'), ('IRR', 'IRR'), ('GNF', 'GNF'), ('GYD', 'GYD'), ('BYN', 'BYN'), ('ALK', 'ALK'), ('NPR', 'NPR'), ('AFA', 'AFA'), ('XBB', 'XBB'), ('UYW', 'UYW'), ('MTL', 'MTL'), ('BGL', 'BGL'), ('AOK', 'AOK'), ('UZS', 'UZS'), ('VND', 'VND'), ('AED', 'AED'), ('XPF', 'XPF'), ('MNT', 'MNT'), ('TPE', 'TPE'), ('CDF', 'CDF'), ('BSD', 'BSD'), ('GRD', 'GRD'), ('AFN', 'AFN'), ('KPW', 'KPW'), ('MXV', 'MXV'), ('RHD', 'RHD'), ('SOS', 'SOS'), ('SHP', 'SHP'), ('PHP', 'PHP'), ('CHW', 'CHW'), ('EUR', 'EUR'), ('USN', 'USN'), ('FIM', 'FIM'), ('BEF', 'BEF'), ('BTN', 'BTN'), ('CUC', 'CUC'), ('ILS', 'ILS'), ('BHD', 'BHD'), ('SDD', 'SDD'), ('ECV', 'ECV'), ('LUL', 'LUL'), ('LTL', 'LTL'), ('PEI', 'PEI'), ('ESB', 'ESB'), ('NZD', 'NZD'), ('TZS', 'TZS'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('LKR', 'LKR'), ('AMD', 'AMD'), ('COP', 'COP'), ('YUM', 'YUM'), ('SKK', 'SKK'), ('SLL', 'SLL'), ('BRE', 'BRE'), ('RWF', 'RWF'), ('UYU', 'UYU'), ('XBA', 'XBA'), ('ZMW', 'ZMW'), ('CRC', 'CRC'), ('BOL', 'BOL'), ('LYD', 'LYD'), ('XEU', 'XEU'), ('JPY', 'JPY'), ('ATS', 'ATS'), ('PLN', 'PLN'), ('KZT', 'KZT'), ('CSK', 'CSK'), ('BIF', 'BIF'), ('CYP', 'CYP'), ('OMR', 'OMR'), ('QAR', 'QAR'), ('MRU', 'MRU'), ('BOV', 'BOV'), ('JOD', 'JOD'), ('PEN', 'PEN'), ('GTQ', 'GTQ'), ('TRY', 'TRY'), ('FKP', 'FKP'), ('ALL', 'ALL'), ('CHE', 'CHE'), ('PKR', 'PKR'), ('STD', 'STD'), ('TJS', 'TJS'), ('XCD', 'XCD'), ('ZRZ', 'ZRZ'), ('IDR', 'IDR'), ('XAU', 'XAU'), ('XAG', 'XAG'), ('KWD', 'KWD'), ('BND', 'BND'), ('AZM', 'AZM'), ('GWP', 'GWP'), ('BGO', 'BGO'), ('XUA', 'XUA'), ('TRL', 'TRL'), ('HNL', 'HNL'), ('LUF', 'LUF'), ('ARP', 'ARP'), ('MAF', 'MAF'), ('PES', 'PES'), ('BYR', 'BYR'), ('MCF', 'MCF'), ('CNH', 'CNH'), ('KHR', 'KHR'), ('MWK', 'MWK'), ('SDP', 'SDP'), ('TWD', 'TWD'), ('DJF', 'DJF'), ('HUF', 'HUF'), ('BGN', 'BGN'), ('MOP', 'MOP'), ('PLZ', 'PLZ'), ('CZK', 'CZK'), ('GWE', 'GWE'), ('LRD', 'LRD'), ('ADP', 'ADP'), ('TTD', 'TTD'), ('BAD', 'BAD'), ('XBC', 'XBC'), ('CVE', 'CVE'), ('ESA', 'ESA'), ('TOP', 'TOP'), ('HRD', 'HRD'), ('RUB', 'RUB'), ('KMF', 'KMF'), ('YUR', 'YUR'), ('SGD', 'SGD'), ('LVR', 'LVR'), ('ROL', 'ROL'), ('BRC', 'BRC'), ('XPD', 'XPD'), ('HKD', 'HKD'), ('BEC', 'BEC'), ('CLP', 'CLP'), ('FJD', 'FJD'), ('MVP', 'MVP'), ('YER', 'YER'), ('ZWR', 'ZWR'), ('BRZ', 'BRZ'), ('ARS', 'ARS'), ('ARL', 'ARL'), ('MXP', 'MXP'), ('ECS', 'ECS'), ('SIT', 'SIT'), ('YDD', 'YDD'), ('SSP', 'SSP'), ('MKN', 'MKN'), ('GQE', 'GQE'), ('KES', 'KES'), ('KRH', 'KRH'), ('TJR', 'TJR'), ('BUK', 'BUK'), ('MVR', 'MVR'), ('MTP', 'MTP'), ('SDG', 'SDG'), ('BAN', 'BAN'), ('MZM', 'MZM'), ('MAD', 'MAD'), ('ITL', 'ITL'), ('XRE', 'XRE'), ('SZL', 'SZL'), ('TMM', 'TMM'), ('AOR', 'AOR'), ('XDR', 'XDR'), ('BEL', 'BEL'), ('ESP', 'ESP'), ('SRG', 'SRG'), ('GNS', 'GNS'), ('IQD', 'IQD'), ('ETB', 'ETB'), ('SAR', 'SAR'), ('GIP', 'GIP'), ('EEK', 'EEK'), ('BRN', 'BRN'), ('ZWL', 'ZWL'), ('NIO', 'NIO'), ('BBD', 'BBD'), ('XPT', 'XPT'), ('SUR', 'SUR'), ('SVC', 'SVC'), ('CUP', 'CUP'), ('VNN', 'VNN'), ('UGS', 'UGS'), ('BDT', 'BDT'), ('AWG', 'AWG'), ('UYP', 'UYP'), ('BAM', 'BAM'), ('LTT', 'LTT'), ('MMK', 'MMK'), ('UAH', 'UAH'), ('NLG', 'NLG'), ('YUN', 'YUN')], max_length=100),
        ),
    ]
