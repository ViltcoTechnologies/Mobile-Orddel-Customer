# Generated by Django 3.1.4 on 2021-01-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20210113_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('MXN', 'MXN'), ('MRO', 'MRO'), ('USD', 'USD'), ('UZS', 'UZS'), ('DJF', 'DJF'), ('RSD', 'RSD'), ('GRD', 'GRD'), ('CUC', 'CUC'), ('HUF', 'HUF'), ('NLG', 'NLG'), ('LUF', 'LUF'), ('BAM', 'BAM'), ('XTS', 'XTS'), ('XBB', 'XBB'), ('SUR', 'SUR'), ('VND', 'VND'), ('BYN', 'BYN'), ('BRL', 'BRL'), ('TRL', 'TRL'), ('GWE', 'GWE'), ('KES', 'KES'), ('PES', 'PES'), ('YUR', 'YUR'), ('MGF', 'MGF'), ('CHW', 'CHW'), ('ECS', 'ECS'), ('PYG', 'PYG'), ('BTN', 'BTN'), ('ZWL', 'ZWL'), ('STN', 'STN'), ('TJS', 'TJS'), ('CLE', 'CLE'), ('ARL', 'ARL'), ('JOD', 'JOD'), ('XCD', 'XCD'), ('TND', 'TND'), ('BRB', 'BRB'), ('XAG', 'XAG'), ('ZWD', 'ZWD'), ('COP', 'COP'), ('BDT', 'BDT'), ('OMR', 'OMR'), ('BUK', 'BUK'), ('RHD', 'RHD'), ('CNH', 'CNH'), ('HTG', 'HTG'), ('UYP', 'UYP'), ('XFU', 'XFU'), ('BGO', 'BGO'), ('ILS', 'ILS'), ('ETB', 'ETB'), ('AZM', 'AZM'), ('CLP', 'CLP'), ('DZD', 'DZD'), ('PEN', 'PEN'), ('GEL', 'GEL'), ('MXP', 'MXP'), ('CNY', 'CNY'), ('CSD', 'CSD'), ('DEM', 'DEM'), ('ILR', 'ILR'), ('AZN', 'AZN'), ('KMF', 'KMF'), ('PTE', 'PTE'), ('KRW', 'KRW'), ('SGD', 'SGD'), ('MOP', 'MOP'), ('XBA', 'XBA'), ('CSK', 'CSK'), ('GHC', 'GHC'), ('ZRN', 'ZRN'), ('XPT', 'XPT'), ('LSL', 'LSL'), ('ZRZ', 'ZRZ'), ('MTP', 'MTP'), ('ALL', 'ALL'), ('PAB', 'PAB'), ('XPF', 'XPF'), ('CUP', 'CUP'), ('MLF', 'MLF'), ('ECV', 'ECV'), ('GBP', 'GBP'), ('FRF', 'FRF'), ('ADP', 'ADP'), ('YUM', 'YUM'), ('ZWR', 'ZWR'), ('KWD', 'KWD'), ('VEF', 'VEF'), ('SRD', 'SRD'), ('SAR', 'SAR'), ('BRZ', 'BRZ'), ('LTT', 'LTT'), ('LKR', 'LKR'), ('BGL', 'BGL'), ('GTQ', 'GTQ'), ('EUR', 'EUR'), ('BEL', 'BEL'), ('UYU', 'UYU'), ('JPY', 'JPY'), ('AFA', 'AFA'), ('LUC', 'LUC'), ('AOK', 'AOK'), ('LYD', 'LYD'), ('IRR', 'IRR'), ('PLZ', 'PLZ'), ('GEK', 'GEK'), ('SKK', 'SKK'), ('LAK', 'LAK'), ('FIM', 'FIM'), ('CNX', 'CNX'), ('ANG', 'ANG'), ('ROL', 'ROL'), ('KYD', 'KYD'), ('YER', 'YER'), ('GIP', 'GIP'), ('LVR', 'LVR'), ('BRN', 'BRN'), ('STD', 'STD'), ('KRH', 'KRH'), ('AED', 'AED'), ('SLL', 'SLL'), ('COU', 'COU'), ('VEB', 'VEB'), ('EEK', 'EEK'), ('NIO', 'NIO'), ('AON', 'AON'), ('SRG', 'SRG'), ('XUA', 'XUA'), ('INR', 'INR'), ('PHP', 'PHP'), ('TRY', 'TRY'), ('VES', 'VES'), ('SEK', 'SEK'), ('XXX', 'XXX'), ('CDF', 'CDF'), ('MZN', 'MZN'), ('MVP', 'MVP'), ('DKK', 'DKK'), ('GMD', 'GMD'), ('XSU', 'XSU'), ('HRK', 'HRK'), ('BRE', 'BRE'), ('AWG', 'AWG'), ('YDD', 'YDD'), ('TTD', 'TTD'), ('ZMW', 'ZMW'), ('ZAL', 'ZAL'), ('UYI', 'UYI'), ('MDC', 'MDC'), ('ESB', 'ESB'), ('NGN', 'NGN'), ('SDP', 'SDP'), ('CHF', 'CHF'), ('AFN', 'AFN'), ('BRC', 'BRC'), ('HRD', 'HRD'), ('FJD', 'FJD'), ('GYD', 'GYD'), ('VNN', 'VNN'), ('XEU', 'XEU'), ('CYP', 'CYP'), ('HKD', 'HKD'), ('RUR', 'RUR'), ('KHR', 'KHR'), ('GNS', 'GNS'), ('MKD', 'MKD'), ('YUD', 'YUD'), ('TMT', 'TMT'), ('AOA', 'AOA'), ('UYW', 'UYW'), ('CHE', 'CHE'), ('BSD', 'BSD'), ('ARA', 'ARA'), ('BHD', 'BHD'), ('GQE', 'GQE'), ('ATS', 'ATS'), ('LTL', 'LTL'), ('TOP', 'TOP'), ('XPD', 'XPD'), ('RUB', 'RUB'), ('JMD', 'JMD'), ('LRD', 'LRD'), ('ERN', 'ERN'), ('BZD', 'BZD'), ('MAF', 'MAF'), ('SZL', 'SZL'), ('MZM', 'MZM'), ('NOK', 'NOK'), ('BBD', 'BBD'), ('KZT', 'KZT'), ('XFO', 'XFO'), ('WST', 'WST'), ('XOF', 'XOF'), ('CVE', 'CVE'), ('NAD', 'NAD'), ('BEF', 'BEF'), ('SOS', 'SOS'), ('THB', 'THB'), ('SHP', 'SHP'), ('GHS', 'GHS'), ('TPE', 'TPE'), ('AOR', 'AOR'), ('MDL', 'MDL'), ('BND', 'BND'), ('SDD', 'SDD'), ('TZS', 'TZS'), ('MZE', 'MZE'), ('SIT', 'SIT'), ('PGK', 'PGK'), ('BGM', 'BGM'), ('BIF', 'BIF'), ('ESA', 'ESA'), ('BEC', 'BEC'), ('PEI', 'PEI'), ('ARM', 'ARM'), ('SBD', 'SBD'), ('MVR', 'MVR'), ('SYP', 'SYP'), ('ZMK', 'ZMK'), ('XAU', 'XAU'), ('MYR', 'MYR'), ('MAD', 'MAD'), ('USS', 'USS'), ('TWD', 'TWD'), ('MUR', 'MUR'), ('TMM', 'TMM'), ('CLF', 'CLF'), ('ITL', 'ITL'), ('LBP', 'LBP'), ('SSP', 'SSP'), ('DOP', 'DOP'), ('BOP', 'BOP'), ('CZK', 'CZK'), ('MTL', 'MTL'), ('NPR', 'NPR'), ('IEP', 'IEP'), ('SCR', 'SCR'), ('ARP', 'ARP'), ('IDR', 'IDR'), ('MGA', 'MGA'), ('UGS', 'UGS'), ('UGX', 'UGX'), ('BRR', 'BRR'), ('KRO', 'KRO'), ('AUD', 'AUD'), ('AMD', 'AMD'), ('ILP', 'ILP'), ('ZAR', 'ZAR'), ('MCF', 'MCF'), ('DDM', 'DDM'), ('BWP', 'BWP'), ('ALK', 'ALK'), ('KGS', 'KGS'), ('ARS', 'ARS'), ('UAK', 'UAK'), ('USN', 'USN'), ('XDR', 'XDR'), ('SDG', 'SDG'), ('GNF', 'GNF'), ('SVC', 'SVC'), ('MWK', 'MWK'), ('UAH', 'UAH'), ('KPW', 'KPW'), ('XBC', 'XBC'), ('PLN', 'PLN'), ('CRC', 'CRC'), ('NZD', 'NZD'), ('BOV', 'BOV'), ('HNL', 'HNL'), ('MRU', 'MRU'), ('MKN', 'MKN'), ('RON', 'RON'), ('BAD', 'BAD'), ('PKR', 'PKR'), ('GWP', 'GWP'), ('BAN', 'BAN'), ('FKP', 'FKP'), ('ISJ', 'ISJ'), ('YUN', 'YUN'), ('XBD', 'XBD'), ('BYB', 'BYB'), ('XAF', 'XAF'), ('LUL', 'LUL'), ('NIC', 'NIC'), ('XRE', 'XRE'), ('LVL', 'LVL'), ('CAD', 'CAD'), ('ISK', 'ISK'), ('BMD', 'BMD'), ('EGP', 'EGP'), ('QAR', 'QAR'), ('IQD', 'IQD'), ('BOL', 'BOL'), ('ESP', 'ESP'), ('RWF', 'RWF'), ('BGN', 'BGN'), ('MMK', 'MMK'), ('MXV', 'MXV'), ('MNT', 'MNT'), ('TJR', 'TJR'), ('VUV', 'VUV'), ('BYR', 'BYR'), ('BOB', 'BOB')], max_length=100),
        ),
    ]
