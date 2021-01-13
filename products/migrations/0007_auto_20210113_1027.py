# Generated by Django 3.1.5 on 2021-01-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210113_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('UYI', 'UYI'), ('ARA', 'ARA'), ('AOR', 'AOR'), ('BRZ', 'BRZ'), ('CRC', 'CRC'), ('CNX', 'CNX'), ('MTP', 'MTP'), ('TJR', 'TJR'), ('ITL', 'ITL'), ('HNL', 'HNL'), ('ZRZ', 'ZRZ'), ('SYP', 'SYP'), ('SGD', 'SGD'), ('SVC', 'SVC'), ('BSD', 'BSD'), ('MAF', 'MAF'), ('ZWL', 'ZWL'), ('NGN', 'NGN'), ('ETB', 'ETB'), ('IRR', 'IRR'), ('SDD', 'SDD'), ('MRO', 'MRO'), ('KRW', 'KRW'), ('RUR', 'RUR'), ('GWE', 'GWE'), ('GIP', 'GIP'), ('XBA', 'XBA'), ('NPR', 'NPR'), ('SDG', 'SDG'), ('VES', 'VES'), ('YUM', 'YUM'), ('ECV', 'ECV'), ('BEF', 'BEF'), ('DDM', 'DDM'), ('AZN', 'AZN'), ('XFO', 'XFO'), ('ECS', 'ECS'), ('MKN', 'MKN'), ('BIF', 'BIF'), ('ATS', 'ATS'), ('MZM', 'MZM'), ('OMR', 'OMR'), ('LUC', 'LUC'), ('NIO', 'NIO'), ('TMT', 'TMT'), ('ALL', 'ALL'), ('LTT', 'LTT'), ('MTL', 'MTL'), ('HKD', 'HKD'), ('PEI', 'PEI'), ('SEK', 'SEK'), ('WST', 'WST'), ('BMD', 'BMD'), ('TND', 'TND'), ('KES', 'KES'), ('UYP', 'UYP'), ('BGL', 'BGL'), ('YUR', 'YUR'), ('FJD', 'FJD'), ('NLG', 'NLG'), ('JOD', 'JOD'), ('SKK', 'SKK'), ('RHD', 'RHD'), ('ISJ', 'ISJ'), ('CLF', 'CLF'), ('CHF', 'CHF'), ('PKR', 'PKR'), ('BRN', 'BRN'), ('MXV', 'MXV'), ('SSP', 'SSP'), ('GRD', 'GRD'), ('QAR', 'QAR'), ('AED', 'AED'), ('NOK', 'NOK'), ('LYD', 'LYD'), ('XAF', 'XAF'), ('SZL', 'SZL'), ('INR', 'INR'), ('PLN', 'PLN'), ('MGA', 'MGA'), ('ZMK', 'ZMK'), ('ILR', 'ILR'), ('KMF', 'KMF'), ('RON', 'RON'), ('KHR', 'KHR'), ('MDL', 'MDL'), ('DZD', 'DZD'), ('AFN', 'AFN'), ('LVL', 'LVL'), ('TPE', 'TPE'), ('CSK', 'CSK'), ('BAM', 'BAM'), ('UAH', 'UAH'), ('MDC', 'MDC'), ('HUF', 'HUF'), ('JPY', 'JPY'), ('XEU', 'XEU'), ('LTL', 'LTL'), ('IDR', 'IDR'), ('GEK', 'GEK'), ('ZRN', 'ZRN'), ('SOS', 'SOS'), ('ARL', 'ARL'), ('ZAL', 'ZAL'), ('ZWD', 'ZWD'), ('CVE', 'CVE'), ('FIM', 'FIM'), ('GWP', 'GWP'), ('YER', 'YER'), ('KGS', 'KGS'), ('PTE', 'PTE'), ('KZT', 'KZT'), ('ZWR', 'ZWR'), ('ISK', 'ISK'), ('BAD', 'BAD'), ('BGO', 'BGO'), ('CNH', 'CNH'), ('XRE', 'XRE'), ('XSU', 'XSU'), ('BWP', 'BWP'), ('RWF', 'RWF'), ('FKP', 'FKP'), ('LUL', 'LUL'), ('BZD', 'BZD'), ('BAN', 'BAN'), ('XBB', 'XBB'), ('LSL', 'LSL'), ('CAD', 'CAD'), ('ILP', 'ILP'), ('BGN', 'BGN'), ('BOB', 'BOB'), ('GHS', 'GHS'), ('PAB', 'PAB'), ('SDP', 'SDP'), ('AOK', 'AOK'), ('XAG', 'XAG'), ('VUV', 'VUV'), ('BYB', 'BYB'), ('GYD', 'GYD'), ('BDT', 'BDT'), ('GQE', 'GQE'), ('DOP', 'DOP'), ('MVP', 'MVP'), ('TRL', 'TRL'), ('PYG', 'PYG'), ('LAK', 'LAK'), ('IEP', 'IEP'), ('ADP', 'ADP'), ('CDF', 'CDF'), ('TTD', 'TTD'), ('UGS', 'UGS'), ('TWD', 'TWD'), ('GEL', 'GEL'), ('ALK', 'ALK'), ('ANG', 'ANG'), ('GHC', 'GHC'), ('VEF', 'VEF'), ('BTN', 'BTN'), ('MXP', 'MXP'), ('KPW', 'KPW'), ('LVR', 'LVR'), ('SCR', 'SCR'), ('XCD', 'XCD'), ('MGF', 'MGF'), ('BEL', 'BEL'), ('BRL', 'BRL'), ('CYP', 'CYP'), ('MUR', 'MUR'), ('NAD', 'NAD'), ('AZM', 'AZM'), ('UYU', 'UYU'), ('CLP', 'CLP'), ('EUR', 'EUR'), ('BOP', 'BOP'), ('ESP', 'ESP'), ('BUK', 'BUK'), ('PLZ', 'PLZ'), ('MWK', 'MWK'), ('LRD', 'LRD'), ('MNT', 'MNT'), ('STD', 'STD'), ('XUA', 'XUA'), ('AMD', 'AMD'), ('HRD', 'HRD'), ('AWG', 'AWG'), ('CSD', 'CSD'), ('RSD', 'RSD'), ('PGK', 'PGK'), ('MXN', 'MXN'), ('ERN', 'ERN'), ('LUF', 'LUF'), ('XPT', 'XPT'), ('NZD', 'NZD'), ('GNF', 'GNF'), ('SUR', 'SUR'), ('XBD', 'XBD'), ('GMD', 'GMD'), ('HRK', 'HRK'), ('ARM', 'ARM'), ('PEN', 'PEN'), ('STN', 'STN'), ('TZS', 'TZS'), ('MOP', 'MOP'), ('CUC', 'CUC'), ('YUD', 'YUD'), ('MVR', 'MVR'), ('COP', 'COP'), ('ILS', 'ILS'), ('TOP', 'TOP'), ('UAK', 'UAK'), ('KRO', 'KRO'), ('BRR', 'BRR'), ('TRY', 'TRY'), ('BRB', 'BRB'), ('THB', 'THB'), ('UGX', 'UGX'), ('UYW', 'UYW'), ('BOV', 'BOV'), ('CHE', 'CHE'), ('NIC', 'NIC'), ('SHP', 'SHP'), ('XBC', 'XBC'), ('MZE', 'MZE'), ('BRC', 'BRC'), ('IQD', 'IQD'), ('SLL', 'SLL'), ('MYR', 'MYR'), ('RUB', 'RUB'), ('CHW', 'CHW'), ('BND', 'BND'), ('DEM', 'DEM'), ('TMM', 'TMM'), ('SAR', 'SAR'), ('CZK', 'CZK'), ('BRE', 'BRE'), ('MCF', 'MCF'), ('KYD', 'KYD'), ('TJS', 'TJS'), ('ARP', 'ARP'), ('SRD', 'SRD'), ('MMK', 'MMK'), ('USD', 'USD'), ('MZN', 'MZN'), ('MKD', 'MKD'), ('XAU', 'XAU'), ('SRG', 'SRG'), ('GNS', 'GNS'), ('PHP', 'PHP'), ('BEC', 'BEC'), ('YDD', 'YDD'), ('AFA', 'AFA'), ('MAD', 'MAD'), ('VEB', 'VEB'), ('YUN', 'YUN'), ('BOL', 'BOL'), ('MLF', 'MLF'), ('USS', 'USS'), ('XPD', 'XPD'), ('DJF', 'DJF'), ('BBD', 'BBD'), ('ESA', 'ESA'), ('KWD', 'KWD'), ('HTG', 'HTG'), ('KRH', 'KRH'), ('XOF', 'XOF'), ('FRF', 'FRF'), ('AUD', 'AUD'), ('VND', 'VND'), ('ESB', 'ESB'), ('VNN', 'VNN'), ('CNY', 'CNY'), ('LKR', 'LKR'), ('SBD', 'SBD'), ('ZMW', 'ZMW'), ('XFU', 'XFU'), ('GTQ', 'GTQ'), ('EEK', 'EEK'), ('PES', 'PES'), ('BHD', 'BHD'), ('AON', 'AON'), ('BYR', 'BYR'), ('CUP', 'CUP'), ('ROL', 'ROL'), ('DKK', 'DKK'), ('JMD', 'JMD'), ('XDR', 'XDR'), ('ZAR', 'ZAR'), ('XTS', 'XTS'), ('LBP', 'LBP'), ('BGM', 'BGM'), ('ARS', 'ARS'), ('EGP', 'EGP'), ('MRU', 'MRU'), ('CLE', 'CLE'), ('BYN', 'BYN'), ('COU', 'COU'), ('SIT', 'SIT'), ('XXX', 'XXX'), ('XPF', 'XPF'), ('UZS', 'UZS'), ('AOA', 'AOA'), ('USN', 'USN'), ('GBP', 'GBP')], max_length=100),
        ),
    ]
